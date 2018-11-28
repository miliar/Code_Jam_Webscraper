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

int hd, ad, hk, ak, b, d;

int ans = 20000;

int get(int dbf, int bf, int atk) {
	bool t = false;
	if (!dbf && bf == 1 && atk == 1) {
		t = true;
	}
	if (!d && dbf) {
		return ans;
	}
	if (!b && bf) {
		return ans;
	}

	int s = dbf + bf + atk;
	int h = hd;
	int a = bf * b + ad;
	if (a * atk < hk) {
		return ans;
	}
	int a2 = ak;
	bool lastCure = false;
	while (dbf) {
//		cerr << "dbf" << endl;
		if (h - (a2 - d) <= 0) {
			if (lastCure) {
				return ans;
			}
			++s;
			h = hd;
			lastCure = true;
		} else {
			lastCure = false;
			a2 -= d;
			--dbf;
		}
		h -= a2;
	}
	lastCure = false;
	while (bf) {
//		cerr << "bf" << endl;
		if (hd - a2 <= 0) {
			return ans;
		}
		if (hd - a2 * 2 <= 0 && atk > 1) {
			return ans;
		}
		if (h - a2 <= 0) {
			if (lastCure) {
				return ans;
			}
			lastCure = true;
			++s;
			h = hd;
		} else {
			lastCure = false;
			--bf;
		}
		h -= a2;
	}
	if (t) {
		cerr << s << endl;
	}
	int h2 = hk;
	lastCure = false;
	while (atk) {
//		cerr << "atk" << endl;
		if (h - a2 <= 0 && h2 - a > 0) {
			++s;
			if (lastCure) {
				return ans;
			}
			if (s >= ans) {
				return s;
			}
			lastCure = true;
			h = hd;
		} else {
			h2 -= a;
			--atk;
			if (h2 <= 0) {
				return s;
			}
			lastCure = false;
		}
		h -= a2;
	}
	return s;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);

	for (int cass = 1; cass <= cas; ++cass) {
		printf("Case #%d: ", cass);
		cerr << "case " << cass << endl;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		bool possible = false;
		if (hd - (ak - d) - (ak - d * 2) > 0) {
			possible = true;
		}
		if (hd - ak > 0 && (hk - ad * 2 <= 0 || hk - b - ad <= 0)) {
			possible = true;
		}
		if (hk - ad <= 0) {
			possible = true;
		}
		if (!possible) {
			puts("IMPOSSIBLE");
			continue;
		}
		ans = 400;
		for (int bf = 0; bf <= 100; ++bf) {
			for (int atk = 0; atk <= 100; ++atk) {
				for (int dbf = 0; dbf <= 100; ++dbf) {
					if (dbf + bf + atk >= ans) {
						continue;
					}
					ans = min(ans, get(dbf, bf, atk));
				}
			}
		}
		cout << ans << endl;
	}
	fclose(stdin);
	fclose(stdout);
}

