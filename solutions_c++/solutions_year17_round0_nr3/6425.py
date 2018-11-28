#include <cstdio>
#include <queue>
#include <unordered_map>

using namespace std;

pair<int, int> SplitInHalves(int K) {
	if (K % 2) {
		return make_pair(K / 2, K / 2);
	} else {
		return make_pair(K / 2, K / 2 - 1);
	}
}

void AddToState(const long long K, priority_queue<long long> &queue, unordered_map<long long, long long> &freq, long long val) {
	if (K <= 0) {
		return;
	}
	if (freq.find(K) == freq.end()) {
		queue.push(K);
	}
	freq[K] += val;
}

void Solve() {
	priority_queue<long long> queue;
	unordered_map<long long, long long> freq;
	long long N, numOps;
	scanf("%I64d %I64d", &N, &numOps);
	queue.push(N);
	freq[N] = 1;
	while (true) {
		const long long K = queue.top(); queue.pop();
		fprintf(stderr, "Processing %I64d %I64d\n", K, freq[K]);
		const long long largerHalf = K / 2;
		const long long smallerHalf = K / 2 - (1 - K % 2);
		numOps -= freq[K];
		if (numOps <= 0) {
			printf("%I64d %I64d\n", largerHalf, smallerHalf);
			return;
		}
		AddToState(largerHalf, queue, freq, freq[K]);
		AddToState(smallerHalf, queue, freq, freq[K]);
	}
}

int main() {
	freopen("data.in", "rb", stdin);
	freopen("data.out", "wb", stdout);
	int tst;
	scanf("%d", &tst);
	for (int index = 1; index <= tst; index++) {
		printf("Case #%d: ", index);
		Solve();
	}
	return 0;
}
