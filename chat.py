def read_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    c_word_count = 0
    l_word_count = 0
    c_sticker_count = 0
    l_sticker_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == '賴芊宇':
            if s[2] == '[貼圖]':
                c_sticker_count += 1
            else:
                for m in s[2:]:
                    c_word_count += len(m)
        elif name == '李彥澄':
            if s[2] == '[貼圖]':
                l_sticker_count += 1
            else:
                for m in s[2:]:
                    l_word_count += len(m)
    print('賴芊宇說了', c_word_count, '個字', ',傳了', c_sticker_count, '個貼圖')
    print('李彥澄說了', l_word_count, '個字', ',傳了', l_sticker_count, '個貼圖')

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('聊天.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)

main()
