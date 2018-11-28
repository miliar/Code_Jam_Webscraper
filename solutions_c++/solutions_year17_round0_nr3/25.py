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

int main()
{
		if (DEBUG)
			freopen("in.txt","r",stdin);
	//freopen("C-small-2-attempt0.in","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t;
	LL N,K;
	LL a,b,c;
	priority_queue<pair<LL,LL> > Q;
	Read(T);
		Fox1(t,T)
		{
			scanf("%lld%lld",&N,&K);
				while (!Q.empty())
					Q.pop();
			Q.push(mp(N,1));
				while (K>0)
				{
					N=Q.top().x;
					c=Q.top().y;
					Q.pop();
						while ((!Q.empty()) && (Q.top().x==N))
						{
							c+=Q.top().y;
							Q.pop();
						}
					K-=c;
					a=(N-1)/2;
					b=N-a-1;
						if (a==b)
							Q.push(mp(a,c*2));
						else
						{
							Q.push(mp(a,c));
							Q.push(mp(b,c));
						}
				}
			printf("Case #%d: %lld %lld\n",t,b,a);
		}
	return(0);
}