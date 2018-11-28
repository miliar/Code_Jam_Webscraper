#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int main(){
  	//freopen("input.txt","r",stdin);
  	//freopen("output.txt","w",stdout);
  	int t;
  	cin>>t;
  	for(int tc = 1; tc<=t;tc++){
  		double ans = 0;
  		ll n,d;
  		cin>>d>>n;
  		for(int i = 0;i<n;i++){
  			ll k,s;
			cin>>k>>s;
			ans = max(ans,(d-k)/(s*1.0));	
		}
		ans = d/ans;
		cout.precision(6);
  		cout<<fixed<<"Case #"<<tc<<": "<<ans<<endl;
	}
	return 0;
}

