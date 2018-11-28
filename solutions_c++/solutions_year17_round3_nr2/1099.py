// Problem B. Parenting Partnering
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

struct slot {
	int start, end, len, type;
	bool operator<(const slot &s) const { return start < s.start; }
};

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		int n, m;
		scanf("%d %d", &n, &m);
		vector<slot> a;
		slot s;
		int t0 = 0, t1 = 0;
		for (int i = 0; i < n + m; i++) {
			scanf("%d %d", &s.start, &s.end);
			s.len = s.end - s.start;
			if (i < n) {
				s.type = 0;
				t0 += s.len;
			} else {
				s.type = 1;
				t1 += s.len;
			}
			a.push_back(s);
		}

		sort(a.begin(), a.end());

		for ( ; ; ) {
			bool found = false;
			int min_len = -1, min_i;
			for (int i = 0; i < a.size(); i++) {
				if (a[i].type != 0) continue;
				slot &ps = i == 0 ? a[a.size() - 1] : a[i - 1];
				if (a[i].type == ps.type) {
					int len = a[i].end - ps.start;
					if (len < 0) len += 1440;
					if ((min_len < 0 || min_len > len) && (t0 + len - a[i].len - ps.len) <= 720) {
						min_i = i;
						min_len = len;
						found = true;
					}
				}
			}
			if (found) {
				if (min_i == 0) {
					if (t0 + min_len - a[min_i].len - a[a.size() - 1].len > 720)
						break;
					t0 += min_len - a[min_i].len - a[a.size() - 1].len;
					a[min_i].start = a[a.size() - 1].start - 1440;
					a[min_i].len = min_len;
					a.erase(a.begin() + a.size() - 1);
				} else {
					if (t0 + min_len - a[min_i].len - a[min_i - 1].len > 720)
						break;
					t0 += min_len - a[min_i].len - a[min_i - 1].len;
					a[min_i].start = a[min_i - 1].start;
					a[min_i].len = min_len;
					a.erase(a.begin() + min_i - 1);
				}
			} else {
				break;
			}
		}

		for ( ; ; ) {
			bool found = false;
			int min_len = -1, min_i;
			for (int i = 0; i < a.size(); i++) {
				if (a[i].type != 1) continue;
				slot &ps = i == 0 ? a[a.size() - 1] : a[i - 1];
				if (a[i].type == ps.type) {
					int len = a[i].end - ps.start;
					if (len < 0) len += 1440;
					if ((min_len < 0 || min_len > len) && (t1 + len - a[i].len - ps.len) <= 720) {
						min_i = i;
						min_len = len;
						found = true;
					}
				}
			}
			if (found) {
				if (min_i == 0) {
					if (t1 + min_len - a[min_i].len - a[a.size() - 1].len > 720)
						break;
					t1 += min_len - a[min_i].len - a[a.size() - 1].len;
					a[min_i].start = a[a.size() - 1].start - 1440;
					a[min_i].len = min_len;
					a.erase(a.begin() + a.size() - 1);
				} else {
					if (t1 + min_len - a[min_i].len - a[min_i - 1].len > 720)
						break;
					t1 += min_len - a[min_i].len - a[min_i - 1].len;
					a[min_i].start = a[min_i - 1].start;
					a[min_i].len = min_len;
					a.erase(a.begin() + min_i - 1);
				}
			} else {
				break;
			}
		}

		// printf("t0: %d, t1: %d\n", t0, t1);
		// for (int i = 0; i < a.size(); i++) printf("%d %d (len: %d, type: %d)\n", a[i].start, a[i].end, a[i].len, a[i].type);
		// printf("count: %d\n", (int) a.size());
		int ans = 1;
		for (int i = 1; i < a.size(); i++)
			ans += a[i].type == a[i - 1].type ? 2 : 1;
		if (ans % 2) ans++;

		printf("Case #%d: %d\n", ti, ans);
	}

	return 0;
}
