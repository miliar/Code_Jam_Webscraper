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

const int N = 30;
char a[N][N];

int n, m;

bool in(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < m;
}

bool ck(int lx, int ly, int rx, int ry, char c) {
	for (int i = lx; i <= rx; ++i) {
		for (int j = ly; j <= ry; ++j) {
			if (a[i][j] != c && a[i][j] != '?') {
				return false;
			}
		}
	}
	return true;
}

void fill(int lx, int ly, int rx, int ry, char c) {
	for (int i = lx; i <= rx; ++i) {
		for (int j = ly; j <= ry; ++j) {
			a[i][j] = c;
		}
	}
}

//bool cmp(const tuple<int, int, char> &t1, const tuple<int, int, char> &t2) {
//	int
//}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);

	for (int cass = 1; cass <= cas; ++cass) {
		printf("Case #%d: ", cass);
		puts("");
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			scanf("%s", a[i]);
		}
		if (cass == 65) {
			for (int i = 0; i < n; ++i) {
				cerr << a[i] << endl;
			}
		}
		vector<tuple<int, int, char>> vec;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				vec.emplace_back(i, j, a[i][j]);
			}
		}
		sort(vec.begin(), vec.end());
		for (auto &tp : vec) {
			int x, y;
			char c;
			tie(x, y, c) = tp;
			for (int lx = 0; lx <= x; ++lx) {
				for (int ly = 0; ly <= y; ++ly) {
					for (int ry = m - 1; ry >= y; --ry) {
						for (int rx = n - 1; rx >= x; --rx) {
							if (ck(lx, ly, rx, ry, c)) {
								fill(lx, ly, rx, ry, c);
								goto done;
							}
						}
					}
				}
			}
			done:
			continue;
		}

		for (int i = 0; i < n; ++i) {
			puts(a[i]);
		}
	}
	fclose(stdin);
	fclose(stdout);
}

//int hd, ad, hk, ak, b, d;
//
//int ans = 20000;
//int get(int dbf, int bf, int atk) {
//	int s = dbf + bf + atk;
//	int h = hd;
//	int a = bf * b + ad;
//	if (a * atk < hk) {
//		return 20000;
//	}
//	int a2 = ak;
//	while (dbf) {
//		if (h - (a2 - d) <= 0) {
//			++s;
//			h = hd;
//		} else {
//			a2 -= d;
//			--dbf;
//		}
//		h -= a2;
//	}
//	while (bf) {
//		if (h - a2 <= 0) {
//			++s;
//			h = hd;
//		} else {
//			--bf;
//		}
//		h -= a2;
//	}
//	int h2 = hk;
//	while (atk) {
//		if (h - a2 <= 0 && h2 - a > 0) {
//			++s;
//			if (s >= 2000) {
//				return s;
//			}
//			h = hd;
//		} else {
//			h2 -= a;
//			--atk;
//		}
//		h -= a2;
//	}
//	return s;
//}
//
//int main() {
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
//	int cas;
//	scanf("%d", &cas);
//
//	for (int cass = 1; cass <= cas; ++cass) {
//		printf("Case #%d: ", cass);
//		cerr << "case " << cass << endl;
//		cin >> hd >> ad >> hk >> ak >> b >> d;
//		bool possible = false;
//		if (hd - (ak - d) - (ak - d * 2) > 0) {
//			possible = true;
//		}
//		if (hd - ak > 0 && (hk - ad * 2 <= 0 || hk - b - ad <= 0)) {
//			possible = true;
//		}
//		if (hk - ad <= 0) {
//			possible = true;
//		}
//		if (!possible) {
//			puts("IMPOSSIBLE");
//			continue;
//		}
//		ans = 2000;
//		for (int bf = 0; bf <= 100; ++bf) {
//			for (int dbf = 0; dbf <= 100; ++dbf) {
//				for (int atk = 0; atk <= 100; ++atk) {
//					if (dbf + bf + atk >= ans) {
//						continue;
//					}
//					ans = min(ans, get(dbf, bf, atk));
//				}
//			}
//		}
//		cout << ans << endl;
//	}
//	fclose(stdin);
//	fclose(stdout);
//}

