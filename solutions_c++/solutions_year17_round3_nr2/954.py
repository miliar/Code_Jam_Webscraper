/*input
5
1 1
540 600
840 900
2 0
900 1260
180 540
1 1
1439 1440
0 1
2 2
0 1
1439 1440
1438 1439
1 2
3 4
0 10
1420 1440
90 100
550 600
900 950
100 150
1050 1400
*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define PII pair<ll, ll>
#define f first
#define s second
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define MAXN 100005
#define INF LLONG_MAX
#define mod 1000000007
using namespace std;

ll power(ll x, ll y)
{	ll temp=1;
	while(y>0)
	{
		if(y%2==1)
			temp=(x*temp)%mod;
		x=(x*x)%mod;
		y=y/2;
	}
	return temp;
}

ll t, c1, c2, l, r;
ll arr[2555];
ll rem1, rem2;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>t;
	F(cas,1,t)
	{
		rem1=rem2=720;
		memset(arr,-1,sizeof(arr));
		cin>>c1>>c2;
		F(i,1,c1)
		{
			cin>>l>>r;
			F(j,l,r-1)
				arr[j] = 0;
			rem1 = rem1 - (r-l);
		}
		F(i,1,c2)
		{
			cin>>l>>r;
			F(j,l,r-1)
				arr[j] = 1;
			rem2 = rem2 - (r-l);
		}
		cout<<"Case #"<<cas<<": ";
		if(c1 == 0 && c2 ==0)
		{
			cout<<"2"<<endl;
			continue;
		}
		F(i,0,1439)
		{
			if(arr[i]==-1)
			{
				ll j = i;
				ll cnt = 0;
				while(arr[j]==-1)
				{
					cnt++;
					j = (j+1)%1440;
				}
				ll k = (i-1+1440)%1440;
				while(arr[k]==-1)
				{
					cnt++;
					k = (k-1+1440)%1440;
				}
				if(arr[j] == arr[k])
				{
					if(arr[j]==0)
					{
						if(rem1>=cnt)
						{
							ll j = i;
							while(arr[j]==-1)
							{
								arr[j] = 0;
								j = (j+1)%1440;
							}
							ll k = (i-1+1440)%1440;
							while(arr[k]==-1)
							{
								arr[k] = 0;
								k = (k-1+1440)%1440;
							}
							rem1-=cnt;
						}
					}
					else
					{
						if(rem2>=cnt)
						{
							ll j = i;
							while(arr[j]==-1)
							{
								arr[j] = 1;
								j = (j+1)%1440;
							}
							ll k = (i-1+1440)%1440;
							while(arr[k]==-1)
							{
								arr[k] = 1;
								k = (k-1+1440)%1440;
							}
							rem2-=cnt;
						}
					}
				}
			}
		}
		ll ans = 0;
		F(i,0,1439)
		{
			if(arr[i]==-1)
			{
				ll j = i;
				ll cnt = 0;
				while(arr[j]==-1)
				{
					cnt++;
					j = (j+1)%1440;
				}
				ll k = (i-1+1440)%1440;
				while(arr[k]==-1)
				{
					cnt++;
					k = (k-1+1440)%1440;
				}
				if(arr[j] != arr[k])
				{
					ll org = k;
					k = (k+1)%1440;
					while(k!=j)
					{
						if(arr[org] == 0)
						{
							if(rem1>0)
							{
								arr[k] = 0;
								rem1--;
							}
							else
							{
								arr[k] = 1;
								rem2--;
							}
						}
						else
						{
							if(rem2>0)
							{
								arr[k] = 1;
								rem2--;
							}
							else
							{
								arr[k] = 0;
								rem1--;
							}
						}
						k = (k+1)%1440;
					}
				}
			}
		}
		F(i,0,1439)
		{
			if(arr[i]==-1)
			{
				ll j = i;
				while(arr[j]==-1)
				{
					j = (j+1)%1440;
				}
				ll k = (i-1+1440)%1440;
				while(arr[k]==-1)
				{
					k = (k-1+1440)%1440;
				}
				k = (k+1)%1440;
				while(k!=j)
				{
					if(rem1>0)
					{
						arr[k] = 0;
						rem1--;
					}
					else
					{
						arr[k] = 1;
						rem2--;
					}
					k = (k+1)%1440;
				}
			}
		}
		F(i,0,1439)
		{
			ll j = (i+1)%1440;
			if(arr[i]!=arr[j])
				ans++;
		}
		cout<<ans<<endl;
	}
	return 0;
}