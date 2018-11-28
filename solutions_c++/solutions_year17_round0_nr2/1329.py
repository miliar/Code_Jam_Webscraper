#include<iostream>
using namespace std;

int _, T;

long long chk(long long x) {
	long long tmp = x;
	int last = 9;
	while(x) {
		int cur = x%10;
		if(cur > last) return -1LL;
		last = cur;
		x/=10;
	}
	return tmp;
}

void upd(long long &x, long long y) {
	if(x<y) x=y;
}

int main() {
	cin>>_;
	for(int T=1; T<=_; T++) {
		long long x, ans = 0LL;
		cin>>x;
		upd(ans, chk(x));
		for (long long mo=10LL; mo<=x; mo*=10)
			upd(ans, chk(x/mo*mo-1));
		cout<<"Case #" << T << ": "<<ans<<endl;
	}
	
	return 0;
}