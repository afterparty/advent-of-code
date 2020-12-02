
#with open('test', 'r') as file:
#    data = file.read().splitlines()
#    print(data)

with open('input', 'r') as file:
    d = dict()
    line = file.readline()
    while(line):
        d[int(line)] = int(line)
        lookup_num = 2020 - int(line)
        if lookup_num in d:
            print(int(line) * lookup_num)
        line = file.readline()