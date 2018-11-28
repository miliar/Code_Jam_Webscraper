#include <bits/stdc++.h>
using namespace std;
typedef long long int LL;
typedef unsigned long long int uLL;
inline int _Int() { int x; scanf("%d",&x); return x; }
LL bigMod(LL A,LL P,int M){ LL R=1; for(A%=M; P; P>>=1) { if(P&1) R=(R*A)%M; A=(A*A)%M; } return R; } /** (A^P) % M **/
LL bigMul(LL A,LL B,LL M) { LL R=0; for(A%=M; B; B>>=1) { if(B&1) R=(R+A)%M; A=(A+A)%M; } return R; } /** (A*B) % M **/
LL negMod(LL A,LL B) { return ( ( ( A % B ) + B) % B ); } /** (A % B) when A is negative or positive **/
LL invMod(LL A,LL M) { return bigMod( A , M-2, M ); } /** (A^(-1)) % M */
uLL _pow(uLL A,int P) { uLL R=1; for(; P; P>>=1) { if(P&1) R=(R*A); A=(A*A); } return R; } /** (A^P) **/
template<class T>T GCD(T x, T y) { while(x) x^=y^=x^=y%=x; return y; } /** Greatest Common Divisor( a , b ) **/
template<class T> bool inRng( T u, T v, T x ) { return u<=x && x<=v; } /** check ( u <= x <=v ) */
#define myMemset(a,b) memset(a,b,sizeof(a))
#define pi            acos(-1)
#define pb            push_back
#define myDebug(x)    cout<<#x<<" : "<<x<<"\n"
/*************************************************************************************************************************
**                                            Syed Zafrul Lipu (ShockProof)                                              *
**                                            CSE, University of Asia Pacific                                            *
**************************************************************************************************************************/
int Case;

int D;
int n;

struct horse{
        int p;
        double s;
        double time() {
                double d = (D-p);
                return d/s;
        }
}A[ 1000 + 7 ];

void Main()
{
        D = _Int();
        n = _Int();
        double time = 0;
        for( int i = 0 ; i < n ; i ++ ) {
                A[i].p = _Int();
                A[i].s = _Int();
                time = max ( time , A[i].time() );
        }
        double d = D;
        printf( "Case #%d: %0.8f\n" , Case , d/time );
}

int main()
{
        freopen( "A-large.in" , "r" , stdin );
        freopen( "A-large-out.out" , "w" , stdout);
        int test = _Int();
        for( Case = 1 ; Case <= test ; Case ++ )
                Main();
        return 0;
}
