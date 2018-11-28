#include<bits/stdc++.h>
#define nl ('\n')
#define pb push_back
#define MOD 1000000007
#define MAX 100000
#define FOR(i,a,b) for(int i=a;i<=b;i++)       //only for a<=b
typedef long long ll;
using namespace std;
//ll expo(ll x,ll y,ll M){ if(y==0) return 1; ll z = expo(x,y/2,M); if(y&1) return (1ll * ((1ll * x * z)%M) * z)%M; else return (1ll * z * z)%M;}
//ll gcd(ll x,ll y){ if(x==0) return y; return gcd(y%x,x); }
int main()
{
	ios::sync_with_stdio(0);cin.tie(0);
	int t;ll n;
	cin>>t;
	FOR(i,1,t)
	{
		cin>>n;ll ans = 0;
		vector<int> arr;
		ll num = n;
		while(num != 0)
		{
			int x = num % 10;
			arr.pb(x);
			num /= 10;
		}
		reverse(arr.begin(),arr.end());int mark = arr.size() - 1;
		int yy = arr.size() - 2;
		FOR(j,0,yy)
		{
			//cout<<"Gaya\n";
			int now = arr[j];
			int nxt = arr[j+1];
			if(nxt < now){
				arr[j] = now - 1;
				mark = j;
				break;
			}
		}
		yy = arr.size() - 1;
		FOR(jj,mark+1,yy)
			arr[jj] = 9;
		for(int jj=mark-1;jj>=0;jj--)
		{
			if(arr[jj] > arr[jj+1]){
				arr[jj] = arr[jj] - 1;
				arr[jj+1] = 9;
			}
		}
		FOR(k,0,yy)
			ans = 1ll*ans*10 + arr[k];
		cout<<"Case #"<<i<<": "<<ans<<nl;
	}
	return 0;
}
