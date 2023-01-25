'''
Ex07-1-for

for 문
    값의 범위나 횟수가 정해져 있을 때
    사용하면 편리한 반복문
    while문 보다 자주 사용된다.

for 변수 in 반복가능한객체
    반복실행문
'''

# pwd = 'abcdefg55'
pwd = input('비밀번호를 입력하세요 >>>')


ch_count = 0
num_count = 0
for ch in pwd:
        if ch.isalpha(): #문자여부 판단
            ch_count += 1 #  만약 문자라면 ch_count에 1을 추가
        elif ch.isnumeric(): #숫자여부 판단
            num_count += 1  # 만약 숫자라면 num_count에 1을 추가

if ch_count > 0 and num_count > 0: # 만약 ch count와 num count가 0보다 크다면
    print('가능한 비밀번호 입니다.')
else:                              # 아니라면
    print('불가능한 비밀번호 입니다.')

'''


'''