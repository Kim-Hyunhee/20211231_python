# DB를 조회 / 수정 / 삭제 / 추가 등등 => DB를 제어 (Control)
# 모델을 이용해 데이터를 컨트롤 => Controller

# DB 연결 / 쿼리 / 결과 분석 표시 등등
# 데이터베이스와 관련된 파이썬 코드
from pymysql import connect
from pymysql.cursors import DictCursor  # DB SELECT 결과를 dict 형태로 가져오게 해주는 클래스

# connect 함수를 직접 import => pymysql  코드 생략
db = connect (
    host = 'finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
    port = 3306, # port : 한 대의 컴퓨터가 여러 개의 프로그램을 돌릴 때 -> 각각의 (인터넷을 통해서) 프로그램을 찾아갈 때 사용하는 고유 번호
                 # => mysql : 보통 3306번 포트에 실행시켜 두는 것이 일반적 
    user = 'admin',
    passwd = 'Vmfhwprxm!123',  # 프로젝트!123 (첫 글자만 대문자)    
    db = 'test_202112_python',  # 호스트에 있는 여러 논리DB 중 사용할 DB 선정
    charset = 'utf8',  # 연결할 DB가 한글을 utf8 인코딩으로 한글 처리 진행할 예정
    cursorclass = DictCursor 
)

# 쿼리 수행 전담 변수  (연결된 DB에서 수행)
cursor = db.cursor()

# 필요 기능들을 함수로 작성

def get_user_list():
    sql = f"SELECT * FROM users"
    cursor.execute(sql)
    
    result = cursor.fetchall()
    
    # API => 원하는 쿼리의 수행 결과를 가공해서 화면단에서 사용할 수 있게 전달해주는 역할
    return result