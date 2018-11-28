#include<bits/stdc++.h>
using namespace std;
int main() {
	int T; cin >> T;
	for (int tc=1; tc<=T; tc++) {
		int N, K; cin >> N >> K;
		priority_queue<int> Q;
		Q.push(N);
		for (int it=1; it<=K; it++) {
			int d = Q.top();
			Q.pop();
			if (it == K) printf("Case #%d: %d %d\n", tc, d / 2, (d - 1) / 2);
			else Q.push(d / 2), Q.push((d - 1) / 2);
		}
	}
}
