# R4Pi Project dependency management

We used to do this with ansible, but it was unnecessarily difficult to run in
the local environment, so we wrote our own.

This is not a general purpose dependency management solution, but rather a tool
to specifically address our problem in a way that works for us.

## What is it?

A simple command line tool that requires no additional dependencies on the
Raspberry Pi OS. Dependencies are stored in a json file and grouped under a key 
related to the build project.

Current build projects include:

* build - for building R itself
* packages - for bulding our current package set

## Usage

change into the correct directory and run `./install-deps.py`.

Output:

``` default
Available commands:
* build
* packages
```

To install a specifc set of dependencies, use one of the available commands.

eg.

``` bash
./install-deps.py packages
```

## License

Copyright (c) 2022 R4Pi.org authors - Released under the MIT License

