#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

#define mp make_pair

map<long long, long long> cnt;
map<long long, bool> ok;

priority_queue<long long> pq;

int main(){
	int T;
	long long N, K;
	scanf("%d", &T);
	for(int t=1;t<=T;t++){
		cnt.clear();
		ok.clear();
		scanf("%lld %lld", &N, &K);
		N--;
		pq.push(N/2+N%2);
		pq.push(N/2);

		cnt[N/2+N%2]++;
		cnt[N/2]++;
		printf("Case #%d: ", t);
		K--;
		if(K == 0){
			long long mx = N/2+N%2;
			long long mn = N/2;
			printf("%lld %lld\n", mx, mn);
			while(!pq.empty()) pq.pop();
			continue;
		}
		while(1){
			N = pq.top();
			pq.pop();
			if(ok.count(N)) continue;
			ok[N] = 1;
			K -= cnt[N];
			N--;
			if(K <= 0){
				long long mx = N/2+N%2;
				long long mn = N/2;
				printf("%lld %lld\n", mx, mn);
				while(!pq.empty()) pq.pop();
				break;
			}
			pq.push(N/2+N%2);
			pq.push(N/2);

			cnt[N/2+N%2] += cnt[N+1];
			cnt[N/2] += cnt[N+1];
		}
	}
}