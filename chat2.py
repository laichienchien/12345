lines = []
with open('聊天.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    print(name)
