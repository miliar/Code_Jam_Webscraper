#include <iostream>
#include <utility>
using namespace std;

#define llong long long

pair<llong,llong> doit(llong n, llong k) {
	if(k==1) {
		if(n%2==0) return make_pair(n/2,n/2-1);
		else return make_pair(n/2,n/2);
	}
	k--;
	if(n%2==1) {
		if(k%2==0) return doit((n-1)/2,k/2);
		else return doit((n-1)/2,k/2+1);
	} else {
		if(k%2==0) return doit(n/2-1,k/2);
		else return doit(n/2,k/2+1);
	}
}

void solve(int tc) {
	llong n,k;
	cin>>n>>k;
	pair<llong,llong> ret=doit(n,k);
	cout<<"Case #"<<tc<<": "<<ret.first<<' '<<ret.second<<endl;
}

int main() {
	int c;
	cin>>c;
	for(int i=1;i<=c;i++) solve(i);
}
