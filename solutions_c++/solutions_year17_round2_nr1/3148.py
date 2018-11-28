#include<bits/stdc++.h>
#define rep(x,a,b) for(x=a;x<b;x++)
#define SIZE
typedef long long int ll;
using namespace std;
ll i,j;

int main(){
	ios::sync_with_stdio(false);
	//cin.tie(0);
	ll t;
	cin>>t;
	for(j=1;j<=t;j++){
		ll d,n;
		cin>>d>>n;
		double bottleneck=0;
		for(i=0;i<n;i++){
			ll dist,speed;
			cin>>dist>>speed;
			double currtime=(double)((double)d-(double)dist)/(double)speed;
			if(currtime>bottleneck){
				bottleneck=currtime;
			}
		}
		cout<<"Case #"<<j<<": ";
		cout<<setprecision(6)<<fixed<<(double)(((double)d)/bottleneck)<<endl;
	}
	return 0;
}

