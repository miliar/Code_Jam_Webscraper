test= int(input())
n=test
while(test):
    frnd = 0
    count = 0
    array = raw_input().split()
    m_shy = int(array[0])
    shy = array[1]
    
    count1=0
    count+=int(shy[0])
    for i in range(1,m_shy+1):
        if shy[i] == '0':
            continue
        count1 = i - count
        if count1>0:
            count+=count1
            frnd+=count1
            count+=int(shy[i])
        else:
            count+=int(shy[i])
    print 'Case #%d:'%(n-test+1),frnd
    test-=1
