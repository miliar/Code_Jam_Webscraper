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

vector<string> s;
bool vis[150];

bool good(int i1, int j1, int i2, int j2)
{
    int i,j; if(i1 < 0 || j1 < 0 || i2 >= sz(s) || j2 >= sz(s[0]))return false;
    fo(i,i1,i2+1)fo(j,j1,j2+1)if(s[i][j] != '?')return false;
    return true;
}

bool TrySet(int i1, int j1, int i2, int j2, char ch)
{
    if(!good(i1,j1,i2,j2))return false;
    int i,j;
    fo(i,i1,i2+1)fo(j,j1,j2+1)s[i][j] = ch;
    return true;
}

void update(int i1, int j1, int i2, int j2)
{
    while(1){ if(!TrySet(i1,j2+1,i2,j2+1,s[i1][j1]))break; j2++; }
    while(1){ if(!TrySet(i1,j1-1,i2,j1-1,s[i1][j1]))break; j1--; }
    while(1){ if(!TrySet(i2+1,j1,i2+1,j2,s[i1][j1]))break; i2++; }
    while(1){ if(!TrySet(i1-1,j1,i1-1,j2,s[i1][j1]))break; i1--; }
}

void calc()
{
	CLR(vis,false);
    int i,j,n,m; cin >> n >> m; s.resize(n);
    foo(i,0,s)cin >> s[i];
    foo(i,0,s)foo(j,0,s[i])if(s[i][j] != '?' && vis[s[i][j]] == false)
	{
		update(i,j,i,j); vis[s[i][j]] = true;
	}
    foo(i,0,s)cout << s[i] << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
	freopen("E://input.txt","r",stdin);
	//freopen("E://output.txt","w",stdout);
	int Case,t;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{
		printf("Case #%d:\n",Case);
        calc();
		//cout << endl;
	}
	return 0;
}

