# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()
t=name1.count("t")
r=name1.count("r")
u=name1.count("u")
e=name1.count("e")

t2=name2.count("t")
r2=name2.count("r")
u2=name2.count("u")
e2=name2.count("e")

l=name1.count("l")
o=name1.count("o")
v=name1.count("v")
e=name1.count("e")

l2=name2.count("l")
o2=name2.count("o")
v2=name2.count("v")
e2=name2.count("e")

total1=t+r+u+e+t2+r2+u2+e2
total2=l+o+v+e+l2+o2+v2+e2
love= str(total1) + str(total2)
love=int(love)

if (love < 10) or (love > 90):
    
    print(f"Your score is {love}, you go together like coke and mentos.")
elif (love >= 40) and (love <= 50):
     print(f"Your score is {love}, you are alright together.")
else:
    print(f"your score is {love}")