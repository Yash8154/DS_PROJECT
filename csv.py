users={}
with open('passwd.txt') as f:
    for line in f:
        if not line.startswith("#") and line.strip():
            user_info=line.split(":")
            users[user_info[0]] = user_info[7]
for username,user_id in sorted(users.items()):
    print(f"{username}:{user_id}")