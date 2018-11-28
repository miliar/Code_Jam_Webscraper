/*input
*/
#include "bits/stdc++.h"
using namespace std;

#define ll      long long
#define vll     vector< long long >
#define vvll    vector< vll >
#define vd      vector< double > 
#define mp(x,y) make_pair(x,y)
#define ENDL prllf("\n");
#define ldb double
const ll mod = (ll)1e9+7;

#define X first
#define Y second
#define INF (long long)1e18

ll modpow(ll base, ll exp){
	if(exp==0)return (ll)1;
	ll a = modpow(base,exp/2)%mod;
	if(exp%2){
		return ((a*a)%mod)*base%mod;
	}
	return (a*a)%mod;
}

int main(int argc, char const *argv[])
{
	ll T,n;double d;
	cin>>T;
	for (ll cases = 1; cases <= T; ++cases)	{
		cout<<"Case #"<<cases<<": ";
		cin>>d>>n;
		//		cout<<d<<' '<<n<<'\n';
		vector<pair<double,double> >  h(n,mp(0LL,0LL));
		for(ll i=0;i<n;i++){
			cin>>h[i].first>>h[i].second;
			//			cout<<h[i].first<<' '<<h[i].second<<'\n';
		}
		sort(h.begin(), h.end());
		double time = 0;
		for(ll i=n-1;i>=0;i--){
			time = max(time,(d - h[i].first)/(h[i].second));
		}
		cout<<setprecision(7)<<fixed<<(d/time)<<'\n';
	}
}