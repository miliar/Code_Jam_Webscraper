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

const int INF = (int)1e9;
const LD EPS = 1e-9;
const LD PI = acos(-1.0);

bool Read(int &x)
{
	char c,r=0,n=0;
	x=0;
		for(;;)
		{
			c=getchar();
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

typedef vector<int> VI;
typedef vector<VI> VVI;

struct MaxFlow {
  int N;
  VVI cap, flow;
  VI dad, Q;

  MaxFlow(int N) :
    N(N), cap(N, VI(N)), flow(N, VI(N)), dad(N), Q(N) {}

  void AddEdge(int from, int to, int cap) {
    this->cap[from][to] += cap;
  }

  int BlockingFlow(int s, int t) {
    fill(dad.begin(), dad.end(), -1);
    dad[s] = -2;

    int head = 0, tail = 0;
    Q[tail++] = s;
    while (head < tail) {
      int x = Q[head++];
      for (int i = 0; i < N; i++) {
        if (dad[i] == -1 && cap[x][i] - flow[x][i] > 0) {
          dad[i] = x;
          Q[tail++] = i;
        }
      }
    }

    if (dad[t] == -1) return 0;

    int totflow = 0;
    for (int i = 0; i < N; i++) {
      if (dad[i] == -1) continue;
      int amt = cap[i][t] - flow[i][t];
      for (int j = i; amt && j != s; j = dad[j])
        amt = min(amt, cap[dad[j]][j] - flow[dad[j]][j]);
      if (amt == 0) continue;
      flow[i][t] += amt;
      flow[t][i] -= amt;
      for (int j = i; j != s; j = dad[j]) {
        flow[dad[j]][j] += amt;
        flow[j][dad[j]] -= amt;
      }
      totflow += amt;
    }

    return totflow;
  }

  int GetMaxFlow(int source, int sink) {
    int totflow = 0;
    while (int flow = BlockingFlow(source, sink))
      totflow += flow;
    return totflow;
  }
};

int N;

int D1(int i,int j)
{
	return(i+j);
}

int D2(int i,int j)
{
	return(i-j+N);
}

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	//freopen("D-small-attempt0.in","r",stdin);
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int M,V;
	int i,j,d,init,ans1,ans2,a1,a2,d1,d2;
	char c;
	bool inv1[808],inv2[808];
	static char orig[100][100];
	vector<char> lstC;
	vector<int> lstY,lstX;
	Read(T);
		Fox1(t,T)
		{
			Read(N),Read(M);
			V=N*4+2;
			MaxFlow G1(V),G2(V);
				Fox(i,N)
					Fox(j,N)
					{
						G1.AddEdge(i,N*2+j,1);
						d1=D1(i,j);
						d2=D2(i,j);
						G2.AddEdge(d1,N*2+d2,1);
					}
			Fill(inv1,0);
			Fill(inv2,0);
			Fill(orig,0);
			init=0;
				while (M--)
				{
					scanf("%c",&c);
					Read(i),Read(j),i--,j--;
					orig[i][j]=c;
						if (c!='+')
						{
							init++;
							inv1[i]=1;
							inv1[N*2+j]=1;
						}
						if (c!='x')
						{
							init++;
							d1=D1(i,j);
							d2=D2(i,j);
							inv2[d1]=1;
							inv2[N*2+d2]=1;
						}
				}
				Fox(i,N*2)
				{
					if (!inv1[i])
						G1.AddEdge(V-2,i,1);
					if (!inv1[N*2+i])
						G1.AddEdge(N*2+i,V-1,1);
					if (!inv2[i])
						G2.AddEdge(V-2,i,1);
					if (!inv2[N*2+i])
						G2.AddEdge(N*2+i,V-1,1);
				}
			ans1=G1.GetMaxFlow(V-2,V-1);
			ans2=G2.GetMaxFlow(V-2,V-1);
			lstC.clear();
			lstY.clear();
			lstX.clear();
				Fox(i,N)
					Fox(j,N)
					{
						a1=a2=0;
							if ((orig[i][j]=='x') || (orig[i][j]=='o'))
								a1=1;
							else
							if (G1.flow[i][N*2+j]>0)
								a1=1;
						d1=D1(i,j);
						d2=D2(i,j);
							if ((orig[i][j]=='+') || (orig[i][j]=='o'))
								a2=1;
							else
							if (G2.flow[d1][N*2+d2]>0)
								a2=1;
						if (a1+a2)
						{
								if (!a1)
									c='+';
								else
								if (!a2)
									c='x';
								else
									c='o';
								if (c!=orig[i][j])
								{
									lstC.pb(c);
									lstY.pb(i+1);
									lstX.pb(j+1);
								}
						}
					}
			printf("Case #%d: %d %d\n",t,init+ans1+ans2,Sz(lstC));
				Fox(i,Sz(lstC))
					printf("%c %d %d\n",lstC[i],lstY[i],lstX[i]);
		}
	return(0);
}