#include <bits/stdc++.h>
#define fr(x) scanf("%d", &x)
using namespace std;

int k[1024], s[1024];

bool valid(int n, int d, double c){
	// cout<<"T"<<tym<<endl;
	for(int i=1; i<=n; ++i){
		if((((d*1LL*s[i])/c)+k[i]) <= (d)){
			// cout<<(tym*s[i]+k[i])<<" <= "<<(d)<<endl;
			return 0;
		}
	}
	return 1;
}

int main(){
	int t, d, n;
	fr(t);

	for(int t1=1; t1<=t ;++t1){
		fr(d);
		fr(n);

		for(int i=1; i<=n; ++i){
			fr(k[i]);
			fr(s[i]);
		}

		double lo=1, hi=1e16, m;
		for(int i=1;i<=2000;++i){
			m = lo + ((hi-lo)/2);
			if(valid(n, d, m)){
				lo=m;
			}
			else{
				hi=m;
			}
			// cout<<lo<<" "<<hi<<endl;
		}

		printf("Case #%d: %lf\n", t1, lo);

	}
	return 0;
}