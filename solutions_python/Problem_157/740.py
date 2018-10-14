__author__ = 'kanhua'
import numpy as np



i_mat=np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,-1],[0,0,1,0]],dtype=np.int16)

j_mat=np.array([[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]],dtype=np.int16)

k_mat=np.array([[0,0,0,1],[0,0,-1,0],[0,1,0,0],[-1,0,0,0]],dtype=np.int16)

I_mat=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],dtype=np.int16)

def display_mat():
    print(i_mat)
    print(j_mat)
    print(k_mat)
    print(I_mat)


mat_map={'i':i_mat,
         'j':j_mat,
         'k':k_mat}


def is_equal(mat1,mat2):

    assert isinstance(mat1,np.ndarray)
    assert isinstance(mat2,np.ndarray)
    assert mat1.ndim==mat2.ndim



    return np.all(mat1==mat2)


def test_operation():

    assert (np.all(np.dot(i_mat,i_mat)==-I_mat))
    assert is_equal(i_mat,i_mat)
    assert is_equal(np.dot(j_mat,i_mat),-k_mat)


def test_iteration(N=10000):

    start=i_mat;


    for i in range(N):
        start=np.dot(start,i_mat)

    return start


def test_mat_match():

    _,r1=mat_match(i_mat,'i',-I_mat)

    assert r1==True

    _,r2=mat_match(k_mat,'j',-i_mat)
    assert r2==True

    _,r3=mat_match(i_mat,'j',k_mat)
    assert r3==True




def mat_match(mat,uchar,mat_to_match):

    assert isinstance(mat,np.ndarray)
    assert isinstance(uchar,str)
    assert isinstance(mat_to_match,np.ndarray)

    uchar_mat=mat_map[uchar]
    next_mat=np.dot(mat,uchar_mat)

    return next_mat, is_equal(next_mat,mat_to_match)

def test_match_ijk():

    print(np.dot(i_mat,k_mat))

    #assert match_ijk("iiiiiiijjjjjjjkkkkkk")



def match_ijk(ijk_str,verbose=False):

    cur_mtx=I_mat
    match=0
    for idx,c in enumerate(ijk_str):
        if verbose==True:
            print("running index:%s"%idx)
        if match==0:
            next_mtx,result=mat_match(cur_mtx,c,i_mat)
            if result==True:
                cur_mtx=I_mat
                match+=1
            else:
                cur_mtx=next_mtx

        elif match==1:
            next_mtx,result=mat_match(cur_mtx,c,j_mat)
            if result==True:
                cur_mtx=I_mat
                match+=1
            else:
                cur_mtx=next_mtx

        elif match==2:
            next_mtx,result=mat_match(cur_mtx,c,k_mat)
            if result==True:
                cur_mtx=next_mtx
                if idx==(len(ijk_str)-1):
                    match+=1
            else:
                cur_mtx=next_mtx


    assert match>=0
    assert match<=3
    if match==3:
        return True
    else:
        return False




def run_contest(input_file="ijk_test.in",output_file="ijk_test.out"):

    fp=open(input_file,'r')
    op=open(output_file,'w')

    N=int(fp.readline())

    for i in range(N):
        print("running case:%s"%i)
        set_str=fp.readline().split()
        set_num=list(map(int,set_str))
        L=set_num[0]
        X=set_num[1]

        ijk_s=fp.readline().rstrip()
        #for c in range(L):
        #    ijk_s+=ijk_s+fp.read(1)

        assert len(ijk_s)==L

        # clean the remaining line that contains '\n'
        #fp.readline()

        ijk_s=ijk_s*X

        op.write("Case #%s: "%(i+1))

        match_result=match_ijk(ijk_s,verbose=False)

        if match_result==True:
            op.write("YES")
        else:
            op.write("NO")

        op.write("\n")


    fp.close()
    op.close()



if __name__=="__main__":
    #display_mat()
    test_operation()
    test_mat_match()
    #print(test_iteration())

    test_match_ijk()
    run_contest(input_file="C-small-attempt3.in")


