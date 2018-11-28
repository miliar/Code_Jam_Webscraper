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

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	int N,K;
	int v,ans,i,j,k,v2,d;
	int C[4];
	static int dyn[101][101][101][4];
	Read(T);
		Fox1(t,T)
		{
			Fill(C,0);
			Read(N),Read(K);
				Fox(i,N)
				{
					Read(v);
					C[v%K]++;
				}
			Fill(dyn,-1);
			dyn[C[1]][C[2]][C[3]][0]=0;
				FoxR(i,C[1]+1)
					FoxR(j,C[2]+1)
						FoxR(k,C[3]+1)
							Fox(v,K)
							{
								d=dyn[i][j][k][v];
									if (d<0)
										continue;
								//1
									if (i)
									{
										v2=(v+1)%K;
										Max(dyn[i-1][j][k][v2],d+int(v2==0));
									}
								//2
									if (j)
									{
										v2=(v+2)%K;
										Max(dyn[i][j-1][k][v2],d+int(v2==0));
									}
								//3
									if (k)
									{
										v2=(v+3)%K;
										Max(dyn[i][j][k-1][v2],d+int(v2==0));
									}
							}
			ans=0;
				Fox(i,K)
					Max(ans,dyn[0][0][0][i]-(i?0:1));
			ans+=C[0]+1;
			Min(ans,N);
			printf("Case #%d: %d\n",t,ans);
		}
	return(0);
}