# 큰따옴표나 작은따옴표로 묶어주면 문자열 데이터로 취급한다.
memo = 'Hello\nWorld'
print(memo)
print('*' * 75)

# 큰따옴표 3개를 사용하면 여러줄 문자열을 만들 수 있다.
memo = """개울가에
올챙이 한마리
꼬물꼬물 헤엄치다."""
print(memo)
print('*' * 75)
memo = '''앞다리가 쏘옥
뒷다리가 쑤욱
팔딱팔딱 메뚜기됬네'''
print(memo)
print('*' * 75)

# 문자열 인덱싱(1문자 꺼내기), 문자열 슬라이싱(범위를 지정해서 여러 문자 꺼내기)
# 인덱싱은 문자열의 특정 위치의 1문자를 얻어오는 것을 의미하고 슬라이싱은 여러문자를 잘라내는 것을
# 의미한다.
string = 'We are the champions, My friend!'

# 인덱싱 => 문자열변수[인덱스]
print(string[0]) # W
print(string[11]) # c
print(string[-1]) # !
print('*' * 75)

# 슬라이싱 => 문자열변수[시작위치:끝위치]
# 문자열에서 시작 위치 부터 끝 위치 - 1 번째 문자열을 얻어온다.
print(string[3:6]) # are
print(string[11:20]) # champions
# 스라이싱을 할 때 시작 위치를 생략하면 처음 부터를 의미하고 끝 위치를 생략하면 마지막 까지를 의미한다.
print(string[:20]) # We are the champions
print(string[22:]) # My friend!
print('*' * 75)

# 인덱싱이나 슬라이싱을 이용해서 문자열의 일부를 수정할 수 없다.
string = 'pithon'
print(string)
print(string[1])
# string[1] = 'y' # 에러 발생
print(string[1:2])
# string[1:2] = 'y' # 에러 발생
print(string[:1]) # P
print(string[2:]) # thon
string = string[:1] + 'y' + string[2:]
print(string)
print('*' * 75)

# 8304221185600
jumin = input('주민등록번호 13자리를 "-"없이 입력하세요 : ')
print(jumin[6])
print(jumin[0:2])
print(jumin[2:4])
print(jumin[4:6])












