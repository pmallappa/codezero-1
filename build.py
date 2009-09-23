#! /usr/bin/env python2.6
# -*- mode: python; coding: utf-8; -*-
#
# Top-level build script for Codezero
#
# Configures the Codezero environment, builds the kernel and userspace
# libraries, builds and packs all containers and builds the final loader
# image that contains all images.
#
import os, sys, shelve, shutil
from os.path import join
from config.projpaths import *
from config.configuration import *
from scripts.conts import containers
from configure import *

# NOTE:
# The scripts obtain all the configuration data (a set of class
# instances) from the configuration shelve, so we don't pass
# any arguments here.

def main():
    #
    # Configure
    #
    configure_kernel(join(CML2_CONFIG_SRCDIR, 'arm.cml'))

    #
    # Build the kernel
    #
    print "\nBuilding the kernel..."
    os.chdir(PROJROOT)
    os.system("scons")

    #
    # Build userspace libraries
    #
    print "\nBuilding userspace libraries..."
    os.system('scons -f SConstruct.userlibs')

    #
    # Build containers
    #
    print "\nBuilding containers..."
    containers.build_all_containers()

    #
    # Build libs and loader
    #
    os.chdir(PROJROOT)
    print "\nBuilding the loader and packing..."
    os.system("scons -f SConstruct.loader")

if __name__ == "__main__":
    main()