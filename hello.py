def log_analyzer(logs):
    unique_user=set()
    count_action={}
    for log in logs:
        parts=log.split()
        user=parts[1]
        unique_user.add(user)
        if user in count_action:
            count_action[user]=+1
        else:
            count_action[user]=1
    
    top_user=max(count_action,key=count_action.get)
    return unique_user,count_action,top_user
logs=[
    "10:00:1 login:Ahmed",
    "10:05:2 login:Ali",
    "10:10:3 logout:Mughees",
    "10:10:4 update:Mohsan"
]
user,count,top_user=log_analyzer(logs)

print("unique User",user)

print("Action Count",count)
print("Top active User",top_user)

