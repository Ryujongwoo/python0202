# input() 함수로 입력받기

# 변수(variable)는 처리할 데이터(상수)를 저장시키는 기억장소를 말한다.
# 변수 이름 작성방법
# 영문자, 숫자, 특수문자(_)만 사용할 수 있으며 대문자와 소문자를 구분한다.
# 변수 이름은 반드시 문자로 시작해야 하고 예약어는 사용할 수 없다.

# 변수를 선언할 때 C, C++, JAVA 언어와 달리 변수의 자료형을 지정하지 않으며 변수에 저장되는 데이터의
# 타입에 따라서 자동으로 변수의 타입이 결정된다.
# '='는 같다라는 의미로 사용되지 않고 '=' 오른쪽의 데이터를 '=' 왼쪽의 기억장소에 저장시키라는 의미로
# 사용된다. => 대입문 => '=='을 사용해야 '같다'로 인식한다.

name = '홍길동'
print(name)
# type() 함수는 인수로 지정된 기억장소의 자료형을 얻어온다.
print(type(name))
age = 20
print(age)
print(type(age))
height = 181.5
print(height)
print(type(height))
# 논리값 True와 False는 반드시 첫 문자만 대문자로 사용한다.
isGender = True # 논리값을 기억하는 변수 이름은 'is'로 시작하는 것이 관행이다.
print(isGender)
print(type(isGender))
none = None # 빈 변수를 만든다.
print(none)
print(type(none))
name = 10
print(name)
print(type(name))

# 변수를 제거하려면 del 명령어를 사용한다.
del name
# print(name) # 변수를 메모리에서 제거했으므로 에러가 발생된다.
print('=' * 50)

# =====================================================================================================

# input() 함수는 키보드로 입력받는 모든 데이터를 문자열 형태로 입력 받는다.

# 문장이 '#'로 시작하면 한 줄 주석이고 작은따옴표 3개 사이에 쓰면 여러 줄(범위) 주석이 된다.
'''
print('이름을 입력하세요 : ', end = '')
name = input() # 키보드로 문자열을 입력받아 name이라는 변수에 저장한다.
print('%s님 안녕하세요' % name)
print('{}님 안녕하세요'.format(name))
print('{0}님 안녕하세요'.format(name))
print('{0:10s}님 안녕하세요'.format(name))
print(f'{name}님 안녕하세요')
print('=' * 50)

# input() 함수의 인수로 문자열을 입력하면 입력받기 전에 문자열을 메시지로 출력한다.
nickname = input('별명을 입력하세요 : ')

# int() 함수는 () 안에 인수로 지정된 문자열을 정수로 변환한다.
# float() 함수는 () 안에 인수로 지정된 문자열을 실수로 변환한다.
age = input('나이를 입력하세요 : ')
print('{}님은 {}살 입니다.'.format(nickname, age))
print('{}님은 내년에 {}살 입니다.'.format(nickname, float(age) + 1))

# split(구분자) : 문자열을 구분자를 경계로 분리한다. 나눈다. 쪼갠다. => 구분자를 생략하면 공백이 기본값
name, age = input('이름과 나이를 입력하세요 : ').split(',')
print('{}님은 {}살 입니다.'.format(name, age))

python, java, jsp = input('3과목 점수를 입력하세요 : ').split()
# '+' 연산자는 숫자와 숫자 사이에 있으면 덧셈을 하고 문자열과 문자열 사이에 있으면 문자열을 연결한다.
# 숫자와 문자열 또는 문자열과 숫자 사이에 있으면 에러가 발생된다.
print('총점 : {}'.format(python + java + jsp))
print('총점 : {}'.format(int(python) + int(java) + int(jsp)))
'''

# map() 함수를 사용해서 입력받은 데이터를 일괄적으로 숫자로 변환시킬 수 있다.
python, java, jsp = map(int, input('3과목 점수를 입력하세요 : ').split())
print('총점 : {}'.format(python + java + jsp))















