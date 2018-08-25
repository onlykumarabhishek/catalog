#!/usr/bin/env python3

from os import mkdir
from os.path import isdir
from shutil import rmtree, copytree
from sys import argv, exit

SRCDIR = 'src'
DISTDIR = '_dist'

if len(argv) != 2:
    exit("Usage: copy.py GIT_TAG")

# Get name and version
name, version = argv[1].split('-', 1)

if not isdir(f'{SRCDIR}/{name}'):
    exit("GIT_TAG arg must be in format name-version e.g. memcached-v0.0.1")

# Clean DISTDIR
if isdir(DISTDIR):
    rmtree(DISTDIR)
mkdir(DISTDIR)

# Copy {name} and _common
copytree(f'{SRCDIR}/{name}', f'{DISTDIR}/{name}/{version}')
