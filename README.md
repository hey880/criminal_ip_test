# Crimianl IP API APP

OSINT 검색 도구인 Criminal IP의 API를 활용하여 만든 파이썬(python 3.11.2 사용) 앱입니다.\
Asset Search, Asset Search (IP검색) 리포트 조회, Domain Scan, Domain Scan 리포트 조회 API를 호출하도록 구현했습니다.


## Development

앱 실행

```
1) 가상 환경 생성
python -m venv venv

2) 가상 환경 활성화
# mac, linux 환경
. venv/bin/activate 

# window 환경
. venv/Scripts/activate

3) 모듈 설치
pip install -r requirements.txt

4) .env 파일 추가
.env 파일을 생성하고 CRIMINAL_IP_API_KEY 상수를 선언하고 Criminal IP 계정에 부여된 API Key를 저장해주세요.
ex) CRIMINAL_IP_API_KEY="나의apikey"
 
5) 실행
python main.py
```