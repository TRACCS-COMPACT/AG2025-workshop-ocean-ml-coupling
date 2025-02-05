# AG 2025 - AI/Ocean coupling

The repository contains pre-requisites steps for "AI / Ocean model coupling" workshop at TRACCS General Assembly 2025.

Workshop requires specific dependencies. We provide container images from Apptainer with ready-to-use environment.

## Install Apptainer

### Apptainer for Linux

    # Ubuntu
    # ------
    sudo apt update && sudo apt install -y software-properties-common
    sudo add-apt-repository -y ppa:apptainer/ppa
    sudo apt update && sudo apt install -y apptainer

    # Debian (amd64 ONLY)
    # -------------------
    sudo apt update
    sudo apt install -y wget
    cd /tmp
    wget https://github.com/apptainer/apptainer/releases/download/v1.3.6/apptainer_1.3.6_amd64.deb
    sudo apt install -y ./apptainer_1.3.6_amd64.deb

For other Linux distributions, please refer to this [guide](https://github.com/apptainer/apptainer/blob/main/INSTALL.md).

### Apptainer for macOS

Apptainer is available on macOS via LIMA (LInux virtual MAchines):

    # Install with brew
    # -----------------
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew install qemu lima

    # Install with macports
    # ---------------------
    sudo port install qemu lima

Create and run Linux VM with Apptainer:

    limactl start template://apptainer
    limactl shell apptainer
    # IMPORTANT: type 'cd' to go in VM home, 'pwd' should return '/home/<your_name>.linux'
    cd 

Some optional tips:

    # NB1: copy files from VM to host
    limactl cp apptainer:/path/to/file  /host/destination
    
    # NB2: remove VM on host
    limactl stop apptainer
    rm -rf ~/.lima/apptainer

## Download and run container

[Morays](https://github.com/morays-community) is an organization that hosts material for coupled Ocean-ML. Container is there.

Identify your hardware architecture (in VM)

    uname -m
    #  aarch64 --> arm64
    #  x86_64  --> amd64
    ARCH=arm64

Download image (for macOS: type "cd" to be in VM home or it won't work)

    wget https://github.com/morays-community/morays-doc/releases/download/containers/morays_env_${ARCH}.sif

Run container

    apptainer run --writable-tmpfs --bind $(pwd):/home/jdoe/morays_tutorial morays_env_${ARCH}.sif
    # should print " >>>> Welcome in Morays environment ! <<<< "

## Tutorial

When container is running, you can start [here](https://morays-doc.readthedocs.io/en/latest/nemo.tuto.html).
