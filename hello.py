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
num=[1,2,3,4,5,6]
res=list(filter(lambda x:x%2==0,num))
print(res)
#Square The Number
res=list(map(lambda x:x**2,res))
print(res)