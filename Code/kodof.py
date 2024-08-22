from random import *
import time

hp  = 100
ehp = 100
maxultp = 10
ult = 0
ultp = 0
pat = ("\n\n(공격:1 수면:2 선생님 부르기: 3《궁극기》: 4 도망: 5)")

print("《죽거나 죽이거나 도망치거나》")
dif = input("난이도 설정: 쉬움:1 보통:2 어려움:3 김정은:4\n")

name = input("적 이름:")
name = str(name)

print("\n야생의 ",name,"이/가 나타났다!")
print("\n《궁극기》 사용까지 남은 횟수: ",maxultp - ultp - 1,"\n")
esc = 0

while esc == 0:    
        
    time.sleep(0.1)
    print(pat,"\n")
    type = input()  
    ultp = ultp + 1
    
    if maxultp - ultp < 0:
        print("\n《궁극기》 사용까지 남은 횟수: 0\n")
        
    else: print("\n《궁극기》 사용까지 남은 횟수: ",maxultp - ultp - 1,"\n")
    if ultp >= 9:
            print("---------‐---------------------------------------------")
            print("《궁극기》 사용가능")
            print("---------‐---------------------------------------------\n")
    
    
    if type == "1":
        atk = randint(1, 20)
        ehp = ehp - atk
        print(name,"를 공격했다!\n",atk,"의 데미지")
        print(name,"의 체력은(",ehp,"/100)")
   
    if type == "2":
        sleep =randint(1, 10) and randint(40, 50)
        hp = hp + sleep
        
        if hp > 100:
            hp = 100
            
        print("당신은 아까 꾸던 꿈을 회생하며, 잠시 눈을 감습니다. ")
        print("몽환 속에서도 느껴지는 살기에 눈을 뜬 당신은 \n",name,"이/가 싸가지없는 눈빛으로 당신을 노려보는 것을 발견합니다.\n퇴학을 면하고 싶다면 목숨을 걸어야 할 것입니다.\n")
        print(sleep,"을/를 회복했습니다.")
        print("현재 내 체력은(",hp,"/100)")
    
    if type == "3":
        print("국어 선생님:1 수학 선생님: 2 영어 선생님:3")
        tchr = input()
        
        if tchr == '1':
            print("선생님이 출장 가셔서 자습을 준다")
            print(name,"를 공격했다!\n0의 데미지")
            print(name,"의 체력은(",ehp,"/100)")
        
        if tchr == "2":
            print("합성 함수를 시전한다.")
            atk = randint(1, 5)
            
            def funcA(x):
                global y
                y = x ** 2 -2 * x + 1
    
            def funcB(a):
                global b
                b = 2 * a
                
            funcA(atk)
            funcB(y)
            ehp = ehp - b
            print("y = (x-1)^2, y= 2x")
            print("합성 전: ",atk," 합성 후:",b)
            print(name,"를 공격했다!\n",b,"의 데미지")
            print(name,"의 체력은(",ehp,"/100)")
            
        if tchr == "3":
            print("영어본문을  읽어 잠에 빠지게 한다")
            sleep = randint(40, 50) 
            entype = randint(1, 2)
            eatk = randint(10, 25)
            
            if entype == 1:
                hp = hp - eatk
                print("당신은 자다가 선생님에의해서 깼습니다.")
                print(eatk,"의 데미지")
                print("현재 내 체력은(",hp,"/100)")
            
            if entype == 2:
                hp = hp + sleep
                
                if hp > 100:
                    hp = 100
                    
                print("당신은 깊게 잠들었습니다.")
                print(sleep,"을/를 회복했습니다.")
                print("현재 내 체력은(",hp,"/100)")
              
    if type == "5":
        esc = 1
        print("당신은 ",name,"(으)로부터 도망쳤습니다.\n GAME OVER")
        
    if type == "4":
       if ultp >= 10:
            if dif == "1": 
                power = 50
            
            if dif == "2":
                power = 50
            
            if dif == "3":
                power = 65
                
            if dif == "4":
                power = 75
                
            ehp = ehp - power
            print("《궁극기》\n")
            print(name,"을/를 공격했다!\n",power,"의 데미지")
            print(name,"의 체력은(",ehp,"/100)")
            ultp = 0
        
       if ultp < 10:
            print ("《궁극기》사용 불가\n")
        
    if ehp <= 0:
        esc = 1
        print("\n당신은 ",name,"(으)로 부터 이겼습니다.")
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        print("GAME OVER")
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
       
       
    if esc == 0:
        time.sleep(1.5)
        etype = randint(1, 2)
        
        if etype == 1:
            print("\n",name,"의 반격!")
            
            if dif == "1":
                eatk = randint(0, 15)
                
            if dif == "2":
                eatk = randint(1, 25)
               
            if dif == "3":
                eatk = randint(30, 50)
                
            if dif == "4":
                eatk = randint(50, 80)
                
            hp = hp - eatk
            print(eatk,"의 데미지")
            print("현재 내 체력은(",hp,"/100)")
            print("-------------------------------------------------------")
            
        if etype == 2:
            if dif == "1":
                esleep = randint(1, 15)
                
            if dif == "2":
                esleep = randint(1, 30)
            
            if dif == "3":
                esleep = randint(20, 40)
                
            if dif == "4":
                esleep = randint(40, 80)
             
            ehp = ehp + esleep
            
            if ehp > 100:
                ehp = 100
                
            print("\n",name, "이/가 ", esleep,"을/를 회복했다!")
            print(name,"의 체력은(",ehp,"/100)")      
            print("----------‐--------------------------------------------")
    
    if hp <=  0:
       esc = 1
       print("\n당신은 ",name,"(으)로 부터 졌습니다.")
       print("-------------------------------------------------------")
       print("-------------------------------------------------------")
       print("GAME OVER")
       print("-------------------------------------------------------")
       print("-------------------------------------------------------")
