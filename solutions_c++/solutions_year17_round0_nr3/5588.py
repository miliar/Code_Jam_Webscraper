#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <limits>

#include <cstdio>
#include <cmath>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);

	int32_t T;
	cin >> T;

	for (auto tc = 1; tc <= T; tc++) {
		int64_t N, K;
		cin >> N >> K;

		priority_queue<int64_t, vector<int64_t>, less<int64_t> > PQ;
		PQ.push(N);

		int64_t count_v = 1;
		while (count_v < K) {
			int64_t left = PQ.top() / (int64_t)2;
			int64_t right = PQ.top() / (int64_t)2;
			
			if (PQ.top() % (int64_t)2 == 0) {
				left--;
			}
			PQ.pop();

			PQ.push(left);
			PQ.push(right);

			count_v++;
		}

		int64_t last_left = PQ.top() / (int64_t)2;
		int64_t last_right = PQ.top() / (int64_t)2;

		if (PQ.top() % (int64_t)2 == 0) {
			last_left--;
		}

		if (last_left < last_right) {
			swap(last_left, last_right);
		}

		cout << "Case #" << tc << ": " << last_left << " " << last_right << endl;
	}

	return 0;
}