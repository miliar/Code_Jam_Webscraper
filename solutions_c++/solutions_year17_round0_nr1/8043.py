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

int main()
{	DRT()
	{	int k; string s;
		printf("Case #%d: ",t1);
		s.clear();
		cin>>s>>k;
		int i=0,n=s.size(),a=0;
		while(i<=n-k)
		{	while(s[i]=='+' && i<=n-k)i++;
//			cerr<<i<<s[i]<<endl;
			if(i<=n-k)
			{	a++;
				f(j,i,i+k)
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
			}
//			cerr<<s<<endl;
			i++;
		}
		bool fl=1;
		f(i,n-k,n)
			if(s[i]=='-')
				fl=0;
		if(fl)
			printf("%d\n",a);
		else
			cout<<"IMPOSSIBLE\n";
	}
}


