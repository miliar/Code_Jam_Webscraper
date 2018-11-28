#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
int tt;
typedef long long ll;
int A[1005];
ll N, K;
ll mi, ma;
void get() {
	for(int i = 0; i < N; i++) A[i] = 0;

	for(int i = 0; i < K; i++) {
		int a, b, maxi = -1, start = 0;
		for(int j = 0; j < N; j++) {
			if (A[j] == 0) continue;
			if (maxi < (j - start)) {
				a = start, b = j;
				maxi = j - start;
			}
			start = j + 1;
		}
		if (maxi < (N - start)) {
			a = start, b = N;
			maxi = N - start;
		}
		//cout << maxi << endl;
		mi = (maxi - 1) / 2;
		ma = maxi - 1 - mi;
		A[a + mi] = 1;
	}
}

void get2() {
	priority_queue<ll> q;
	q.push(N);
	for(int i = 1; i < K; i++) {
		ll t = q.top();q.pop();
		q.push((t - 1) / 2);
		q.push(t - 1 - ((t - 1) / 2));
	}
	ll maxi = q.top();
	mi = (maxi - 1) / 2;
    ma = maxi - 1 - mi;
}

void solve() {
	scanf("%lld %lld", &N, &K);
	get2();
	printf("Case #%d: %lld %lld\n", tt, ma, mi);
}
int main() {
	int t; scanf("%d", &t);
	for(tt=1; tt <= t; tt++) solve();
}
