#include <bits\stdc++.h>
#define RUN_TEST
using namespace std;

struct Interval {
	int left, right;
	int length;

	Interval(int left, int right) : left(left), right(right) {
		length = right - left + 1;
	}

	bool operator < (const Interval& rhs) const {
		if (length < rhs.length)
			return true;
		else if (length == rhs.length && left > rhs.left)
			return true;
		return false;
	}
};

int main() {
#ifdef RUN_TEST
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, c = 1;
	scanf("%d", &T);
	while (T--) {
		int N, K, ans1, ans2;
		priority_queue<Interval> PQ;
		scanf("%d%d", &N, &K);

		PQ.push(Interval(1, N));
		for (int i = 0; i < K; i++) {
			Interval selected = PQ.top();
			PQ.pop();

			int chosenStall = (selected.left + selected.right) / 2;
			ans1 = max(chosenStall - selected.left, selected.right - chosenStall);
			ans2 = min(chosenStall - selected.left, selected.right - chosenStall);
			if (selected.left <= chosenStall - 1) {
				PQ.push(Interval(selected.left, chosenStall - 1));
			}
			if (selected.right >= chosenStall + 1) {
				PQ.push(Interval(chosenStall + 1, selected.right));
			}
		}

		printf("Case #%d: %d %d\n", c++, ans1, ans2);
	}
	return 0;
}