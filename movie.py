import sys

# f = sys.stdin
while True:
    menu = input ("메뉴를 선택하세요\n1. 영화 예매\n2. 종료\n")
    if menu == '1':
        #1 선택시 영화 리스트 생성(2주차)
        print("1번을 선택하셨습니다.")
    elif menu == '2':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다.")


