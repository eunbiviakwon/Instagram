# Instagram

## Requirements

- Python (>3.6)
- Secrets JSON File



## Installation

```
pip install -r requirements.txt
```



## Secrets JSON File

`<project root>/secrets.json`

```json
{
  "AWS_ACCESS_KEY_ID": "<AWS AccessKeyID (S3 permission)>",
  "AWS_SECRET_ACCESS_KEY": "<AWS SecretAccessKey (S3 permission)>"
}
```



## Run development server

```
python manage.py runserver
```



## EC2에 Docker배포

1. 로컬에서 이미지 생성, 실행 확인
2. DockerHub에 저장소 생성
3. 로컬 이미지에 태그 추가  
   `docker tag <로컬이미지명> <저장소명>`
4. DockerHub에 이미지 Push  
   `docker push <저장소명>`
5. EC2에 Docker설치
6. EC2에서 docker run명령어 실행  
   `docker run --rm -it -p 80:8000 <저장소명>`

docker설치 및 run명령어 실행하는 부분을 `deploy-docker.sh` 안에 적절히 작성하기