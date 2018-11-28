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

const int maxn = 1440;
//const int maxn = 24;
vector<int> v;
int f[maxn][maxn/2+1][3][3][3];
int memo(int cur, int n1,int m,int first,int last)
{	
	int n2 = maxn - cur - n1;
	if(n1 < 0)return imax;
	if(n2 < 0)return imax;
	if(n1 > (maxn/2) || n2 > (maxn/2))return imax;
	if(cur == maxn)
	{
		return first != last;
	}
	if(v[cur] == m)return maxn;
	int &res = f[cur][n1][m][first][last]; if(res != -1)return res;

	int res1 = memo(cur+1,n1 - (m == 0),m,first,m);
	int res2 = memo(cur+1,n1 - (m == 0),1-m,first,m) + 1;
	res = min(res1, res2 );
	return res;
}

void calc()
{
	CLR(f,-1); v.clear(); v.resize(maxn,2);
	int i,j,n,m,a,b; cin >> n >> m;
	fo(i,0,n){ cin >> a >> b; fo(j,a,b)v[j] = 0; }
	fo(i,0,m){ cin >> a >> b; fo(j,a,b)v[j] = 1; }
	cout << min(memo(0,maxn/2,0,0,2),memo(0,maxn/2,1,1,2));
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

