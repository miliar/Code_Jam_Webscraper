/*
ID: Tariqul
PROG:
LANG: C++
*/

#include <bits/stdc++.h>

using namespace std;

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) fo(i,j,sz(v))
#define Foo(i,j,v) Fo(i,j,sz(v))
#define li(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define CLR(a,v) memset((a),(v),sizeof(a))

typedef long long Long;
//typedef __int64 Long;
#define pi (2*acos(0))
#define eps 1e-9

const int imax = 1e9+7;
const Long lmax = 1e18;

#define two(X) (1<<(X))
#define twoL(X) (((Long)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)

char BUFFER[100000 + 5];
bool readn(int &n)	{ return scanf("%d",&n) == 1; }
bool readl(Long &n)	{ return scanf("%I64d",&n) == 1; }
bool readd(double &n){ return scanf("%lf",&n) == 1; }
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }

// std::getline(std::cin, name);

template<class T>
T gcd(T a,T b) { if(a < b)swap(a,b); if(b==0)return a; return gcd(b,a%b); }


void checkmax(Long &k1, Long &s1, Long k2, Long s2)
{
	if( k1 * s2 < k2 * s1)
	{
		k1 = k2;
		s1 = s2;
	}
}

void calc()
{
	Long D,N,K,S,maK, maS,i;
	cin >> D >> N >> maK >> maS; maK = D - maK;
	fo(i,1,N)
	{
		cin >> K >> S; K = D - K;
		checkmax(maK, maS, K, S);
	}
	printf("%.6lf", D * maS * 1.0 / maK);
}

int main()
{
    ios_base::sync_with_stdio(0);
	freopen("E://input.txt","r",stdin);
	freopen("E://output.txt","w",stdout);
	int Case,t;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{
		printf("Case #%d: ",Case);
        calc();
		cout << endl;
	}
	return 0;
}

