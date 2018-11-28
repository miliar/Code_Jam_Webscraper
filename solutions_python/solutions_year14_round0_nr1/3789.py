def magic_trick():
    f = open("A-small-attempt2.in", "r")
    o = open("A-small-attempt2.out", "w")
    
    case_num = int(f.readline())
    case_counter = 1
    
    while case_counter <= case_num:
        # First Question.
        ans = int(f.readline())
        cards = []
        # Get the card arrangement info.
        cards.append(f.readline().strip().split(" "))
        cards.append(f.readline().strip().split(" "))
        cards.append(f.readline().strip().split(" "))
        cards.append(f.readline().strip().split(" "))
        # Get the selected row.
        selected_row_first = cards[ans - 1]
        
        # Second Question.
        ans = int(f.readline())
        cards = []
        cards.append(f.readline().strip().split(" "))
        cards.append(f.readline().strip().split(" "))
        cards.append(f.readline().strip().split(" "))
        cards.append(f.readline().strip().split(" "))    
        selected_row_second = cards[ans - 1]
        
        # Guess which cards volunteer selected.
        possibility_selected = []
        for i in selected_row_first:
            for j in selected_row_second:
                if i == j:
                    possibility_selected.append(i)
        
        # Case where there are one possibility (Correct one.)
        if len(possibility_selected) == 1:
            o.write("Case #" + str(case_counter) + ": " + possibility_selected[0])
        elif len(possibility_selected) > 1:
            # Case where there are multiple possibilities.
            o.write("Case #" + str(case_counter) + ": Bad magician!")
        else:
            # Case where volunteer provided false information.
            o.write("Case #" + str(case_counter) + ": Volunteer cheated!")
        
        if case_counter < case_num:
            o.write("\n")
            
        case_counter += 1
        
    f.close()
    o.close()

if __name__ == "__main__":
    magic_trick()