/*
ID: Alaudddin
PROG: 
LANG: C++
*/

#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector>

using namespace std; 

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) fo(i,j,sz(v))
#define Foo(i,j,v) Fo(i,j,sz(v))
#define li(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define CLR(a,v) memset((a),(v),sizeof(a))
#define inf 1000000001
typedef long long Long;
//typedef __int64 Long;
#define pi (2*acos(0))
#define eps 1e-9

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

template<class T>
T gcd(T a,T b) { if(a < b)return gcd(b,a); if(b==0)return a; return gcd(b,a%b); }

vector<bool> vis;
vector<pair<pair<int,int>,int> > v;

pair<int,int> doit()
{
	v.clear();
	pair<pair<int,int>,int> pp;
	int i,j, n = sz(v),mi,ma;
	foo(i,1,vis)if(vis[i] == false)
	{
		Fo(j,0,i)if(vis[j])break; mi = i - j - 1;
		foo(j,i+1,vis)if(vis[j])break; ma = j - i - 1;
		if(mi > ma)swap(mi,ma);
		pp.first.first = -mi; pp.first.second = -ma;
		pp.second = i;
		v.push_back(pp);
	}
	sort(li(v)); if(sz(v) == 0)return make_pair(0,0);
	vis[v[0].second] = true;
	return make_pair(-v[0].first.second,-v[0].first.first);
}

int simulate()
{
	cout << endl;
	int i,n = 4 + 2; vis.clear(); vis.resize(n,false); vis[0] = vis[n-1] = true;
	fo(i,1,n-1)
	{
		pair<int,int> pp = doit();
		cout << "n = " << i << ", " << pp.first << " " << pp.second << endl;
	}
	return 0;
}

map<Long,Long> mp;

void calc()
{
	//simulate(); return;
	mp.clear(); Long n,k,a,b,m; cin >> n >> k; mp[-n]++;
	while(1)
	{
		n = -mp.begin()->first; m = mp.begin()->second; mp.erase(mp.begin());
		if(n == 0){ a = b = 0; break; }
		a = n / 2; b = (n - a - 1); k -= m; if(k <= 0)break;
		mp[-a] += m; mp[-b] += m;
	}
	cout << a << " " << b;
}

int main()
{
	freopen("E://input.txt","r",stdin);
	//freopen("E://output.txt","w",stdout);
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

