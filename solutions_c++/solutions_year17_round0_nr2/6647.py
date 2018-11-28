#include<bits/stdc++.h>
#define ll long long
#define MOD 1000000007
using namespace std;

ll convert(vector<ll> v, vector<ll> pw){
	ll ret = 0;	
	for(int i=0; i<=19; i++)
	ret += pw[i]*v[i];
	return ret;
}
int main(){
	int t;cin>>t;
	for(int kase = 1; kase <= t; kase++){
		ll n;cin>>n;
		vector<ll> v(19);
		vector<ll> pw(19);
		pw[0] = 1;
		ll temp = n;
		v[0] = temp%10;temp/=10;
		for(int i=1; i<19; i++){
			pw[i] = pw[i-1]*10; 
			v[i] = temp%10;
			temp/=10;
		}
		
		for(int i=18; i>=0; i--){
			vector<ll> v1 = v;
			for(int j=i; j>=0; j--)v1[j] = v[i];
			temp = convert(v1, pw);
			if(temp > n){
				v1[i]--;
				for(int j=i-1; j>=0; j--)v1[j] = 9;
				v = v1;
				break;
			}
		}
		ll ans = convert(v, pw);
		cout<<"Case #"<<kase<<": "<<ans<<endl;

		assert(ans != 0 and ans <= n);
	}
	return 0;
}
