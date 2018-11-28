#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <map>
#include <utility>
#include <vector>
#include <ctime>
#include <queue>
#include <set>
#include <cmath>
#include <iostream>
#include <string>

using namespace std;

const int maxn = 1050;
int n, m, p[maxn], b[maxn];
vector<int> ride[maxn];
int minseat[maxn];
int appear[maxn][maxn];
int overlap = 0;
int counter = 0;
pair<int,int> tickets[maxn];

int ok(int q) {
	 // printf(" ok %d\n", q);
	counter ++;
	overlap = 0;
	for (int i = 1; i <= q; i ++) ride[i].clear();
	for (int i = 1; i <= q; i ++) minseat[i] = 1;
	for (int i = 1; i <= m; i ++) {
		int ppl = tickets[i].second;
		int seat = tickets[i].first;
		 // printf("i=%d,ppl=%d, seat=%d\n",i,ppl, seat);
		int found = 0;
		// no overlap
		for (int j = 1; j <= q; j ++) {
			if (seat >= minseat[j] && appear[j][ppl] != counter
				&& (ride[j].empty() || ride[j].back() != seat)) {
				found = j;
				break;
			}
		}
		// ok overlap
		if (found == 0) {
			for (int j = 1; j <= q; j ++) {
				if (seat >= minseat[j] && appear[j][ppl] != counter) {
					found = j;
					if (!ride[j].empty()) overlap += (bool)(ride[j].back() == seat);
					break;
				}
			}
		}
		 // printf("found=%d,ppl=%d,seat=%d\n", found,ppl,seat);

		if (found == 0){
			return -1;
		}
		appear[found][ppl] = counter;
		ride[found].push_back(seat);
		if ((int)ride[found].size() >= ride[found].back()) {
			minseat[found] = max(minseat[found], (int)ride[found].size() + 1);
		}
		 // printf("minseat[found]=%d, overlap=%d\n",minseat[found],overlap);
	}
	return overlap;
}


int tmp[maxn];
void solve(int tst) {
	counter = 0;
	int c;
	memset(appear, 0, sizeof appear);
	scanf("%d%d%d", &n, &c, &m);
	int cnt[3] = {0, 0, 0};
	int tot[3] = {0, 0, 0};
	memset(tmp, 0, sizeof tmp);
	bool spec = true;
	int maxtmp =0;
	for (int i = 1; i <= m; i ++) {
		scanf("%d%d", &p[i], &b[i]), tickets[i] = make_pair(p[i], b[i]);
		if (p[i] == 1) {
			cnt[b[i]] ++;
		}
		tot[b[i]] ++;
		if (p[i] > 2) {
			spec = false;
		}
		tmp[p[i]] ++;
		maxtmp=max(maxtmp, tmp[p[i]]);
	}
	int ans = max(cnt[1] + cnt[2], max(tot[1], tot[2]));

	sort(tickets + 1, tickets + 1 + m);
	// printf("hi\n");
	int l = 0, r = m + 1;
	while (l <= r) {
		int md = (l + r) / 2;
		if (ok(md) != -1) r = md - 1;
		else l = md + 1;
	}
	int rides = r + 1;
	int promotions = ok(rides);
	if (ans != rides) {
		// printf("WARNING case #%d %d,%d,%d\n", tst, n,m,c);
		// printf("==\n");
		// for (int i=1;i<=m;i++) printf("p,b=%d,%d\n", p[i],b[i]);
		// printf("===\n");
		rides = ans;
	}
	promotions = min(promotions,  max(0,maxtmp - ans));

	printf("Case #%d: %d %d\n", tst, rides, promotions);

}

int main() {
    int tst;
    scanf("%d", &tst);
    for (int t = 1; t <= tst; t ++) {
        solve(t);
    }
    return 0;
}
