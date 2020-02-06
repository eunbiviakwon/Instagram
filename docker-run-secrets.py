#!/usr/bin/env python
# poetry export
# docker build
# docker stop
# docker run(bash, background mode)
# docker cp secrets.json

# ./docker-run-secrets.py <cmd>
# 뒤에 <cmd> 내용을 docker run <cmd>처럼 실행해주기
# 지정하지 않으면 /bin/bash 실행
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('cmd', type=str, nargs=argparse.REMAINDER)
args = parser.parse_args()

DOCKER_OPTIONS = [
    ('--rm', ''),
    ('-it', ''),

    ('-d', ''),
    ('-p', '8001:80'),
    ('--name', 'instagram'),
]
DOCKER_IMAGE_TAG = 'azelf/wps-instagram'

# poetry export로 docker build시 사용할 requirements.txt 작성
subprocess.run(f'poetry export -f requirements.txt > requirements.txt', shell=True)

# secrets.json이 없는 이미지를 build
subprocess.run(f'docker build -t {DOCKER_IMAGE_TAG} -f Dockerfile .', shell=True)

# 이미 실행되고 있는 name=instagram인 containter를 종료
subprocess.run(f'docker stop instagram', shell=True)

# secrets.json이 없는 상태로 docker run으로 bash를 실행 -> background로 들어감
subprocess.run('docker run {options} {tag} /bin/bash'.format(
    options=' '.join([
        f'{key} {value}' for key, value in DOCKER_OPTIONS
    ]),
    tag=DOCKER_IMAGE_TAG,
), shell=True)

# secrets.json을 전송
subprocess.run('docker cp secrets.json instagram:/srv/instagram', shell=True)
subprocess.run('docker exec instagram /srv/instagram/app/manage.py collectstatic --noinput', shell=True)
# bash실행
# subprocess.run('docker exec -it instagram /bin/bash', shell=True)


subprocess.run('docker exec -it instagram {cmd}'.format(
    cmd=' '.join(args.cmd) if args.cmd else 'supervisord -c ../.config/supervisord.conf -n'
), shell=True)
# runserver명령을 전송
# subprocess.run('docker exec -it instagram python manage.py runserver 0:8000', shell=True)

