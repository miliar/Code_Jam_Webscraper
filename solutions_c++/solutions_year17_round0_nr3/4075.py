#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int c = 0; c < T; ++c) {
		int N, K;
		cin >> N >> K;
		priority_queue<int> pq;
		pq.push(N);
		for (int i = 0; i < K-1; ++i) {
			int n = pq.top();
			pq.pop();
			pq.push(n/2);
			pq.push((n-1)/2);
		}
		int t = pq.top();
		cout << "Case #" << (c+1) << ": " << t/2 << " " << (t-1)/2 << endl;
	}
	return 0;
}
