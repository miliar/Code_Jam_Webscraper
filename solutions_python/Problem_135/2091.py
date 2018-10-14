

def get_values(f,line):
    choices = [];
    for i in range(0,4):
        if i+1 == line:
            choices.extend(f.readline().split())
        else:
            f.readline()
    return choices


if __name__ == "__main__":
    with open('problem.txt','r') as f:
        trials = int(f.readline())
        for i in range(0,trials):
            first = int(f.readline())
            first_choices = get_values(f,first)
            second = int(f.readline())
            second_choices = get_values(f,second)
            
            combined = []
            for a in first_choices:
                if a in second_choices:
                   combined.append(a)

            if len(combined) == 1:
                print "Case #%s: %s"%(i+1,combined[0])
            elif len(combined) > 1:
                print "Case #%s: %s"%(i+1,"Bad magician!")
            else:
                print "Case #%s: %s"%(i+1,"Volunteer cheated!")


