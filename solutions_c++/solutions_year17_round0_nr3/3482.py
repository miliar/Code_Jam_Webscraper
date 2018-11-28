#include <cstdio>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;
int main() {
    int TC;
    cin >> TC;

    for (int tc = 1; tc <= TC; tc++) {
	priority_queue<pair<long long, long long> > q;
	long long n, k;
	cin >> n >> k;
	q.push(make_pair(n, 0));

	long long mins, maxs;
	while(k--) {
	    long long cnt = q.top().first;
	    long long idx = -q.top().second;
	    q.pop();

	    long long leftend = idx;
	    long long rightend = idx+cnt-1;
	    long long mid = idx+(cnt-1)/2;

	    if (k == 0) {
		maxs = max(mid-leftend, rightend-mid);
		mins = min(mid-leftend, rightend-mid);
	    } else {
		q.push(make_pair(mid-leftend, -leftend));
		q.push(make_pair(rightend-mid, -(mid+1)));
	    }
	}

	while(!q.empty()) q.pop();
	printf("Case #%d: %lld %lld\n", tc, maxs, mins);
    }
    return 0;
}
