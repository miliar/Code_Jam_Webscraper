#define DEBUG 1

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define Fox(i,n) for (i=0; i<n; i++)
#define Fox1(i,n) for (i=1; i<=n; i++)
#define FoxI(i,a,b) for (i=a; i<=b; i++)
#define FoxR(i,n) for (i=(n)-1; i>=0; i--)
#define FoxR1(i,n) for (i=n; i>0; i--)
#define FoxRI(i,a,b) for (i=b; i>=a; i--)
#define Foxen(i,s) for (i=s.begin(); i!=s.end(); i++)
#define Min(a,b) a=min(a,b)
#define Max(a,b) a=max(a,b)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second

template<typename T> T Abs(T x) { return(x<0 ? -x : x); }
template<typename T> T Sqr(T x) { return(x*x); }
string plural(string s) { return(Sz(s) && s[Sz(s)-1]=='x' ? s+"en" : s+"s"); }

const int INF = (int)1e9;
const LD EPS = 1e-12;
const LD PI = acos(-1.0);

//#if DEBUG
#define GETCHAR getchar
/*#else
#define GETCHAR getchar_unlocked
#endif*/

bool Read(int &x)
{
	char c,r=0,n=0;
	x=0;
		for(;;)
		{
			c=GETCHAR();
				if ((c<0) && (!r))
					return(0);
				if ((c=='-') && (!r))
					n=1;
				else
				if ((c>='0') && (c<='9'))
					x=x*10+c-'0',r=1;
				else
				if (r)
					break;
		}
		if (n)
			x=-x;
	return(1);
}

struct TwoSat {
	int n;
	vector<vector<int> > adj, radj, scc;
	vector<int> sid, vis, val;
	stack<int> stk;
	int scnt;
	
	// n: number of variables, including negations
	TwoSat(int n): n(n), adj(n), radj(n), sid(n), vis(n), val(n, -1) {}

	// adds an implication
	void impl(int x, int y) { adj[x].push_back(y); radj[y].push_back(x); }
	// adds a disjunction
	void vee(int x, int y) { impl(x^1, y); impl(y^1, x); }
	// forces variables to be equal
	void eq(int x, int y) { impl(x, y); impl(y, x); impl(x^1, y^1); impl(y^1, x^1); }
	// forces variable to be true
	void tru(int x) { impl(x^1, x); }
	
	void dfs1(int x) {
		if (vis[x]++) return;
		for (int i = 0; i < adj[x].size(); i++) {
			dfs1(adj[x][i]);
		}
		stk.push(x);
	}
	
	void dfs2(int x) {
		if (!vis[x]) return; vis[x] = 0;
		sid[x] = scnt; scc.back().push_back(x);
		for (int i = 0; i < radj[x].size(); i++) {
			dfs2(radj[x][i]);
		}
	}

	// returns true if satisfiable, false otherwise
	// on completion, val[x] is the assigned value of variable x
	// note, val[x] = 0 implies val[x^1] = 1
	bool two_sat() {
		scnt = 0;
		for (int i = 0; i < n; i++) {
			dfs1(i);
		}
		while (!stk.empty()) {
			int v = stk.top(); stk.pop();
			if (vis[v]) {
				scc.push_back(vector<int>());
				dfs2(v);
				scnt++;
			}
		}
		for (int i = 0; i < n; i += 2) {
			if (sid[i] == sid[i+1]) return false;
		}
		vector<int> must(scnt);
		for (int i = 0; i < scnt; i++) {
			for (int j = 0; j < scc[i].size(); j++) {
				val[scc[i][j]] = must[i];
				must[sid[scc[i][j]^1]] = !must[i];
			}
		}
		return true;
	}
};

int N,M,K;
bool hit;
char G[51][51];
vector<int> vis[51][51];
int my[4]={-1,0,1,0};
int mx[4]={0,1,0,-1};

bool Sim(int i,int j,int d,int v)
{
	i+=my[d];
	j+=mx[d];
		if ((i<0) || (i>=N) || (j<0) || (j>=M))
			return(0);
		if (G[i][j]=='#')
			return(0);
		if (G[i][j]=='-')
			return(1);
		if (G[i][j]=='.')
			if (v>=0)
				vis[i][j].pb(v);
		if (G[i][j]=='/')
		{
			if (d==0)
				d=1;
			else
			if (d==1)
				d=0;
			else
			if (d==2)
				d=3;
			else
				d=2;
		}
		else
		if (G[i][j]=='\\')
		{
			if (d==0)
				d=3;
			else
			if (d==1)
				d=2;
			else
			if (d==2)
				d=1;
			else
				d=0;
		}
	return(Sim(i,j,d,v));
}

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	//freopen("C-small-attempt0.in","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int i,j,k,a,b;
	int ind[51][51];
	Read(T);
		Fox1(t,T)
		{
			printf("Case #%d: ",t);
			Read(N),Read(M);
				Fox(i,N)
					Fox(j,M)
						vis[i][j].clear();
			K=0;
			Fill(ind,-1);
				Fox(i,N)
				{
					scanf("%s",&G[i]);
						Fox(j,M)
							if ((G[i][j]=='-') || (G[i][j]=='|'))
							{
								G[i][j]='-';
								ind[i][j]=K++;
							}
				}
			TwoSat S(K*2);
				Fox(i,N)
					Fox(j,M)
						if (ind[i][j]>=0)
						{
							k=ind[i][j];
							bool canV=!Sim(i,j,0,-1) && !Sim(i,j,2,-1);
							bool canH=!Sim(i,j,1,-1) && !Sim(i,j,3,-1);
								if (!canV && !canH)
									goto Imp;
								if (!canH)
									S.tru(k*2);
								if (!canV)
									S.tru(k*2+1);
								if (canV)
								{
									Sim(i,j,0,k*2);
									Sim(i,j,2,k*2);
								}
								if (canH)
								{
									Sim(i,j,1,k*2+1);
									Sim(i,j,3,k*2+1);
								}
						}
				Fox(i,N)
					Fox(j,M)
						if (G[i][j]=='.')
						{
							if (!Sz(vis[i][j]))
								goto Imp;
							if (Sz(vis[i][j])==1)
								S.tru(vis[i][j][0]);
							else
							{
								a=vis[i][j][0];
								b=vis[i][j][1];
								S.vee(a,b);
							}
						}
				if (!S.two_sat())
				{
Imp:;
					printf("IMPOSSIBLE\n");
					continue;
				}
			printf("POSSIBLE\n");
				Fox(i,N)
					Fox(j,M)
					{
						k=ind[i][j];
							if (k>=0)
								if (S.val[k*2])
									G[i][j]='|';
								else
									G[i][j]='-';
					}
				Fox(i,N)
					printf("%s\n",G[i]);
		}
	return(0);
}