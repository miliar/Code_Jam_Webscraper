#include <iostream>
#include <cstdio>

using namespace std;

int testcase = 0;

void solve(){
	testcase++;
	double D,N,K,S,max_slow = 0;
	cin>>D>>N;
	for(int i = 0; i<N; i++){
		cin>>K>>S;
		max_slow = max(max_slow,(D-K)/S);
	}
	printf("Case #%d: %.6f\n",testcase,D/max_slow);
}

int main(){
	int t;
	cin>>t;
	while(t--) solve();
	return 0;
}