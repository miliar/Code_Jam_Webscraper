def main():
    cases = input()
    for i in range(1, cases+1):
        first_answer = int(raw_input())
        first_set = [str(raw_input()).split(" ") for x in range(0, 4)] 
        
        second_answer = int(raw_input())
        second_set = [str(raw_input()).split(" ") for x in range(0, 4)] 

        intersect = list(set(first_set[first_answer-1]).intersection(second_set[second_answer-1]))

        if not intersect:
            answer = "Volunteer cheated!"
        elif len(intersect) == 1:
            answer = intersect[0]
        else:
            answer = "Bad magician!"
        print("Case #" + str(i) + ": " + answer)
    
    return None

if __name__=="__main__":
    main()
