#Task Log Analyzer
# def log_analyzer(logs):
#     unique_user=set()
#     count_action={}
#     for log in logs:
#         parts=log.split()
#         user=parts[1]
#         unique_user.add(user)
#         if user in count_action:
#             count_action[user]=+1
#         else:
#             count_action[user]=1
    
#     top_user=max(count_action,key=count_action.get)
#     return unique_user,count_action,top_user
# logs=[
#     "10:00:1 login:Ahmed",
#     "10:05:2 login:Ali",
#     "10:10:3 logout:Mughees",
#     "10:10:4 update:Mohsan"
# ]
# user,count,top_user=log_analyzer(logs)

# print("unique User",user)

# print("Action Count",count)
# print("Top active User",top_user)

#Task 2 Map,Filter,Reduce
#Map 
# numbers=[1,2,3,4]
# result=list(map(lambda x:x*2,numbers))
# print(result)
#Filter
# numbers=[1,2,3,4,5,6]
# result=list(filter(lambda x:x%2==0,numbers))
# print(result)
#reduce
# from functools import reduce
# numbers=[1,2,3,4,5,6]
# result=reduce(lambda x,y:x+y,numbers)
# print(result)
#remove Odd number
# num=[1,2,3,4,5,6]
# res=list(filter(lambda x:x%2==0,num))
# print(res)
# #Square The Number
# res=list(map(lambda x:x**2,res))
# print(res)

#Time Complexity Task
#basicaly set is best approach to store a unique value and other side time complexity nested loops and mush more taks time
# student=["Mughees","Mohsan","Zafar","Azhar","Ahsan","Ashar","Mohsan","Mughees"]
# login=set()
# signin=set()
# for user in student:
#     if user in signin:
#         login.add(user)
#     else:
#         signin.add(user)
# print(login)
# print(signin)

#Day $ File HAndlinf +Json

# import json

# def save_config(data):
#     with open("config.json","w") as file:
#         json.dump(data,file,indent=4)
# def load_config():
#     try:
#         with open("config.json","r") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}
# def update_config(key,value):
#     data=load_config()
#     print(data)
#     data[key]=value
#     save_config(data)
#     print(f"{key},update!")
# def delete_config(key):
#         data=load_config()
#         if key in data:
#             del data[key]
#             save_config()
#             print(f"{key},deleted!")
#         else:
#                 print("key did not found")
# update_config("dark","Theme")
# update_config("value",18)
# print("current Config",load_config())
# delete_config("volume")
# print("after delete",load_config())


# import json

# def save_config(data):
#     with open("config.json", "w") as file:
#         json.dump(data, file, indent=4)

# def load_config():
#     try:
#         with open("config.json", "r") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}

# def update_config(key, value):
#     data = load_config()
#     data[key] = value
#     save_config(data)
#     print(f"{key} updated!")

# def delete_config(key):
#     data = load_config()
    
#     if key in data:
#         del data[key]
#         save_config(data)
#         print(f"{key} deleted!")
#     else:
#         print("Key not found")

# # -------- TEST --------
# update_config("theme", "dark")
# update_config("volume", 80)

# print("Current Config:", load_config())

# delete_config("volume")

# print("After Delete:", load_config())

#Day 5 Task Exception handeling

# class invalidOperatorError:
#     pass
# while True:
#     try:
#         num1=float(input("Enter a num "))
#         operator=(input("Enter a Operatore (+,-,*,/ )" ))
#         num2=float(input("Enter a num "))
#         if operator=="+":
#             print("Result",num1+num2)
#         elif operator=="-":
#             print("Result",num1-num2)
#         elif operator=="*":
#             print("Result",num1*num2)
#         elif operator=="/":
#             print("Result",num1/num2)
#         else:
#             raise invalidOperatorError ("Operatore not supported")
#     except ValueError:
#         print("Inavlid Error")
#     except ZeroDivisionError:
#         print("Cannot Divide by Zero ")
#     except invalidOperatorError as e:
#         print("X",e)
#     except Exception as e:
#         print("Unexpected Error",e)
    
#     again=input("Continue ? (y/n)")
#     if again.lower() !='y':
#         break
#     print("Debug",num1,operator,num2) 

#practise question OOp Concept

class Student:
    def __init__(self,name,math,phys,ch):
        self.name=name
        self.math=math
        self.phys=phys
        self.ch=ch
        
    def avg_marks(self):
        sum=0
        for val in self.math,self.ch,self.phys:
            sum=sum+val
        print ("Total avg Of  Marks",self.name ,"is",sum/3)
    
s1=Student("Mughees",78,43,65)
s1.avg_marks()

#practise Question 2
class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    def debit(self,amount):
        self.balance-=amount
        print("account Debit",amount)
        print("total balcnce",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("Credit",amount)
        print("total balcnce",self.get_balance())
    def get_balance(self):
        return self.balance

acc1=Account(5000,133)
acc1.debit(200)
print(acc1.balance)
acc1.credit(300)