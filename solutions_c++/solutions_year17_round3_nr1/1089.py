/*input
4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
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
pair < double,double > arr[2005];
multiset < double > myset;
int main() 
{
	std::ios::sync_with_stdio(false);
	//freopen("A-small-attempt0","r",stdin);
	//freopen("o.out","w",stdout);
	ll tc=1;
	ll t;
	cin>>t;
	while(t--)
	{
		myset.clear();
		cout<<"Case #"<<tc++<<": ";
		ll n,k;
		cin>>n>>k;
		F(i,0,n-1)
		{
			double r,h;
			cin>>r>>h;
			arr[i].ff = r;
			arr[i].ss = h;
		}
		sort(arr,arr+n);
		double sum = 0.0;
		F(i,0,k-1)
		{
			double temp = (arr[i].ff)*(arr[i].ss);
			myset.insert(temp);
			sum += temp;
		}
		multiset <double>::iterator it;
		double ans = 2.0*sum + (arr[k-1].ff)*(arr[k-1].ff);
		F(i,k,n-1)
		{
			it = myset.begin();
			sum -= *it;
			sum += ((arr[i].ff)*(arr[i].ss));
			ans = max(ans,(2.0*sum + (arr[i].ff)*(arr[i].ff)) ) ;
			myset.erase(it);
		}
		ans = ans * PI;
		cout<<fixed<<setprecision(12)<<ans<<endl;
	}
	return 0;
}