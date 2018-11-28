#include <bits/stdc++.h>
#define ff first
#define ss second
#define pb push_back
#define MOD (1000000007LL)
#define LEFT(n) (2*(n))
#define RIGHT(n) (2*(n)+1)
 
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
 
ll pwr(ll base, ll p, ll mod = MOD){
ll ans = 1;while(p){if(p&1)ans=(ans*base)%mod;base=(base*base)%mod;p/=2;}return ans;
}
 
ll gcd(ll a, ll b){
    if(b == 0)  return a;
    return gcd(b, a%b);
}

typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector<int> VI;

int t,n,p,m;
int g[105];
int main()
{
	scanf("%d",&t);
	int tt = 1;
	while(t--)
	{
		scanf("%d %d",&n,&p);
		for(int i=0;i<n;i++)
			scanf("%d",&g[i]);
		if(p == 2)
		{
			int cnt = 0;
			for(int i=0;i<n;i++)
				if(g[i]%2 != 0)
					cnt++;
			m = cnt/2;
		}
		else if(p == 3)
		{
			int cnt1 = 0, cnt2 = 0;
			for(int i=0;i<n;i++)
			{
				if(g[i]%3 == 1)
					cnt1++;
				if(g[i]%3 == 2)
					cnt2++;
			}
			m = min(cnt1,cnt2);
			cnt1 = cnt1-m;
			cnt2 = cnt2-m;

			int x = cnt1/3;
			if(cnt1%3 != 0)
				x++;
			m += cnt1-x;

			x = cnt2/3;
			if(cnt2%3 != 0)
				x++;
			m += cnt2-x;
		}

		else if(p == 4)
		{
			int cnt1 = 0, cnt2 = 0, cnt3=0;
			for(int i=0;i<n;i++)
			{
				if(g[i]%4 == 1)
					cnt1++;
				if(g[i]%4 == 2)
					cnt2++;
				if(g[i]%4 == 3)
					cnt3++;
			}
			m = cnt2/2;
			cnt2 = cnt2-m*2;
			int x = min(cnt1,cnt3);
			cnt1 = cnt1-x;
			cnt3 = cnt3-x;
			m += x;

			if(!cnt2)
			{
				int y = cnt1/4;
				if(cnt1%4 != 0)
					y++;
				m += cnt1-y;

				y = cnt3/4;
				if(cnt3%4 != 0)
					y++;
				m += cnt3-y;
			}
			else
			{

				int y = (cnt1+2)/4;
				if((cnt1+2)%4 != 0)
					y++;
				m += cnt1+1-y;

				if(cnt3 >= 2)
				{
					m += 2;
					cnt3 = cnt3 - 2;

					y = cnt3/4;
					if(cnt3%4 != 0)
						y++;
					m += cnt3-y;
				}
				else
				{
					m += cnt3;
				}

				
			}
		}
		printf("Case #%d: %d\n",tt,n-m);
		tt++;

	}
	
	return 0;
}