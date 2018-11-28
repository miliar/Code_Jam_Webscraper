#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;cin>>t;
	for(int tt=1;tt<=t;tt++){
		double d;
		ll n; cin>>d>>n;
		double maxT = 0.0;
		for(int i=0;i<n;i++){
			double k,s;
			cin>>k>>s;
			maxT = max(maxT, ((d-k)/s));
		}
		printf("Case #%d: %0.6lf\n",tt,d/maxT);
	}
}
