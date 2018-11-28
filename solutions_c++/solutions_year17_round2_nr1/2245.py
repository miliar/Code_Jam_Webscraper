#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	cout.precision(17);
	for(int i=1; i<=T; i++) {
		long long D, N;
		cin>>D>>N;
		long long distance[N], speed[N];
		double time[N];
		for(int i=0; i<N; i++) {
			cin>>distance[i]>>speed[i];
			time[i] = ((D-distance[i])*1.0)/(speed[i]*1.0);
		}
		sort(time, time+N);
		double ans = D/time[N-1];
		printf("Case #%d: %0.9f\n", i, ans);
		//cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}