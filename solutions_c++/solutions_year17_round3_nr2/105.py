#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <utility>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

typedef pair<int, int> pii;
#define fst first
#define snd second
#define pb push_back

int n, m;
pii a[111], b[111];
vector<int> s;
vector<int> at;
int cnt[2];
priority_queue<pii, vector<pii>, greater<pii>> heap[2];

int main() {
	int T;
	scanf("%d", &T);
	for (int kase = 1; kase <= T; ++ kase) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++ i) {
			scanf("%d%d", &a[i].fst, &a[i].snd);
		}
		for (int i = 0; i < m; ++ i) {
			scanf("%d%d", &b[i].fst, &b[i].snd);
		}
		sort(a, a + n);
		sort(b, b + m);
		s.clear();
		for (int i = 0; i < n; ++ i) {
			s.pb(a[i].fst);
			s.pb(a[i].snd);
		}
		for (int i = 0; i < m; ++ i) {
			s.pb(b[i].fst);
			s.pb(b[i].snd);
		}
		sort(s.begin(), s.end());
		s.resize(unique(s.begin(), s.end()) - s.begin());
		at.clear();
		at.resize(s.size(), -1);
		cnt[0] = cnt[1] = 0;
		for (int i = 0; i < n; ++ i) {
			for (int j = 0; j < s.size(); ++ j) {
				if (s[j] >= a[i].fst && s[j] < a[i].snd) {
					at[j] = 1;
					cnt[1] += s[j + 1] - s[j];
				}
			}
		}
		for (int i = 0; i < m; ++ i) {
			for (int j = 0; j < s.size(); ++ j) {
				if (s[j] >= b[i].fst && s[j] < b[i].snd) {
					at[j] = 0;
					cnt[0] += s[j + 1] - s[j];
				}
			}
		}
		while (heap[0].size()) heap[0].pop();
		while (heap[1].size()) heap[1].pop();
		for (int j = 0; j < s.size(); ++ j) {
			if (at[j] == -1) {
				int l = (j - 1 + s.size()) % s.size();
				int r = (j + 1) % s.size();
				if (at[l] == at[r]) {
					heap[at[l]].push(make_pair((s[r] - s[j] + 1440) % 1440, j));
				}
			}
		}
		while (heap[0].size() && cnt[0] + heap[0].top().first <= 720) {
			cnt[0] += heap[0].top().first;
			at[heap[0].top().second] = 0;
			heap[0].pop();
		}
		while (heap[1].size() && cnt[1] + heap[1].top().first <= 720) {
			cnt[1] += heap[1].top().first;
			at[heap[1].top().second] = 1;
			heap[1].pop();
		}
		int ans = 0;
		for (int j = 0; j < s.size(); ++ j) {
			// printf("%d %d\n", s[j], at[j]);
			int l = (j - 1 + s.size()) % s.size();
			int r = (j + 1) % s.size();
			if (at[j] == -1) {
				if (at[l] != at[r]) {
					++ ans;
				} else {
					ans += 2;
				}
			} else if (at[r] != -1) {
				ans += at[r] != at[j];
			}
		}
		printf("Case #%d: %d\n", kase, ans);
	}
	return 0;
}
