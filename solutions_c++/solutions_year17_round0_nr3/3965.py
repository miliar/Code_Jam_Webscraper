#include <iostream>
#include <queue>


using namespace std;

struct Range {
	int from, to, len;

	Range(int from, int to) {
		this->from = from;
		this->to = to;
		this->len = to - from;
	}
};

struct RangeComparator {
	bool operator() (Range *a, Range *b) {
		return a->len < b->len;
	}
};

void solve(int N, int K) {
	int maxDist = 0, minDist = 0;
	priority_queue<Range*, vector<Range*>, RangeComparator> pq;
	pq.push(new Range(0, N-1));

	// Simulate stalls being taken
	for(int i = 0; i < K; i++) {
		Range *rng = pq.top();
		pq.pop();
		int mid = rng->from + ((rng->to - rng->from) / 2);

		if(i == K-1) {
			maxDist = rng->to - mid;
			minDist = mid - rng->from;
			break;
		}

		if(mid < rng->to) { pq.push(new Range(mid+1, rng->to)); }
		if(mid > rng->from) { pq.push(new Range(rng->from, mid-1)); }
	}

	cout << maxDist << " " << minDist << endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	int T, N, K;
	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> N >> K;
		cout << "Case #" << (i+1) << ": ";
		solve(N, K);
	}
	return 0;
}
