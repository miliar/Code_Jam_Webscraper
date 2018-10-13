__author__ = 'kanhua'



result_table={
    (1,1,1):'G',
    (2,1,1):'R',
    (3,1,1):'R',
    (4,1,1):'R',

    (1,1,2):'G',
    (2,1,2):'G',
    (3,1,2):'R',
    (4,1,2):'R',

    (1,1,3):'G',
    (2,1,3):'R',
    (3,1,3):'R',
    (4,1,3):'R',

    (1,1,4):'G',
    (2,1,4):'G',
    (3,1,4):'R',
    (4,1,4):'R',

    (1,2,2):'G',
    (2,2,2):'G',
    (3,2,2):'R',
    (4,2,2):'R',

    (1,2,3):'G',
    (2,2,3):'G',
    (3,2,3):'G',
    (4,2,3):'R',

    (1,2,4):'G',
    (2,2,4):'G',
    (3,2,4):'R',
    (4,2,4):'R',

    (1,3,3):'G',
    (2,3,3):'R',
    (3,3,3):'G',
    (4,3,3):'R',

    (1,3,4):'G',
    (2,3,4):'G',
    (3,3,4):'G',
    (4,3,4):'G',

    (1,4,4):'G',
    (2,4,4):'G',
    (3,4,4):'R',
    (4,4,4):'G'

}

assert len(result_table)==40


def look_up(game):

    key=(game[0],min(game[1:]),max(game[1:]))

    if (result_table[key])=='G':
        return 'GABRIEL'
    elif result_table[key]=='R':
        return 'RICHARD'



def run_contest(in_file="test.in",out_file="test2.out"):

    fp=open(in_file,'r')
    op=open(out_file,'w')
    N=int(fp.readline())

    for i in range(N):

        game=list(map(int,(fp.readline().split())))

        result=look_up(game)

        op.write("Case #%s: "%(i+1))
        op.write(result)
        op.write("\n")

    fp.close()
    op.close()


if __name__=="__main__":

    run_contest(in_file="D-small-attempt0.in")