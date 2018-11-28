
def elim_f2(m):
    l,k = m.shape
    for col in range(min(k,l)):
        # print "col: {}".format(col)
        if max(m[:, col]) != True:
            continue

        # swap rows
        chosen_row = col + m[col:, col].argmax()
        switch_with = col
        # print "switch {} {}".format(switch_with, chosen_row)
        m[[switch_with, chosen_row]] = m[[chosen_row, switch_with]]
        # print m

        for row_to_sub_i in [v for v in range(l) if v != switch_with]:
            if m[row_to_sub_i, col] == True:
                # print "sub with {}".format(row_to_sub_i)
                m[row_to_sub_i] ^= m[col]
                # print m

    return m

