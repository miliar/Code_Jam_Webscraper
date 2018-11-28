#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

const int N=100;
typedef long long ll;

int main() {
	int ncase, icase, nd, i, j;
	int d[N];
	ll x, ans;
	scanf("%d", &ncase);
	for(icase=1; icase<=ncase; icase++) {
		scanf("%lld", &x);
		nd=0;
		while(x) {
			d[nd++]=x%10;
			x/=10;
		}
		ans=0;
		for(i=nd-1; i>=0; i--) {
			for(j=i-1; j>=0; j--) if(d[j]!=d[i]) break;
			if(j>=0 && d[j]<d[i]) break;
			ans=10*ans+d[i];
		}
		if(i>=0) {
			ans=10*ans+d[i]-1;
			for(i--; i>=0; i--) ans=10*ans+9;
		}
		printf("Case #%d: %lld\n", icase, ans);
	}
	return 0;
}