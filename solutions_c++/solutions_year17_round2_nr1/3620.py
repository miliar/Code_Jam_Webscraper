#include<bits/stdc++.h>

#define lld long long int
#define ld long double

using namespace std;

int main()
{
	lld T;
	cin>>T;
	cout<<fixed<<setprecision(6);
	for(int t = 1; t <= T; t++){
		lld D, N;
		ld ans = 10000000000000LL;
		cin>>D>>N;
		// cout<<"##: "<<D<<" "<<N<<endl;
		for(int i = 1; i <= N; i++){
			lld K, S;
			cin>>K>>S;
			// cout<<"##: "<<K<<" "<<S<<endl;
			ld num = D*S;
			ld den = D-K;
			ld tans = num/den;
			if(tans < ans){
				ans = tans;
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}