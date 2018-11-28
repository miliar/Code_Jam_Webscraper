#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	ll t,d,n,cc,a,b;
	float temp,ans,x;
	cin>>t;
	for(cc=1;cc<=t;cc++){
		cout<<"Case #"<<cc<<": ";
		cin>>d>>n;
		ans=0;
		while(n--){
			cin>>a>>b;
			temp=(d-a)/(float)b;
			ans=max(ans,temp);
		}
		x=d/ans;
		cout<<setprecision(6)<<fixed<<x<<endl;
	}

	return 0;
}