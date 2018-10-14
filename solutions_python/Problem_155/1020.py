__author__ = 'kanhua'



def simulate_ovation(au):

    assert isinstance(au,list)

    total_standed=0
    my_friends=0
    for si, a in enumerate(au):
        if si==0:
            total_standed+=a
        else:
            if total_standed>=si:
                total_standed+=a
            else:
                diff=si-total_standed
                my_friends+=diff
                total_standed+=(a+diff)

    assert sum(au)+my_friends==total_standed

    return my_friends



def unit_test():

    assert simulate_ovation([2])==0
    assert simulate_ovation([0,3,5,8])==1
    assert simulate_ovation([3])==0




def run_contest(input_file="input_test.txt",output_file="test_output.txt"):

    fp=open(input_file,'r')
    op=open(output_file,'w')

    N=int(fp.readline())


    for i in range(N):
        case_str=fp.readline()
        sm,audience=case_str.split()
        sm=int(sm)
        au_ensemble=list()
        for j in range(sm+1):
            au_ensemble.append(int(audience[j]))

        assert len(au_ensemble)==sm+1
        op.write("Case #%s: "%(i+1))
        op.write(str(simulate_ovation(au_ensemble)))
        op.write("\n")


    fp.close()
    op.close()


if __name__=="__main__":
    unit_test()
    run_contest(input_file="A-large.in")