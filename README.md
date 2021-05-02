# naver-blog-posting

python selenium을 이용하여 네이버 글쓰기를 자동화하는 프로그램.

## 유의사항

edge 브라우저와 mac os를 사용하고 있다면 소스코드에서 ID, 비밀번호를 설정해두고 드라이버만 다운받아 설치하면 된다.

### ID / PASSWORD 설정

`main.py` 내에 블로그 ID, 계정 ID, 계정 비밀번호를 변경해야 동작한다.

```python
...
blog_id = '블로그 ID'
login_id = '계정 로그인 ID (따로 설정하지 않았으면 블로그 ID와 동일)'
password = '비밀번호'
...
```

### 드라이버 설정

브라우저에 맞는 드라이버를 설치해야 정상적으로 작동한다. 또한, 현재 컴퓨터에 설치되어 있는 브라우저 버전과 일치하는 버전을 받아야 한다.

- [Google Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [Microsoft Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

그리고, 다운로드 받은 드라이버를 python 파일과 동일한 위치에 두고 아래와 같이 드라이버 설정을 해야한다.

```python
# edge 브라우저를 사용하는 경우
driver = webdriver.Edge(executable_path='./드라이버_파일명', capabilities={})

# chrome 브라우저를 사용하는 경우
driver = webdriver.Chrome(executable_path='./드라이버_파일명', capabilities={})
```

### 키보드 단축키 설정

네이버 로그인 시 CAPTCHA 인증을 우회하기 위해서는 아이디와 비밀번호를 입력할 때 `send_keys` 메소드를 직접 호출하지 않고 `복사-붙여넣기`를 해야한다.
이 때 키를 입력해야 하는데, OS별 단축키가 다르다. MAC인 경우에는 원본 코드과 동일하게 `Keys.COMMAND`를 사용하면 되고, 윈도우인 경우에는 `Keys.CONTROL`을 사용해야 한다.

## 참고 링크

- [python selenium 참고](https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage)
- [네이버 글쓰기 소스코드 참고](http://blog.naver.com/freed0om/222009447800)