# import os
# file_path1 = os.path.join(os.getcwd(), '1.txt')
# file_path2 = os.path.join(os.getcwd(), '2.txt')
# file_path3 = os.path.join(os.getcwd(), 'test.txt')
def open_file(file_name):
    with open(file_name, encoding='utf-8')as f:
        s = f.read()
        return s

def write_file(res_name_file, file_s, file_name):
    with open(res_name_file, 'a') as f:
        f.write(f'{file_name} \n')
        f.write(f'{file_s}\n')

f1 = open_file('1.txt')
f2 = open_file('2.txt')
f3 = open_file('3.txt')


if len(f1) < len(f2) and len(f1) < len(f3):
    write_file('result.txt', f1,'1.txt')
    if len(f2) < len(f3):
        write_file('result.txt', f2, '2.txt')
        write_file('result.txt', f3, '3.txt')
    else:
        write_file('result.txt', f3, '3.txt')
        write_file('result.txt', f2, '2.txt')
elif len(f2) < len(f1) and len(f2) < len(f3):
    write_file('result.txt', f2, '2.txt')
    if len(f1) < len(f3):
        write_file('result.txt', f1, '1.txt')
        write_file('result.txt', f3, '3.txt')
    else:
        write_file('result.txt', f3, '3.txt')
        write_file('result.txt', f1, '1.txt')
else:
    write_file('result.txt', f3, '3.txt')
    if len(f2) < len(f1):
        write_file('result.txt', f2, '2.txt')
        write_file('result.txt', f1, '1.txt')
    else:
        write_file('result.txt', f1, '1.txt')
        write_file('result.txt', f2, '2.txt')



