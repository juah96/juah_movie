import sys

# f = sys.stdin
while True:
    menu = input ("메뉴를 선택하세요\n1. 영화 예매\n2. 종료\n")
    if menu == '1':
        #1 선택시 영화 리스트 생성(2주차)
        print("1번을 선택하셨습니다.")
        f = open('movielist.txt', 'rt', encoding='UTF8')
        movieNum = 1
        movieNameList = []
        while(1):
            M = f.readline()
            if '\n' in M:
                M = M.replace('\n','')
            if M == '':
                break
            print(movieNum,".", M)
            movieNameList.append(M)
            movieNum = movieNum + 1
        i = input("숫자를 입력해 영화를 선택하세요 : ")
        i = int(i)
        moviename = movieNameList[i - 1]
        print(i, "번", moviename, "을 선택하셨습니다.")
        break
    elif menu == '2':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다.")


