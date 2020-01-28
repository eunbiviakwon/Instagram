#!/usr/bin/env sh
IDENTITY_FILE="$HOME/.ssh/wps12th.pem"
USER="ubuntu"
HOST="15.164.222.130"
TARGET=${USER}@${HOST}
ORIGIN_SOURCE="$HOME/projects/fastcampus/12th/instagram/"
DEST_SOURCE="/srv/"
SSH_CMD="ssh -i ${IDENTITY_FILE} ${TARGET}"

echo "== Docker 배포 =="

# 서버 초기설정
echo "apt update & upgrade & autoremove"
${SSH_CMD} -C 'sudo apt update && sudo DEBIAN_FRONTEND=noninteractive apt dist-upgrade -y && apt -y autoremove'
echo "apt install python3-pip"
${SSH_CMD} -C 'sudo apt -y install python3-pip'

# pip freeze
echo "pip freeze"
"$HOME"/.pyenv/versions/3.7.5/envs/wps-instagram/bin/pip freeze > "$HOME"/projects/fastcampus/12th/instagram/requirements.txt

echo "  finish!"
