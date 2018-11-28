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
typedef pair<int,int> PII;
typedef vector<int> vi;
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define trv(s,it) for(auto it:s)
#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__) 
template <typename Arg1> void __f(const char* name, Arg1&& arg1)
{	    cerr << name << " : " << arg1 << std::endl; }
template <typename Arg1, typename... Args> void __f(const char* names, Arg1&& arg1, Args&&... args)
{	    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...); }
#else
#define trace(...)
#endif
char ar[30][30];
int main()
{	DRT()
	{	int r,c;
		cin>>r>>c;
		f(i,0,r)
			cin>>ar[i];
		if(t1==91)
			f(i,0,r)
				trace(ar[i]);
		f(i,0,r)
			f(j,0,c)
				if(ar[i][j]!='?')
				{	int k=j-1;
					while(k>=0 && ar[i][k]=='?')k--;
					for(int l=i;l>-1;l--)
					{	if(ar[l][k+1]!='?' && l!=i)break;
						f(m,k+1,j+1)
							ar[l][m]=ar[i][j];
					}		
					
				}
		f(i,0,r)
			f(j,1,c)
				if(ar[i][j]=='?')
					ar[i][j]=ar[i][j-1];
		f(i,1,r)
			f(j,0,c)
				if(ar[i][j]=='?')
					ar[i][j]=ar[i-1][j];
		printf("Case #%d: \n",t1);
		f(i,0,r)
			cout<<ar[i]<<endl;
	}
}


