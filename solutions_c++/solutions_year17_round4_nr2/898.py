#include <bits/stdc++.h>

#define eb emplace_back
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define INF 0x3f3f3f3f

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const int N = 1010;
int pos[N], b[N];
int cnt[3][N];
int n, m, c;
priority_queue <pii> pq[3];
multiset <int> ms[3];
int main (void) {
	int t; scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		ms[1].clear();
		ms[2].clear();
		scanf("%d %d %d", &n, &c, &m);
//		if (tt == 19) cout << n << " " << c << " " << m << endl;
		for (int i = 0; i < m; i++) {
			scanf("%d %d", pos + i, b + i);
//			if (tt == 19) cout << pos[i] << " " << b[i] << endl;
			ms[b[i]].insert(pos[i]);
		}
		multiset <int>::iterator it = ms[1].begin(), it2;
		int tot = 0, cnt = 0;
		while (it != ms[1].end()) {
			it2 = ms[2].upper_bound(*it);
			if (it2 == ms[2].end()) {
				it++;
				continue;
			}
			it = ms[1].erase(it);
			ms[2].erase(it2);
			tot++;
		}
		it = ms[2].begin();
		while (it != ms[2].end()) {
			it2 = ms[1].upper_bound(*it);
			if (it2 == ms[1].end()) {
				it++;
				continue;
			}
			it = ms[2].erase(it);
			ms[1].erase(it2);
			tot++;
		}
		if (ms[1].empty()) {
			tot += ms[2].size();
		} else if (ms[2].empty()) {
			tot += ms[1].size();
		} else {
			if (*(ms[1].begin()) == 1) {
				tot += int(ms[2].size()) + int(ms[1].size());
			} else {
				tot += max(ms[1].size(), ms[2].size());
				cnt += min ( ms[1].size(), ms[2].size() );
			}
		}
		printf("Case #%d: %d %d\n", tt, tot, cnt);
	}
	return 0;
}

