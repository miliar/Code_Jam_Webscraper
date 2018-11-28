#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>

using namespace std;

typedef unsigned long long uint64;
typedef unsigned int uint32;
typedef long double ldo;
typedef uint64 uint;
typedef vector<string> vstring;
typedef vector<uint> vuint;
typedef map<uint, ldo> horses;


#define UINTMAX 0xffffffff
#define UINV UINTMAX
#define INTMAX 0xffff
#define INV INTMAX

#define F(I,INIT,COMP) for(I=INIT; I<COMP; ++I)
#define FU(I,INIT,COMP,ICR) for(I=INIT; I<COMP; I+=ICR)
#define FUINC(I,INIT,COMP,ICR) for(I=INIT; I<=COMP; I+=ICR)
#define FD(I,INIT,COMP,ICR) for(I=INIT; I>COMP; I-=ICR)
#define FDINC(I,INIT,COMP,ICR) for(I=INIT; I>=COMP; I-=ICR)
#define IFEQSET(A,COND,VAL) if((A)==(COND)) {(A) = (VAL);}
#define IFNEQSET(A,COND,VAL) if((A)!=(COND)) {(A) = (VAL);}
#define IFLTSET(A,COND,VAL) if((A)<(COND)) {(A) = (VAL);}
#define IFLTEQSET(A,COND,VAL) if((A)<=(COND)) {(A) = (VAL);}
#define IFGTSET(A,COND,VAL) if((A)>(COND)) {(A) = (VAL);}
#define IFGTEQSET(A,COND,VAL) if((A)>=(COND)) {(A) = (VAL);}
#define REPL(A,START,LAST,VAL) {uint iii; FUINC(iii,START,LAST,1) A[iii] = (VAL);}

#define SZ(A) (A.size())

template<class T>
print_result(uint n, T res)
{
	int i,j,k;
	cout.precision(6);
    cout << "Case #" << n << ": " << fixed << res << endl;;
}

int main()
{
	uint T;
	uint D,N;
	uint n,i,j,k,p,q,r,s;

	
	cin >> T;
	
	FUINC(n,1,T,1)
	{
	    uint h;
	    ldo s;
        cin >> D >> N;
        ldo max;
        bool flag=false;
        
        F(i,0,N)
        {
            cin >> h >> s;
            ldo tm = ((ldo)D-h)/s;
            if (!flag)
            {
               max = tm ;
               flag = true;
            }
            else if (tm > max)
                max = tm;
        }    
   
		print_result(n, D/max);		
	}
	return 0;
}

