#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <functional>
#include <utility>
#include <set>
#include <map>
#include <complex>
#include <queue>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string.h>
#include <unordered_set>
#include <unordered_map>
#include <mmintrin.h>
#include <xmmintrin.h>
#include <emmintrin.h>
#include <cassert>

using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned short ushort;
typedef unsigned char uchar;
typedef pair<int, int> ipair;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
#define SIZE(A) ((int)(A.size()))
#define LENGTH(A) ((int)(A.length()))
#define MP(A, B) make_pair(A,B)
const double pi = acos(-1.0);
#define FOR(i, a, b) for(int i=(a);i<(b);++i)
#define REP(i, a) for(int i=0;i<(a);++i)
#define ALL(a) (a).begin(),(a).end()

template<class T>
T sqr(const T& x) { return x * x; }

template<class T>
T lowbit(const T& x) { return (x ^ (x - 1)) & x; }

template<class T>
int countbit(const T& n) { return (n == 0) ? 0 : (1 + countbit(n & (n - 1))); }

template<class T>
void ckmin(T& a, const T& b) { if (b < a) a = b; }

template<class T>
void ckmax(T& a, const T& b) { if (b > a) a = b; }

const int maxsize=3000;
const int dx[]={-1,0,1,0};
const int dy[]={0,-1,0,1};

int size_x,size_y;
char s[maxsize][maxsize];
int n,m;
int wid[maxsize][maxsize];
bool g[maxsize][2];
vector<int> a[maxsize][2];
vector<int> b[maxsize];
bool w[maxsize][maxsize];
int r[maxsize];
int px[maxsize],py[maxsize];

bool ray(int x,int y,char key,vector<int>& p)
{
	set<int> ps;
	REP(direction,4)
	{
		if (key=='|' && direction%2==1) continue;
		if (key=='-' && direction%2==0) continue;
		int x0=x,y0=y,d0=direction;
		while (1)
		{
			x0+=dx[d0];
			y0+=dy[d0];
			if (x0<0 || x0>=size_x || y0<0 || y0>=size_y) break;
			if (s[x0][y0]=='#') break;
			if (s[x0][y0]=='/')
			{
				d0^=3;
				continue;
			}
			if (s[x0][y0]=='\\')
			{
				d0^=1;
				continue;
			}
			if (s[x0][y0]=='.') 
			{
				ps.insert(wid[x0][y0]);
				continue;
			}
			return false;
		}
	}
	p=vector<int>(ALL(ps));
	return true;
}
int ID(int p,int d)
{
	return p*2+d;
}
bool dfs(int p,int d)
{
	if (r[p]>=0) return r[p]==d;
	r[p]=d;
	REP(i,n+n) if (w[ID(p,d)][i] && !dfs(i/2,i%2)) return false;
	return true;
}
bool solve()
{
	m=0;
	memset(wid,255,sizeof(wid));
	REP(x,size_x) REP(y,size_y) if (s[x][y]=='.') wid[x][y]=(m++);
	n=0;
	memset(g,false,sizeof(g));
	REP(x,size_x) REP(y,size_y) if (s[x][y]=='|' || s[x][y]=='-')
	{
		g[n][0]=ray(x,y,'|',a[n][0]);
		g[n][1]=ray(x,y,'-',a[n][1]);
		px[n]=x;
		py[n]=y;
		n++;
	}
	REP(i,n) if (!g[i][0] && !g[i][1]) return false;
	REP(i,m) b[i].clear();
	REP(i,n) REP(d,2) if (g[i][d]) for (int p:a[i][d]) b[p].push_back(ID(i,d));
	memset(w,false,sizeof(w));
	REP(i,n)
	{
		if (!g[i][0]) w[ID(i,0)][ID(i,1)]=true;
		if (!g[i][1]) w[ID(i,1)][ID(i,0)]=true;
	}
	REP(i,m) if (SIZE(b[i])==0) return false;
	REP(i,m) if (SIZE(b[i])==1) 
	{
		int x=b[i][0];
		w[x^1][x]=true;
	}
	REP(i,m) if (SIZE(b[i])==2)
	{
		int x=b[i][0],y=b[i][1];
		w[x^1][y]=true;
		w[y^1][x]=true;
	}
	memset(r,255,sizeof(r));
	REP(i,n)
	{
		int t[maxsize];
		memcpy(t,r,sizeof(t));
		if (dfs(i,0)) continue;
		memcpy(r,t,sizeof(t));
		if (dfs(i,1)) continue;
		return false;
	}
	REP(i,n) s[px[i]][py[i]]=(r[i]==0?'|':'-');
	return true;
}
int main()
{
  //freopen("C.in","r",stdin);
  //freopen("C-small-attempt0.in","r",stdin); //freopen("C-small-attempt0.out","w",stdout);
  //freopen("C-small-attempt1.in","r",stdin); freopen("C-small-attempt1.out","w",stdout);
  //freopen("C-small-attempt2.in","r",stdin); freopen("C-small-attempt2.out","w",stdout);
  freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);

  // std::ios_base::sync_with_stdio(false);
  int ntestcase;
  cin >> ntestcase;
  for (int case_id = 1; case_id <= ntestcase; ++case_id) 
  {
	  cin>>size_x>>size_y;
	  REP(x,size_x) cin>>s[x];
	  printf("Case #%d: ", case_id);    
	  if (solve())
	  {
		  printf("POSSIBLE\n");
		  REP(x,size_x) printf("%s\n",s[x]);
	  }
	  else
		  printf("IMPOSSIBLE\n");
  }

  return 0;
}