#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <queue>

using namespace std;

struct Interval {
	int s, e;
	
	int mid, r_s, l_s;
	int mx, mn;
	
	bool operator<(const Interval& other) const {
		if (mn != other.mn) {
			return mn < other.mn;
		}
		if (mx != other.mx) {
			return mx < other.mx;
		}
		return mid > other.mid;
	}
	
	Interval(int s, int e) : s(s), e(e) {
		mid = (s + e) / 2;
		r_s = mid - s;
		l_s = e - mid;
		mn = min(l_s, r_s);
		mx = max(l_s, r_s);
	} 
};

Interval solve(int N, int K) {
	priority_queue<Interval> pq;
	pq.push(Interval(1, N));
	Interval prev(0,0);
	for (int i = 0; i < K; ++i) {
		prev = pq.top();
		pq.pop();
		int mid = prev.mid;
		// printf("Inserting %d\n", mid);
		if (prev.s <= mid - 1) {
			pq.push(Interval(prev.s, mid - 1));
		}
		if (prev.e >= mid + 1) {
			pq.push(Interval(mid + 1, prev.e));
		}
	}
	return prev;
}

int main() {
	freopen("c_in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		int N, K;
		scanf("%d%d", &N, &K);
		auto p = solve(N, K);
		printf("Case #%d: %d %d\n", i, p.mx, p.mn);
	}
	return 0;
}

