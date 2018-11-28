/*input
4
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2
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
	ll T,n,r,o,y,g,b,v;
	cin>>T;
	for (ll cases = 1; cases <= T; ++cases)	{
		cout<<"Case #"<<cases<<": ";
		cin>>n>>r>>o>>y>>g>>b>>v;
		bool imp= 0;
		pair<ll,char> mane[3]={mp(r,'R'),mp(y,'Y'),mp(b,'B')};
		sort(mane,mane+3);
		string ans(n,'_');
		if(mane[0].X==0){
			if(n%2 || mane[1].X!=mane[2].X ){
				cout<<"IMPOSSIBLE\n";
				continue;
			}else{
				for(ll i=0;i<n;i++){	ans[i]=mane[1+i%2].Y;			}
				cout<<ans<<'\n';
				continue;
			}
		}
		ll diff = mane[2].X-mane[1].X;
		ll i=0;
		if(diff>mane[0].X){
			cout<<"IMPOSSIBLE\n";continue;
		}
		while(mane[0].X - diff){
			ans[i] = mane[i%3].Y;
			mane[i%3].X--;
			i++;
			ans[i] = mane[i%3].Y;
			mane[i%3].X--;
			i++;
			ans[i] = mane[i%3].Y;
			mane[i%3].X--;
			i++;
		}
		//			cout<<ans<<' ';
		ll j=0;
		while(mane[0].X){
			ans[i+j]=mane[0].Y;mane[0].X--; j++;
			ans[i+j]=mane[2].Y;mane[2].X--; j++;
			ans[i+j]=mane[1].Y;mane[1].X--; j++;
			ans[i+j]=mane[2].Y;mane[2].X--; j++;
		}
		// 		cout<<ans<<'\n';
		if(ans[i+j-1]==mane[1+(i+j)%2].Y){
			for(ll k=0;(i+j+k)<n;k++){	ans[i+j+k]=mane[2 - (i+j+k)%2].Y;			}	
		}else{
			for(ll k=0;(i+j+k)<n;k++){	ans[i+j+k]=mane[1+(i+j+k)%2].Y;			}	
		}
		
		cout<<ans<<'\n';
		

	}
	return 0;
}