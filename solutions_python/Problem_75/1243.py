import os

Combine = {}
Oppose = []

Invokes = ''

def ProcessInput( Input ) :

    global Combine
    global Oppose
    global Invokes

    Combine = {}
    Oppose = []
    Invokes = ''

    num = int(Input[0])
    Input = Input[2:]
    for index in range(num) :

        Combine[ (Input[0],Input[1]) ] = Input[2]
        Input = Input[4:]

    
    num = int(Input[0])
    Input = Input[2:]
    for index in range(num) :

        Oppose.append( (Input[0],Input[1]) )
        Input = Input[3:]

    Invokes = Input.split(" ")[1]


def CallInvokes( ) :

    global Combine
    global Oppose
    global Invokes

    Out = [Invokes[0]]
    Invokes = Invokes[1:]
    Invokes = Invokes.rstrip('\n')
    
    for invk in Invokes :

        flag = False
        
        if( len(Out) != 0 ) :
            Test = ( Out[len(Out)-1] , invk )
            TestRev = ( invk , Out[len(Out)-1] )

            if Test in Combine :

                flag = True
                Out.pop( )
                Out.append( Combine[Test] )
                continue

            elif TestRev in Combine :

                flag = True
                Out.pop( )
                Out.append( Combine[TestRev] )
                continue

            else :

                temp = Out
                for ivk in temp :

                    test = ( ivk , invk )
                    testRev = ( invk , ivk )
                    if ( (test in Oppose) or (testRev in Oppose) ) :

                        flag = True
                        Out = []
                        break

        if( flag != True ) : Out.append(invk)

    return Out
        


File = open( "B-small-attempt1.in" , "r" )
N = int( File.readline().rstrip('\n') )

Out = open( "Output.txt" , "w" )

for case in range(N):

    Out.write("Case #"+str(case+1)+": ")

    Input = File.readline()
    ProcessInput( Input )

    Output = CallInvokes( )

    length = len(Output)
    if( length == 0 ) :
        Out.write("[]")

    else :
        Out.write('[')
        count = 1
        for char in Output :

            if( count == length ) :
                Out.write(char)
                break

            Out.write("%s, " % char)
            count += 1

        Out.write(']')
    
    Out.write('\n')

File.close()
Out.close()
