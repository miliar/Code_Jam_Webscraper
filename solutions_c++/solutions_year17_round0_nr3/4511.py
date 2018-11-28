#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

int main() {

	int t;
	scanf("%d", &t);
	for (int testCase = 1; testCase <= t; testCase++) {

		priority_queue<pair<int64_t, int64_t> > q;

		map<pair<int64_t, int64_t>, int64_t> m;
		map<pair<int64_t, int64_t>, int64_t>::iterator mit;

		int64_t n, k, cur, cnt, a, b;
		scanf("%lld %lld", &n, &k);

		q.push(make_pair(n, 1));

		while(1){
			cur = q.top().first;
			cnt = q.top().second;
			q.pop();

			if (cur == 0) break;

			while (q.size()) {
				if (q.top().first == cur) {
					cnt += q.top().second;
					q.pop();
				}
				else {
					break;
				}
			}

			a = (cur - 1) / 2;
			b = cur - 1 - a;
			q.push(make_pair(a, cnt));
			q.push(make_pair(b, cnt));

			mit = m.find(make_pair(max(a, b), min(a, b)));
			if (mit != m.end()) {
				mit->second += cnt;
			}
			else {
				m.insert(make_pair(make_pair(max(a, b), min(a, b)), cnt));
			}
		}

		
		int64_t chk = 0;
		a = b = 0;
		map<pair<int64_t, int64_t>, int64_t>::reverse_iterator rit;
		for (rit = m.rbegin(); rit != m.rend(); ++rit) {
			if (rit->second + chk >= k) {
				a = rit->first.first;
				b = rit->first.second;
				break;
			}
			else {
				chk += rit->second;
			}
		}
		printf("Case #%d: %lld %lld\n", testCase, a, b);
	}

	return 0;
}