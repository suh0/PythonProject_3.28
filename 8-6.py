ss=input("날짜(연/월/일) 입력 ==> ")

ssList=ss.split('/')

print("입력한 날짜의 10년 후 ==> ",end='')
print(str(int(ssList[0])+10)+"년", end='')
print(ssList[1]+"월", end='')
print(ssList[2]+"일")