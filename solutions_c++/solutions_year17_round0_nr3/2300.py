#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> pi;
typedef pair<LL, LL> pLL;
map<LL, LL> mep;
set<LL> sit; // pake set biar ga overcount di PQ-nya 

int T;
LL N, K;
int main() {  
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		mep.clear();
		sit.clear();		
		scanf("%I64d %I64d", &N, &K);
		mep[N] = 1;
		priority_queue<LL> q; 
		q.push(N);
		while (!q.empty() && K > 0) {
			LL v = q.top(), freq = mep[q.top()];
			q.pop();
		
			// printf("Here \t%lld %lld\n", v, freq);
			
			// ganjil jadi 2 sama besar
			// genap jadi  v / 2 sama v - 1
			if (v % 2 == 0) {
				mep[v/2] += freq;
				if (sit.find(v / 2) == sit.end()) { 
					sit.insert(v/ 2);
					q.push(v / 2);
				}
				mep[v/2 - 1] += freq;
				if (sit.find(v / 2 - 1) == sit.end()) {
					sit.insert(v/ 2 - 1);
					q.push(v / 2 - 1);
				}			 
			}
			else {
				mep[v / 2] += 2 * freq;
				if (sit.find(v / 2) == sit.end()) {
					sit.insert(v/ 2);
					q.push(v / 2);
				}		 
			}
			
			K -= freq; 
			if (K <= 0) {
				printf("Case #%d: ", t + 1);
				if (v % 2) printf("%lld %lld\n", v / 2, v / 2);
				else printf("%lld %lld\n", v / 2, v / 2 - 1);
			}
		}

	}
  	return 0;
}
