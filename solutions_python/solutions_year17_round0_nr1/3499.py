counter = 0
o = []
with open('a_small.txt', 'r') as f:
    for data in f:
        data = data.strip()
        #print('Data = {}'.format(data))
        if counter == 0:
            T = int(data)
            counter += 1
        else:
            arr = data.split(' ')
            K =int(arr[1])
            data = arr[0].rstrip()
            #print('{}a{}a'.format(K, data))
            l = len(data)
            flip = 0
            prev = ''
            for i in range(l):
                if i <= l - K:
                    prev = data[i]
                    if prev == '-':
                        flip += 1
                        flip_data = []
                        for j in range(K):
                            j_at = j + i
                            if data[j_at] == '+':
                                flip_data.append('-')
                            else:
                                flip_data.append('+')
                            
                        new_data = str(''.join(data[:i])) + str(''.join(flip_data[:])) + str(''.join(data[i+K:]))
                        #print('Before {} = {}'.format(flip_data, data))
                        data = new_data
                        #print('After = {}'.format(data))
                        prev = data[i]
                else:
                    if data[i] != prev:
                        o.append('IMPOSSIBLE')
                        #print('IMPOSSIBle')
                        break
                    if i == l - 1:
                        o.append(flip)
                        #print(flip)
    
                
with open('a_out.txt', 'w') as f:
    for idx, val in enumerate(o):
        f.write('Case #{}: {}\n'.format(idx + 1, val))

