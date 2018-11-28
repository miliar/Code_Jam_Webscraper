#include <queue>
#include <functional>
#include <bits/stdc++.h>

// compile with C++11 (g++ -std=c++11 -o c c.cpp)

#define DEBUG(x)

using namespace std;

// pair format = <available_spaces,left_index>
auto cmp = [](pair<int, int>& lhs, pair<int, int>& rhs) -> bool {
	if(lhs.first > rhs.first) {
		return false;
	} else if(lhs.first < rhs.first) {
		return true;
	} else {
		if(lhs.second < rhs.second) {
			return true;
		} else {
			return false;
		}
	}
};

priority_queue<pair<int, int>, vector<pair<int, int> >, decltype(cmp)> q(cmp);
int max_ans, min_ans;

int solve(int K) {
	int k, cap, pos, ncp;
	for(k = 0; k < K-1; ++k) {
		cap = q.top().first;
		pos = q.top().second;
		q.pop();
		if(cap == 1) continue;
		ncp = cap / 2;
		if(cap & 1) { // odd
			DEBUG(printf("Odd: %d and %d\n", cap, pos);)
			q.push(make_pair(ncp, pos));
			q.push(make_pair(ncp, pos + ncp + 1));
		} else { // even
			DEBUG(printf("Even: %d and %d\n", cap, pos);)
			if(ncp > 1) q.push(make_pair(ncp-1, pos));
			q.push(make_pair(ncp, pos + ncp));
		}
	}
	cap = q.top().first;
	pos = q.top().second;
	q.pop();
	DEBUG(printf("End: %d and %d\n", cap, pos);)
	if(cap & 1) {
		max_ans = cap/2;
		min_ans = cap/2;
	} else {
		max_ans = cap/2;
		min_ans = cap/2-1;
	}
	while(!q.empty()) q.pop();
}

int main() {
	int T, t, K, N, ans;
	scanf("%d", &T);
	for(t = 0; t < T; ++t) {
		scanf("%d %d", &N, &K);
		q.push(make_pair(N, 0));
		solve(K);
		printf("Case #%d: %d %d\n", t+1, max_ans, min_ans);
	}
	return 0;
}
