#include<bits/stdc++.h>
# define ll long long
# define ld long double 
using namespace std;
int main(){
	ios_base::sync_with_stdio();
	cin.tie(0);
	cout.tie(0);
	ll t,i;
	cin>>t;
	for(i=1;i<=t;i++){
		ld d;
		ll n;
		cin>>d>>n;
		ld time=INT_MIN;
		for(ll j=0;j<n;j++){
			ld cp,s;
			cin>>cp>>s;
			ld te;
			te=(d-cp)/s;
			if(te>time)
				time=te;

		}
		ld s;
		s=d/time;
		cout<<"Case #"<<i<<": ";
		cout<<setprecision(6);
		cout<<fixed;
		cout<<s<<endl;
	}
return 0;
}