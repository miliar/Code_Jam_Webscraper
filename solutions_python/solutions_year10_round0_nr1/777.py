
data = open("A-large.in", "r")

output = open("output-large.txt", "w")

def on_or_off(n,k):
    num_bin = bin(k)
    num_bin = str(num_bin)
    num_bin = num_bin[2:]
    line = num_bin[-n:]
    if line.count("1") == n:
        return True
    else:
        return False

def main():
    number_of_elements = data.readline()
    number_of_elements.rstrip('\n')
    number_of_elements=int(number_of_elements)
    i=0
    while i < number_of_elements:
        each = str(data.readline())
        g = each.split()
        result = on_or_off(int(g[0]),int(g[1]))
        if result == True:
            maybe = "ON"
        elif result == False:
            maybe = "OFF"
        else:
            maybe = "SOMETHING WENT WRONG!"
        mystr = "Case #" + str(i+1) + ": " + str(maybe) + "\n"
        output.write(mystr)
        i+=1
    print "DONE"
if __name__ == '__main__':
    main()
    #get = raw_input("Please enter a number: ")
    #get = get.split()
    #print on_or_off(int(get[0]),int(get[1]))
