/*
            @author man singh
		@mail coder.mansingh@gmail.com
*/
#include <bits/stdc++.h>

using namespace std;

typedef int I;
typedef char C;
typedef long L;
typedef double D;
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef string SS;

typedef pair<I,I> PI;
typedef pair<L,L> PL;
typedef pair<D,D> PD;
typedef pair<L,I> PLI;
typedef pair<LL,LL> PLL;

typedef vector<I> VI;
typedef vector<D> VD;
typedef vector<LL> VLL;
typedef complex<double> CD;

#define F first
#define S second
#define inf 1e16
#define null NULL
#define MP make_pair
#define MT make_tuple
#define PB push_back
#define MAX 2000005
#define MOD 1000000007
#define NL putchar('\n')
#define SZ(x) ((int)(x).size())
#define ABS(x) ((x)>0 ?(x):-(x))
#define ALL(x) x.begin(), x.end()
#define MS0(ar) memset(ar, 0, sizeof(ar))
#define MSP1(ar) memset(ar, 1, sizeof(ar))
#define MSN1(ar) memset(ar, -1, sizeof(ar))
#define REP(i, n) for (int i = 0; i < int(n); ++i)
#define REPE(i, a, b) for (int i = (a); i <= int(b); ++i)

int R(C &x) { return scanf("%c", &x); }
int R(I &x) { return scanf("%d", &x); }
int R(L &x) { return scanf("%ld", &x); }
int R(D &x) { return scanf("%lf", &x); }
int R(LD &x) { return scanf("%Lf", &x); }
int R(LL &x) { return scanf("%lld", &x); }
int R(ULL &x) { return scanf("%llu", &x); }
int R(C *str) { return scanf("%[^\n]s", str); }
void R(SS &str) { getline(cin,str); }

void W(const C &c) { putchar(c); };
void W(const I &x) { printf("%d ", x); }
void W(const L &x) { printf("%ld ", x); }
void W(const D &x) { printf("%lf ", x); }
void W(const LD &x) { printf("%Lf ", x); }
void W(const LL &x) { printf("%lld ", x); }
void W(const ULL &x) { printf("%llu ", x); }
void W(const C str[]) { printf("%s", str); }
void W(const SS &str) { cout<<str; }

LL powmod(LL a,LL b) {LL res=1; a%=MOD; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%MOD;a=a*a%MOD;}return res;}
//--------------------------------------------------------------------------------------------------------------

int main(void)
{
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	I i,t,l,c=0;
	R(t);
	getchar();
	while(c<t)
	{
		SS str;
		R(str);
		l = str.length();
		for(i=0;i<l-1;i++)
        {
            if(str[i] > str[i+1])
            {
                str[i] = str[i]-1;
                while(str[++i])
                {
                    str[i]='9';
                }
            }
        }
        for(i=l-2;i>=0;i--)
        {
            if( str[i] && (str[i] > str[i+1]) )
            {
                str[i]=str[i]-1;
                str[i+1] = '9';
            }
        }
        c++;
        W("Case #"); cout<<c; W(": ");
        i=0;
        while(str[i]=='0' && l!=1)
            i++;
        for(;i<l;i++)
            cout<<str[i];
		//W(str);
		NL;
	}
  return 0;
}
