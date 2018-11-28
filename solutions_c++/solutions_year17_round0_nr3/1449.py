#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	int t,cs = 1;
	cin >> t;
	while(t--){
		ll n,k;
		cin >> n >> k;
		ll temp = 1;
		while(temp-1<k) temp*=2;
		temp/=2;
		ll v = (n-(temp-1))/(temp);
		ll high = (n-(temp-1))%(temp);
		//cout << v << " " << high << " " << temp << endl;
		ll left = k-(temp-1);
		if (left<=high) v++;
		printf("Case #%d: ",cs++);
		if (v%2==0) printf("%lld %lld\n",v/2,v/2-1);
		else printf("%lld %lld\n",v/2,v/2);
	}
	return 0;
}