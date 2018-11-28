/*input
2
4 4
1.4000
0.5000 0.7000 0.8000 0.6000
2 2
1.0000
0.0000 0.0000
*/
#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define F(i,a,b) for(ll i = a; i <= b; i++)
#define RF(i,a,b) for(ll i = a; i >= b; i--)
#define pii pair<ll,ll>
#define PI 3.14159265358979323846264338327950288
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define debug(x) cout << #x << " = " << x << endl
#define INF 1000000009
#define mod 1000000007
#define S(x) scanf("%d",&x)
#define S2(x,y) scanf("%d%d",&x,&y)
#define P(x) printf("%d\n",x)
#define all(v) v.begin(),v.end()
ll BIT[200005];
void update(ll id,ll val) {
	for(ll i=id;i<=200000;i+=i&-i) BIT[i]+=val;
}
ll query(ll id) {
	ll sum=0;
	for(ll i=id;i>0;i-=i&-i) sum+=BIT[i];
	return sum;
}
double arr[100];
int main() 
{
	std::ios::sync_with_stdio(false);
	freopen("C-small-1-attempt1.in","r",stdin);
	freopen("output.out","w",stdout);
	ll tc=1;
	ll t;
	cin>>t;
	while(t--)
	{
		cout<<"Case #"<<tc++<<": ";
		ll n,k;
		cin>>n>>k;
		double units;
		cin>>units;
		F(i,0,n-1)
			cin>>arr[i];
		sort(arr,arr+n);
		F(i,0,n-2)
		{
			double req = arr[i+1] - arr[i];
			double prev = i+1;
			double req1 = req * prev;
			if(req1 <= units)
			{
				F(j,0,i)
					arr[j] = arr[i+1];
				units = units - req1;
			}
			else
			{
				double eq = units/prev;
				F(j,0,i)
					arr[j] += eq;
				units = 0.0;
			}
		}
		if(units > 0.0)
		{
			double eq = units/(double)n;
			F(i,0,n-1)
			{
				arr[i] += eq;
				if(arr[i] > 1.0)
					arr[i] = 1.0;
			}
		}
		double ans = arr[0];
		F(i,1,n-1)
			ans = ans * arr[i];
		cout<<fixed<<setprecision(12)<<ans<<endl;
	}
	return 0;
}