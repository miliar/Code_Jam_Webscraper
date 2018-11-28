#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <functional>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

unsigned t;
uint64_t n, k;

struct st {
	uint64_t left, right;
	bool operator < (const st& rhs) const {
		if (size() != rhs.size())
			return size() < rhs.size();
		return left < rhs.left;
	}
	uint64_t size() const {
		return right - left;
	}
};

void print_queue(priority_queue<st> q) {
	while (!q.empty()) {
		cout << "[" << q.top().left << "-" << q.top().right << "]; ";
		q.pop();
	}
	cout << '\n';
}

int main() {
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);
	cin >> t;
	for (unsigned cas = 1; cas <= t; cas++) {
		cin >> n >> k;
		priority_queue<st> Q;
		Q.push({0, n + 1});
		while (k-- > 1) {
			//print_queue(Q);
			st now = Q.top();
			Q.pop();
			Q.push({ now.left + (now.right - now.left) / 2, now.right });
			Q.push({ now.left, now.left + (now.right - now.left) / 2 });
		}
		//print_queue(Q);
		uint64_t x = Q.top().left + (Q.top().right - Q.top().left) / 2;
		//cout << "Chosen: " << x << endl;
		cout << "Case #" << cas << ": " << max(x - Q.top().left, Q.top().right - x) - 1 << " " << min(x - Q.top().left, Q.top().right - x) - 1 << endl;
	}
	return 0;
}