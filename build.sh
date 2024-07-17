#!/usr/bin/env bash
set -o errexit

# Install Rust
curl https://sh.rustup.rs -sSf | sh -s -- -y
source $HOME/.cargo/env

# Install dependencies
pip install -r requirements.txt
