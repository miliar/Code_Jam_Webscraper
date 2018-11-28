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

int A[30] , szz;
int dp[25][11][2];
int goo( int p , int prev , bool on )
{
        if( p == szz ) {
                return 1;
        }

        int &R = dp[p][prev][on];
        if( R != -1 ) return R;

        R = 0;
        for( int i = prev ; i < 10 && !(on && ( i > A[p] )) ; i ++ ) {
                if( goo( p+1 , i , on&&(i==A[p]) ) ) R = 1;
        }
        return R;
}


void make( char *s )
{
        szz = strlen(s);
        for( int i = 0 ; i < szz ; i ++ ) {
                A[ i ] = s[ i ] - '0';
        }
//        for( int i = 0 ; i < szz ; i ++ ) cout << A[i] <<" "; cout << endl;
}

char s[30];
int slen;
void sol( int p , int prev , bool on )
{
        if( p == szz ) return;
        int i = 9;
        if( on ) i = A[p];
        for( ; i >= prev ; i -- ) {
                if( goo( p+1 , i , on&&(i==A[p]) ) != 0 ) {
                        s[slen++] = i+'0';
                        sol( p+1 , i , on&&(i==A[p]) );
                        return;
                }
        }
}

char temps[30];

void Main()
{
        scanf("%s",temps);
        make( temps );

        myMemset( dp , -1 );
//        cout << goo( 0 , 0 , 1 ) << endl;

        slen = 0;
        sol( 0 , 0 , 1 );
        s[slen] = 0;
        reverse( s , s+slen );
        while( (slen-1) && s[slen-1]=='0' ) slen--;
        reverse( s , s+slen );
        s[slen] = 0;

        printf("Case #%d: %s\n" , Case , s );
}

int main()
{
        freopen( "B-large.in" , "r" , stdin );
        freopen( "B-large.out" , "w" , stdout );
        int test = _Int();
        for( Case = 1 ; Case <= test ; Case ++ )
                Main();
        return 0;
}
