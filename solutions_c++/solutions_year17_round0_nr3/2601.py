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

void Main()
{
        uLL n , k , x , d , one=1 , step , y , z;

        scanf("%llu %llu",&n,&k);

        d = 0;
        for( step = 0 ; ; step ++ ) {
                x = (d|(one<<step));
                if( x < k ) {
                        d = x;
                        n -= (one<<step);
                }
                else {
                        break;
                }
        }
        k = (k-d-1);

        uLL final_layer = d+1;
        d = n/final_layer;
        y = n%final_layer;


        if( k >= y ) n = d;
        else n = d+1;
        x = ((n>>one)+(n&one));

        printf("Case #%d: %llu %llu\n" , Case , n-x , x-1 );
}

int main()
{
        freopen("C-large.in" , "r" , stdin );
        freopen("C-large.out" , "w" , stdout );
        int test = _Int();
        for( Case = 1 ; Case <= test ; Case ++ )
                Main();
        return 0;
}
