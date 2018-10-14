def move_to(current_pos, to_pos, mover, last_moved, last_moved_timer, main_timer):
    current_move_time = abs(current_pos - to_pos) + 1
    
    if mover == last_moved:
        main_timer += current_move_time
        last_moved_timer = current_move_time + last_moved_timer

    else:
        if last_moved_timer >= current_move_time:
            main_timer += 1
            last_moved_timer = 1
        else:
            current_move_time = current_move_time - last_moved_timer
            main_timer += current_move_time
            last_moved_timer = current_move_time
    return (to_pos, mover, last_moved_timer, main_timer)


with open('bots_large.in') as f:
    cases = int(f.readline())
    current_case = 1
    while current_case <= cases:
        click_list = f.readline().split(" ")
        total_clicks = click_list.pop(0)
        o_pos = 1
        b_pos = 1
        o_buttons = []
        b_buttons = []
        move_order = []
        
        for i in range(0, len(click_list)/2):
            i *= 2
            move_order.append(click_list[i])
            if click_list[i] == 'O':
                o_buttons.append(click_list[i+1])
            else:
                b_buttons.append(click_list[i+1])
        
        main_timer = 0
        last_moved_timer = 0
        last_moved = None
        while(len(move_order)):
            mover = move_order.pop(0)
            if mover == 'O':
                to_pos = int(o_buttons.pop(0))
                o_pos, last_moved, last_moved_timer, main_timer = move_to(o_pos, to_pos, mover,
                    last_moved, last_moved_timer, main_timer)
            else:
                to_pos = int(b_buttons.pop(0))
                b_pos, last_moved, last_moved_timer, main_timer = move_to(b_pos, to_pos, mover,
                    last_moved, last_moved_timer, main_timer)
            
            
        print("Case #%d: %d" % (current_case, main_timer))
        current_case += 1
                    
                    

        
    
             
        
        
            
            
            
        
        
        
        