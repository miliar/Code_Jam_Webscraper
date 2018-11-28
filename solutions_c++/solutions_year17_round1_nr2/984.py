#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <unordered_map>
#include <unordered_set>

#define pb push_back
#define mp make_pair

//#define x first
//#define y second

using big = long long;

using namespace std;

//const int N = 30;
//char a[N][N];
//
//int n, m;
//
//bool in(int x, int y) {
//	return 0 <= x && x < n && 0 <= y && y < m;
//}
//
//bool ck(int lx, int ly, int rx, int ry, char c) {
//	for (int i = lx; i <= rx; ++i) {
//		for (int j = ly; j <= ry; ++j) {
//			if (a[i][j] != c && a[i][j] != '?') {
//				return false;
//			}
//		}
//	}
//	return true;
//}
//
//void fill(int lx, int ly, int rx, int ry, char c) {
//	for (int i = lx; i <= rx; ++i) {
//		for (int j = ly; j <= ry; ++j) {
//			a[i][j] = c;
//		}
//	}
//}
//
////bool cmp(const tuple<int, int, char> &t1, const tuple<int, int, char> &t2) {
////	int
////}
//
//int main() {
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
//	int cas;
//	scanf("%d", &cas);
//
//	for (int cass = 1; cass <= cas; ++cass) {
//		printf("Case #%d: ", cass);
//		puts("");
//		scanf("%d%d", &n, &m);
//		for (int i = 0; i < n; ++i) {
//			scanf("%s", a[i]);
//		}
//		if (cass == 65) {
//			for (int i = 0; i < n; ++i) {
//				cerr << a[i] << endl;
//			}
//		}
//		vector<tuple<int, int, char>> vec;
//		for (int i = 0; i < n; ++i) {
//			for (int j = 0; j < m; ++j) {
//				vec.emplace_back(i, j, a[i][j]);
//			}
//		}
//		sort(vec.begin(), vec.end());
//		for (auto &tp : vec) {
//			int x, y;
//			char c;
//			tie(x, y, c) = tp;
//			for (int lx = 0; lx <= x; ++lx) {
//				for (int ly = 0; ly <= y; ++ly) {
//					for (int ry = m - 1; ry >= y; --ry) {
//						for (int rx = n - 1; rx >= x; --rx) {
//							if (ck(lx, ly, rx, ry, c)) {
//								fill(lx, ly, rx, ry, c);
//								goto done;
//							}
//						}
//					}
//				}
//			}
//			done:
//			continue;
//		}
//
//		for (int i = 0; i < n; ++i) {
//			puts(a[i]);
//		}
//	}
//	fclose(stdin);
//	fclose(stdout);
//}
int n, m;
const int N = 1020;
int a[N][N], need[N];
int idx[N];
vector<pair<int, int>> range[N];

bool ok(int x, int price, int times) {
	return 0.9 * price * times <= x && x <= 1.1 * price * times;
}

bool intersect(const pair<int, int> &t0, const pair<int, int> &t1) {
	int l = max(t0.first, t1.first);
	int r = min(t0.second, t1.second);
	return l <= r;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int cass = 1; cass <= cas; ++cass) {
		printf("Case #%d: ", cass);
		cerr << "case " << cass << endl;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &need[i]);
			range[i].clear();
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%d", &a[i][j]);
			}
			sort(a[i], a[i] + m, greater<int>());
			idx[i] = 0;
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				int now = a[i][j] / need[i];
				int l = now, r = now;
				if (ok(a[i][j], need[i], r + 1)) {
					++r;
				}
				while (l > 0 && ok(a[i][j], need[i], l)) {
					--l;
				}
				while (ok(a[i][j], need[i], r)) {
					++r;
				}
				++l;
				--r;
//				cerr << need[i] << " " << now << " " << a[i][j] << " " << l << " l r  " << r << endl;
				if (l <= r && ok(a[i][j], need[i], l) && ok(a[i][j], need[i], r)) {
					range[i].emplace_back(l, r);
				}
			}
		}
		int ans = 0;
		int s = 10000000;
		for (int i = 0; i < n; ++i) {
			for (auto r : range[i]) {
				cerr << r.first << "," << r.second << " ";
			}
			cerr << endl;
		}
		cerr << endl;
		while (true) {
			bool fail = false;
			for (int i = 0; i < n; ++i) {
				if (idx[i] == range[i].size()) {
					fail = true;
				}
			}
			if (fail) {
				break;
			}
			vector<int> next_idx(n);
			function<bool(int)> ck = [&](int x) {
				for (int i = 0; i < n; ++i) {
					int j;
					for (j = idx[i]; j < range[i].size(); ++j) {
						const auto &r = range[i][j];
						if (r.first <= x && x <= r.second) {
							next_idx[i] = j + 1;
							break;
						}
					}
					if (j == range[i].size()) {
						return false;
					}
				}
				return true;
			};
			for (int i = 0; i < n; ++i) {
				s = min(s, range[i][idx[i]].second);
			}
			for (; s >= 1; --s) {
				if (ck(s)) {
					break;
				}
			}
			if (!s) {
				break;
			}
			if (ck(s)) {
				++ans;
				for (int i = 0; i < n; ++i) {
					idx[i] = next_idx[i];
				}
			}
		}
		printf("%d\n", ans);
	}
	fclose(stdin);
	fclose(stdout);
}

