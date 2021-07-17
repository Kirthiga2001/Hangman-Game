import cv2
import random

def f(c):
    if c==1:
        i=cv2.imread("1.png")

    elif c==2:
        i=cv2.imread("2.png")

    elif c==3:
        i=cv2.imread("3.png")

    elif c==4:
        i=cv2.imread("4.png")

    elif c==5:
        i=cv2.imread("5.png")

    elif c==6:
        i=cv2.imread("6.png")

    elif c==7:
        i=cv2.imread("7.png")
    elif c==8:
        i = cv2.imread("8.png")
    else:
        i=cv2.imread("9.png")
    ir=cv2.resize(i,(500,500))
    cv2.imshow("Hangman", ir)
    cv2.waitKey(100)

c=9
print("*"*100)
x=int(input("No of players(1 or 2) = "))
if x==1:
    p=["ball","cat","doll","elephant","fish","goat","horse","kite","sheep"]
    l=len(p)
    a=random.randrange(0,l,1)
    s=p[a].strip()
else:
    p1=input("Enter Player 1 name: ")
    p2=input("Enter Player 2 name: ")
    print(p1,"Peek out till",p2,"Gives word to you")
    print("*" * 100)
    s=input("Enter the word for",p1,"(in small letters) : ").strip()
print("*" * 100)
print("_"*len(s))
print("You have",c-1,"Chances left")
print("*" * 100)
sl,k=[],[]
for i in range(len(s)):
    sl.append("_")
f(c)
while(c):
    a=input("Enter a letter(in lower case): ").strip()
    if a not in k:
        k.append((a))
    else:
        print("Letter already choosed, choose a different letter apart from",k)
        a = input("Enter a letter(in lower case) : ")
    if a not in s:
        c-=1
        if c==1:
            f(c)
            print("Try again!!!")
            exit()
    else:
        for i in range(len(sl)):
            if s[i]==a:
                sl[i]=a
    if sl.count("_")==0:
        print("You won!!!")
        exit()
    f(c)

    print(*sl)
    print("*" * 100)



