#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

static_assert(sizeof(size_t) == 8, "asd");

int main() {
	int t;
	cin >> t;
	for (int it = 1; it <= t; ++it) {
		size_t N, K;
		cin >> N >> K;

		priority_queue<size_t> heap;
		heap.push(N);

		size_t x1, x2;

		for (size_t i = 0; i < K; ++i) {
			size_t x = heap.top();
			heap.pop();
			--x;
			x1 = x / 2;
			x2 = x - x1;
			heap.push(x1);
			heap.push(x2);
		}

		cout << "Case #" << it << ": " << max(x1, x2) << ' ' << min(x1, x2) << endl;
		cout.flush();
	}
}