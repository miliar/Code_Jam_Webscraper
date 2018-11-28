#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;

pair<long long, long long> simulate_solve(long long N, long long K) {
	priority_queue<long long> heap;
	heap.push(N);
	for (int i = 0; i < K - 1; ++i) {
		long long stick_length = heap.top();
		heap.pop();
		long long n1 = (stick_length - 1) / 2;
		long long n2 = (stick_length - 1) - n1;
		heap.push(n1);
		heap.push(n2);
	}
	long long cur = heap.top();
	long long n1 = (cur - 1) / 2;
	long long n2 = (cur - 1) - n1;
	return make_pair(max(n1, n2), min(n1, n2));
}

pair<long long, long long> solve(long long N, long long K) {
	map<long long, long long> sticks;
	sticks[N] = 1;
	for (int round = 0; ; ++round) {
		map<long long, long long> next_sticks;
		long long new_sticks = 0;
		for (map<long long, long long>::iterator it = sticks.begin(); it != sticks.end(); ++it) {
			long long stick_length = it->first;
			long long n1 = (stick_length - 1) / 2;
			long long n2 = (stick_length - 1) - n1;
			next_sticks[n1] += it->second;
			next_sticks[n2] += it->second;
			new_sticks += it->second;
		}
		if (K > new_sticks) {
			K -= new_sticks;
		} else {
			for (map<long long, long long>::reverse_iterator it = sticks.rbegin();
				 it != sticks.rend(); ++it) {
				if (K > it->second) {
					K -= it->second;
				} else {
					long long stick_length = it->first;
					long long n1 = (stick_length - 1) / 2;
					long long n2 = (stick_length - 1) - n1;
					return make_pair(max(n1, n2), min(n1, n2));
				}
			}
		}
		sticks = next_sticks;
	}
}

void stress_test() {
	//for (int test = 0; test < 1000; ++test) {
	//	long long N = (rand() % 1000000) + 1;
	//	long long K = (rand() % N) + 1;
	//	assert(solve(N, K) == simulate_solve(N, K));
	//	cout << solve(N, K).first << " " << solve(N, K).second << endl;
	//}
	for (int test = 0; test < 1000; ++test) {
		long long N = (long long) 1e17;
		long long K = (long long) (1e9 * ((0.0 + rand() % 1000 + 1) / 1000.0));
		cout << N << " " << K << " " << solve(N, K).first << " " << solve(N, K).second << endl;
	}
}

int main() {
	int testsCount;
	cin >> testsCount;
	for (int test = 0; test < testsCount; ++test) {
		long long N, K;
		cin >> N >> K;
		pair<long long, long long> res = solve(N, K);
		cout << "Case #" << test + 1 << ": " << res.first << " " << res.second << endl;
	}
	return 0;
}
