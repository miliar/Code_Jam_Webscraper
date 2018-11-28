#include <bits/stdc++.h>
//template to keep things straight
 
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define sc(n) scanf("%d",&n)
#define scL(n) scanf("%lld",&n)
 
//#define cinL(n) scanf("%lld",&n)
//#define coutL(n) printf("%lld ",n);
 
#define pr(n) printf("%d\n",n);
#define prL(n) printf("%lld\n",n);
#define newl printf("\n")
//#define mp make_pair
#define pb push_back
#define pf pop_front
#define in insert
#define ll long long 
#define F first
#define S second
//#define MOD 100000000
#define mp make_pair
using namespace std;
#define tv(container, it)  for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define boost  ios::sync_with_stdio(false)//;cin.tie(0)
#define MOD 1000000007

#define BLOCK 448
#define MAX 1000001

int main()
{
	int t;
	cin>>t;
	FOR(x,1,t+1)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int ans=0;
		FOR(i,0,s.length()-k+1)
		{
			if(s[i]=='-')
			{
				ans++;
				FOR(j,i,i+k)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
			}
		}
		int c=0;
		FOR(i,0,s.length())
		{
			if(s[i]=='+')
				c++;
		}
		cout<<"Case #"<<x<<": ";
		if(c==s.length())
			cout<<ans<<"\n";
		else
			cout<<"IMPOSSIBLE"<<"\n";
	}
}