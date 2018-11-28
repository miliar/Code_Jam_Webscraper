/*input
4
4 4
1.4000
0.5000 0.7000 0.8000 0.6000
2 2
1.0000
0.0000 0.0000
2 1
0.0000
0.9000 0.8000
2 1
0.1000
0.4000 0.5000
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

ll t;
ll n, k;
double arr[55], rem;

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>t;
	F(cas,1,t)
	{
		cin>>n>>k;
		cin>>rem;
		F(i,1,n)
			cin>>arr[i];
		arr[n+1] = 1;
		sort(arr+1,arr+2+n);
		double cur = 1;
		F(i,2,n+1)
		{
			double tmp = arr[i]-arr[i-1];
			tmp = tmp*cur;
			if(tmp<=rem)
			{
				F(j,1,i-1)
					arr[j] = arr[i];
				rem -= tmp;
				cur = cur + 1;
			}
			else
			{
				tmp = rem/cur;
				F(j,1,i-1)
					arr[j] = arr[j] + tmp;
				break;				
			}
		}
		double ans = 1;
		F(i,1,n)
			ans = ans*arr[i];
		cout<<"Case #"<<cas<<": ";
		printf("%.11f\n",ans);
	}    
	return 0;
}