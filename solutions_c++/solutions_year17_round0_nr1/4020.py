#include <bits/stdc++.h>
#define ll long long int
#define fio ios_base::sync_with_stdio(0);cin.tie(0)
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define slld(t) scanf("%lld",&t)
#define plld(t) printf("%lld\n",t)
#define sc(t) scanf("%c",&t)
#define pb(x) push_back(x)
#define ii pair<int,int>
#define vi vector<int>
#define vvi vector<vi >
#define vii vector<ii >
#define vvii vector<vii >
#define clr(x) memset(x,0,sizeof(x))
#define rep(i,begin,end) for(__typeof(end) i=begin-(begin>end);i!=end-(begin>end);i+=1-2*(begin>end))
#define M_PI 3.14159265358979323846
#define MOD 1000000007
#define INF 101010101
#define MAX 100005
#define EPS 1e-12
using namespace std;

int main()
{
	int t; cin>>t;
	rep(z,1,t+1)
	{
		int k; string s; 
		cin>>s>>k;
		int n = s.length();
		int a[n]; rep(i,0,n) a[i] = (s[i]=='+' ? 0:1);

		int ans = 0;
		int par[n]; clr(par);
		rep(i,0,n)
		{
			if(i + k - 1 >= n) break;
			int yo = a[i]^(par[i]%2);
			rep(j,i,i+k) 
			{
				par[j] += yo;
			}
			ans += yo;
		}

		rep(i,0,n) 
		{
			par[i] %= 2;
			if(a[i]!=par[i]) 
			{
				ans = -1;
				break;
			}
		}
		cout<<"Case #"<<z<<": ";
		if(ans == -1) cout<<"IMPOSSIBLE\n";
		else cout<<ans<<"\n";
	}
	return 0;
}
