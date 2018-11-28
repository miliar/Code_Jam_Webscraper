#include <iostream>
#include <queue>

typedef long long int64;

using namespace std;

struct segment {
	int64 left;
	int64 right;

	segment(): left(0), right(0) {}
	segment(int64 x, int64 y): left(x), right(y) {}

	bool operator<(const segment& other) const {
		if (right - left != other.right - other.left) {
			return (right - left < other.right - other.left);
		}
		return (left > other.left);
	}
};

pair<int64, int64> ans(int64 n, int64 k) {
	priority_queue<segment> queue;
	queue.push(segment(1, n));
	for (int u = 0; u < k; ++u) {
		segment current = queue.top();
		queue.pop();
		// cout << current.left << " " << current.right << "\n";
		int64 mid = (current.left + current.right) / 2;
		// cout << mid << "\n";
		if (u == k - 1) {
			return make_pair(mid - current.left, current.right - mid);
		}
		queue.push(segment(current.left, mid - 1));
		queue.push(segment(mid + 1, current.right));
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int64 n,k;
		cin >> n >> k;
		pair<int64, int64> res = ans(n,k);
		int64 x = max(res.first, res.second);
		int64 y = min(res.first, res.second);
		cout << "Case #" << t + 1 << ": " << x << " " << y << "\n";
	}
	return 0;
}