#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	int C = 1;
	while (T--) {
		int N, K;
		cin >> N >> K;
		priority_queue< int > pq;
		pq.push(N);
		int m, M;
		while (K) {
			int l = pq.top();
			pq.pop();
			if (l % 2 == 0) {
				m = l/2-1;
				M = l/2;
				pq.push(m);
				pq.push(M);
			} else {
				m = l/2;
				M = l/2;
				pq.push(m);
				pq.push(M);
			}
			K--;
		}
		cout << "Case #" << C++ << ": " << M << " " << m << endl;
	}
}