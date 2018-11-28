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
	FOR(z,1,t+1)
	{
		long long n,m;
		cin>>n;
		m=n;
		vector<int>v;
		while(n)
		{
			long long r=n%10;
			v.pb(r);
			n=n/10;
		}
		reverse(v.begin(),v.end());
		int pos;
		int flag=0;
		FOR(i,1,v.size())
		{
			if(v[i]<v[i-1])
			{
				flag=1;
				pos=i;
				break;
			}
		}
		cout<<"Case #"<<z<<": ";
		if(flag==0)
			cout<<m<<"\n";
		else
		{
		int x=v[pos-1];
		int f;
		//cout<<x<<" ";
		FOR(i,0,v.size())
		{
			if(v[i]==x)
			{	

				f=i;
				v[i]-=1;
				break;
			}

		}
		FOR(i,f+1,v.size())
		v[i]=9;

		FOR(i,0,v.size())
		{
			if(v[i]!=0)
			cout<<v[i];
		}
		cout<<"\n";
		}

	}
}