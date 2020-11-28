import sys

# f = sys.stdin
while True:
    menu = input ("메뉴를 선택하세요\n1. 영화 예매\n2. 종료\n")
    if menu == '1':
        print("1번을 선택하셨습니다.")
        f = open('movielist.txt', 'rt', encoding='UTF8')
        movieNum = 0
        movieNameList = []
        while(1):
            M = f.readline()
            if '\n' in M:
                M = M.replace('\n','')
            if M == '':
                break
            movieNameList.append(M)
            movieNum = movieNum + 1
        while(1):
            for i in range(movieNum):
                print(i+1,".", movieNameList[i])
            i = input("\n숫자를 입력해 영화를 선택하세요 : ")
            i = int(i)
            moviename = movieNameList[i - 1]
            print(i, "번", moviename, "을 선택하셨습니다.\n") #2주차 과제
            Choice = input("예매를 진행하시겠습니까? \n1.예 2.아니오\n")
            if Choice == '1':
                print("\n영화 시간입니다.")
                f = open('movietime.txt', 'rt', encoding='UTF8')
                timeList = []
                while(1):
                    L = f.readline()
                    if '\n' in L:
                        L = L.replace('\n','')
                    if L == '':
                        break
                    timeList.append(L)
                while(1):
                    print(timeList[i-1])
                    List = input("\n시간을 선택해주세요 : ")
                    if List in timeList[i-1]:
                        print(List, "을 선택하셨습니다.\n")
                        Choice = input("예매를 진행하시겠습니까? \n1.예 2.아니오\n")
                        if Choice == '1':
                            adult = 12000
                            youth = 7000
                            while(1):
                                print("\n인원을 선택해주세요") # 숫자만 눌렀다고 가정
                                n = int(input("성인 인원수를 입력해주세요: "))
                                N = int(input("청소년 인원수을 입력해주세요: "))
                                print("\n성인", n,"명,","청소년", N, "명을 선택하셨습니다.")
                                print("금액은", adult*n,"," ,youth*N, "원 입니다.")
                                print("총 금액은", adult*n + youth*N, "원 입니다.\n")
                                Choice = input("예매를 진행하시겠습니까? \n1.예 2.아니오\n")
                                if Choice == '1':
                                    seatlist = [['o', 'o', 'o'],
                                                ['o', 'o', 'o'],
                                                ['o', 'o', 'o']]
                                    print("좌석을 선택해 주세요.") # 4주차는 좌석 시각화까지
                                    for i in range(3):
                                        print(i*3+1, i*3+2, i*3+3)
                                        break # 5주차를 위한 멈춤
                                elif Choice == '2':
                                    print("이전메뉴로 돌아갑니다.\n")
                                    continue
                                else:
                                    print("잘못 입력하셨습니다.")
                        elif Choice == '2':
                            print("이전메뉴로 돌아갑니다.\n")
                            continue
                        else:
                            print("잘못 입력하셨습니다.")
                    else:
                        print("\n맞는 시간을 입력하세요")
                        continue
            elif Choice == '2':
                print("이전메뉴로 돌아갑니다.\n")
                continue
            else:
                print("잘못 입력하셨습니다.")
    elif menu == '2': 
        print("프로그램을 종료합니다.") 
        break 
    else: 
        print("잘못 입력하셨습니다.")