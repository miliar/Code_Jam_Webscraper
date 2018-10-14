def translate(st):
    english =    [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    googlerese = [' ','y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']
    answer = []
    for c in st:
        for i in range(27):
            if c == googlerese[i]:
                answer.append(english[i])
    S = ''.join(answer)
    return S

def run():
    counter = 0
    ins = open( "A-small-attempt2 (1).in", "r" )
    array = []
    for line in ins:
        counter = counter + 1
        if counter > 1:
            array.append( line )
    for l in range (len(array)):
        STR = ("Case #"+(str)(l+1)+": "+ translate(array[l]))
        print STR

run()
