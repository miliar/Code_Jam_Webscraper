
    
def get_output(case, string):
    friend = 0
    people = 0
    config = string.split()
    for i in range(int(config[0])):
        people += int (config[1][i])
        if people < i + 1: 
            friend += i + 1 - people
            people += i + 1 - people
    return "Case #%d: %d\n" %(case, friend)
    
    
def main():
    text_file = open("A-small-attempt6.in")
    lines = text_file.readlines()
    text_file.close()
    output = open('output.txt', 'w')
    for i in range(int(lines[0]) + 1)[1::]:
        output.write(get_output(i, lines[i]));
    return

    
if __name__ == "__main__":
    
    main()