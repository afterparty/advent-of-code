
with open('input', 'r') as file:
    d = dict()
    items = []
    line = file.readline()
    while(line):
        line = int(line)
        d[line] = 2020 - line
        #store order of lines
        items.append(line)
        #check previous with loop until empty order list
        for i in reversed(items):
            #if line < previous-value
            previous_value = d[i]
            if line < previous_value:
                #value-to-check = previous-value - line
                value_to_check = previous_value - line
                #if value-to-check exists in d
                if value_to_check in d:
                    #multiply value-to-check * previous-value * line
                    result = value_to_check * i * line
                    print(line)
                    print(i)
                    print(value_to_check)
                    print(result)
                    break
        line = file.readline()