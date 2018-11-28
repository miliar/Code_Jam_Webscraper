#include <iostream>
#include <queue>
#include <utility>

using namespace std;

pair<int, int> bathroom(int N, int K) {
	priority_queue<int> pq;
	pq.push(N);
	for (int i = 0; i < K - 1; ++i) {
		int stalls = pq.top();
		pq.pop();
		int l = stalls / 2, r = stalls - 1 - l;
		pq.push(l);
		pq.push(r);
	}
	int stalls = pq.top();
	int l = stalls / 2, r = stalls - 1 - l;
	return make_pair(l, r);
}

int main() {
	int T, N, K;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cin >> N >> K;
		pair<int, int> result = bathroom(N, K);
		cout << "Case #" << (i + 1) << ": " << result.first << " " << result.second << endl;
	}

	return 0;
}