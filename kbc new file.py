print("\tWEL-COME TO K.B.C (KON BANEGA COROREPATI)")



question_list = [
    "1. How many continents are there?",              # pehla question
    "2. What is the capital of India?",            # doosra question
    "3. NG mei kaun se course padhaya jaata hai?",    # teesra question
    "4. 1. sampat pal devi ne bundelkhand me mahilao k khilaf hone wali hinsa ko rokane k liye kis dal ki sthapna ki thi?",
    "5. inme se kis bimari ko  dimagi bukhar k  name se jana jata he ?",
    "6. candy crus saga , tempal run or farut ninza kiske prkar he ? ",
    "7. film 'hiropanti' me bator nayak kadam rakhne wale tiger kis abhineta k bete he?",
    "8. india me konsa pad ek nirvachit pad he?",
    "9. inme se kon ramayan k mukhya patro me se ek he jo mahabharat me bhi nazar aate he?",
    "10. hamare sor mandal me sabse badi vastu kya he?"
]
options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
    ["lakshmi bai","nari mukti vahini","mahila morcha","gulabi gang"],
    ["japani insefalitis","tatnas"," dangu","rabiz"],
    ["chat masanger","anty virus", "games", "search enjan"],
    ["sunil shatty","sany deol","anil kapoor","jacy saraf"],
    ["bharat k mukhya nyayadhish","mukhya chunav aayukt","bharat ke rastrapti","rajyapal"],
    ["hanuman","vedvyas","dashrath","duryodhan"],
    ["titan","sun","alfa sentory","jupitar"]
]
win_ammount = [10000,50000,100000,500000,1000000,2500000,5000000,10000000,50000000,70000000]
solution_list = [3, 4,1,4,1,3,4,3,1,4] 
solution_list2 = ["seven","Delhi","Software Engineering","gulabi gang","japani insefalitis","games","jacy sraf","bharat ke rastrapati","hanuman","jupitar"]
a = 0
l = 1
Q = len(question_list)
while a< len(question_list):
    print("\n\t aapka sawal he",win_ammount[a], "ke liye ye rha ")
    print("\n",question_list[a])
    c = 1
    life = 0
    for x in options_list[a]:
        print("\n",c,x)
        c += 1
    print("have you 1 chance you can used a lifeline 5050")
    A = 5050
    user_input = int(input("\nenter your answer:-  "))
    if user_input == solution_list[a]:
        print("\nCongrats! Aapka answer sahi hai aap ne jeet liye he",win_ammount[a])
    elif user_input == A:
        if user_input == A and l <= 1:
            l+=1
            print("1.",solution_list2[a] ,"or","2.",options_list[a][1] )
            life_line=(input("selact any one ANSWER IS your life_line:- "))
            if (life_line == solution_list2[a] or int(life_line) == 1):
                print("Congrats! Aapka answer sahi hai your aapki lifeline is not west you win now",win_ammount[a])
            else:
                print("sory try bettar luck next time apka ye ansar bhi wrong he apne keval",win_ammount[a],"hi jeet paye hhe")
                print(solution_list[a],solution_list2[a],"sahi answer tha")

                break
        else:
            print("you have alredy use your life line sorry you loss , only win:-",win_ammount[a])
            break
    else:
        print(" sorry your answer is wrong so you loss only you win",win_ammount[a])
        break
    # break    
    a+=1  





