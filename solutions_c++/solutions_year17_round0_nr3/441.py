#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
#include <cstring>
using namespace std;
long long N,K;
void solve(){
	cin>>N>>K;
	map<long long, long long> cap;
	cap[N] = 1;
	priority_queue<long long> pq;
	pq.push(N);
	while (K > 0){
		long long curr = pq.top();

		//cout<<K<<" : "<<curr<<" : "<< cap[curr]<<endl;
		pq.pop();

		K -= cap[curr];
		//left
		long long l = (curr - 1) / 2;
		//right
		long long r = curr - l - 1;
		if (cap[l] == 0)
			pq.push(l);

		cap[l] += cap[curr];
		if (cap[r] == 0)
			pq.push(r);

		cap[r] += cap[curr];
		if (K <= 0)
			cout<<max(l,r)<<" "<<min(l,r)<<endl;
	}
}

int main(){
	int T;
	scanf("%d",&T);
	for (int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}
}