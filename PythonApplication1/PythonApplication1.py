
with open('input.txt','r+') as f:
    lines = f.readlines()
# print(lines)

# for line in lines:
#     print(line)

Modify_line = lines[4]
list = Modify_line.split()

print('--I READ THE NUMBER: '+ list[3])

a = int(list[3])

b = 678

list[3] = str(b)

Modify_line = ' '.join(list)+'\n'

lines[4] = Modify_line

with open('input.txt','w') as f:
    f.writelines(lines)

