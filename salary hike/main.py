print("===========employee salary hike=======")
cur_sal_of_l3=150000
cur_sal_of_l4=100000
cur_sal_of_l5=75000

print('''1==level3
       2==level4
       3==level5''')
option=int(input("enter option:"))
if option==1:
    new_salary=(cur_sal_of_l3*0.15)+cur_sal_of_l3
    print("employee new_salary:",new_salary)
elif option==2:
    new_salary=(cur_sal_of_l4*0.07)+cur_sal_of_l4
    print("employee new_salary:", new_salary)
elif option==3:
    new_salary=(cur_sal_of_l5*0.05)+cur_sal_of_l5
    print("employee new_salary:", new_salary)
else:
    print("invailed job level")
