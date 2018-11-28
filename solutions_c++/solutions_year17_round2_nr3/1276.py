#include<bits/stdc++.h>
#define f(i,a,n) for(int i=a;i<n;i++)
#define S second
#define F first
#define Sc(n) scanf("%lld",&n)
#define scc(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define sp(a) scanf("%lld %lld",&a.first,&a.second)
#define pb push_back
#define mp make_pair
#define lb lower_bound
#define ub upper_bound
#define all(a) a.begin(),a.end()
#define sc(n) scanf("%d",&n)
#define It iterator
#define SET(a,b) memset(a,b,sizeof(a))
#define DRT()  int t,t1=0; cin>>t; while(t1++<t)
// inbuilt functions
// __gcd,  __builtin_ffs,     (returns least significant 1-bit, __builtin_ffsll(1)=1)
// __builtin_clz,             (returns number of leading zeroes in 
// __builtin_popcount,
using namespace std;
typedef long long LL;
typedef pair<double,LL> PII;
typedef vector<int> vi;
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define trv(s,it) for(auto it:s)
//#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__) 
template <typename Arg1> void __f(const char* name, Arg1&& arg1)
{	    cerr << name << " : " << arg1 << std::endl; }
template <typename Arg1, typename... Args> void __f(const char* names, Arg1&& arg1, Args&&... args)
{	    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...); }
#else
#define trace(...)
#endif
#define N 105
priority_queue<PII,vector<PII>,greater<PII> > qu;
int E[N],S[N],vis[N],prv[N];
LL dis[N][N];double di[N];


int main()
{	DRT()
	{	printf("Case #%d: ",t1);
		int n,q,u,v;
		cin>>n>>q;
		f(i,1,n+1)
		{	sc(E[i]);	sc(S[i]);}
		f(i,1,n+1)
			f(j,1,n+1)
			{	sc(dis[i][j]);
				if(dis[i][j]==-1)
					dis[i][j]=LLONG_MAX/400;
			}
		f(i,1,n+1)
		{	di[i]=1e18; dis[i][i]=0; }
		f(k,1,n+1)
			f(i,1,n+1)
				f(j,1,n+1)
					dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j]);

		PII tmp;
		f(i,0,q)
		{	while(!qu.empty())qu.pop();
			SET(vis,0);
			f(j,1,n+1)di[i]=1e18;
			cin>>u>>v;
			qu.push(mp(0.0,u));
			while(!qu.empty())
			{	tmp=qu.top();
				qu.pop();
				di[tmp.S]=min(tmp.F,di[tmp.S]);
				trace(tmp.F,di[tmp.S],tmp.S);
				if(tmp.S==v)break;
				vis[tmp.S]=1;
				f(j,1,n+1)
				{	if(!vis[j] && dis[tmp.S][j]<=E[tmp.S])
						qu.push(mp(double(dis[tmp.S][j])/double(S[tmp.S])+tmp.F,j));
					trace(j,dis[tmp.S][j],S[tmp.S],E[tmp.S]);
				}
			}
			printf("%lf ",di[v]);
		}
		cout<<endl;
	}

}


