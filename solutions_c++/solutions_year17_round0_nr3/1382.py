#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>
#include <unordered_map>
#include <limits.h>
#include <assert.h>
#include <string.h>
#include <Util.h>
#include <queue>

using namespace std;

typedef long long int64_t;

void solve(int CASE, int64_t N, int64_t K) {
	priority_queue<int64_t> pq;
	unordered_map<int64_t, int64_t> set;
	pq.push(N);
	set[N] = 1;
	bool printed = false;
	while (!pq.empty()) {
		int64_t top = pq.top();
		pq.pop();
		int64_t count = set[top];
		K -= count;
		int64_t remaining = top - 1;
		// cout << "popping " << top << ", count = " << count << ", remaining = " << remaining << endl;
		if (remaining == 0) continue;
		int64_t low = remaining / 2;
		int64_t high = remaining - low;
		if (K <= 0) {
			cout << "Case #" << CASE << ": " << high << " " << low << endl;
			printed = true;
			break;
		}
		if (low > 0) {
// cout << "set[low] = " << set[low] << endl;
			if (set[low] == 0) {
				pq.push(low);
				// cout << "pushing " << low << endl;
			}
			set[low] += count;
		}
		if (high > 0) {
// cout << "set[high] = " << set[high] << endl;
			if (set[high] == 0) {
				pq.push(high);
				// cout << "pushing " << high << endl;
			}
			set[high] += count;
		}
	}
	if (!printed)
		cout << "Case #" << CASE << ": " << 0 << " " << 0 << endl;
	// cout << "---" << endl;
}

int main(int argc, const char * argv[]) {

	istream &fin = cin;
	// fstream fin("tiny.in");

	int T;
	fin >> T;
	int64_t N, K;
	for (int CASE = 1; CASE <= T; CASE++) {
		fin >> N;
		fin >> K;
		solve(CASE, N, K);
	}
    return 0;
}
