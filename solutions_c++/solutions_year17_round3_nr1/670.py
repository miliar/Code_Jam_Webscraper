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
#define pi (2.0*acos(0.0))
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

struct xx
{
	Long h,r;
};

bool operator<(const xx& n1, const xx &n2)
{
	return (n1.h * n1.r > n2.h * n2.r);
}

vector<xx> v;

void calc()
{
	int i,j,n,k,mai; cin >> n >> k; v.resize(n);
	foo(i,0,v)cin >> v[i].r >> v[i].h;
	sort(li(v)); Long mar = 0,rad;
	double ma = 0,ans ,val = 0;	
	fo(i,0,(k-1))
	{
		val += 2 * pi * (v[i].h * v[i].r);
		if(v[i].r >= mar){ mar = v[i].r; mai = i; }
	}
	fo(i,k-1,n)
	{
		rad = max(mar,v[i].r);
		ans = val + 2 * pi * (v[i].h * v[i].r);
		ans += pi * rad * rad;
		ma = max(ma,ans);
	}
	printf("%.6lf",ma);
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

