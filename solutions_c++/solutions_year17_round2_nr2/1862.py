#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <cassert>
#include <cmath>

#include <iostream>
#include <fstream>
#include <algorithm>
#include <utility>
#include <string>
#include <iterator>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <array>
#include <map>
#include <set>
#include <deque>
#include <set>
#include <unordered_set>
#include <unordered_map>

//#include<bits/stdtr1c++.h>

#define fi first
#define se second
#define inf 2147483647
#define mod 1000000009

#define mset(a, s) memset(a, s, sizeof(a))
#define forall(i,a,b) for(int i=a;i<b;++i)
#define max(a, b) (a < b ? b : a)
#define min(a, b) (a > b ? b : a)
#define all(a) a.begin(), a.end()
#define len(a) sizeof a/sizeof a[0]

/*/ --remove first * or add / before to enable scan--
#define scan(x) do{while((x=getchar())<0); for(x-='0';(_=getchar())>='0';x=(x<<3)+(x<<1)+_-'0');}while(0);
char _;//*/

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int T, n, r, o, y, g, b, v;

int maxb, minb, maxr, minr, maxy, miny;
char ans[1009];

int main(int argc, const char * argv[])
{
	scanf("%d", &T);
	for (int tc = 0; tc < T; ++tc) {

		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);

		if (b >= o+1) {
			b -= o;

		}
		else if (!(b + o == n && b == o) && (o != 0)) {
			printf("Case #%d: IMPOSSIBLE\n", tc + 1);
			continue;
		}

		if (r >= g+1) {
			r -= g ;
		}
		else if (!(r + g == n && r == g) && (g != 0)){
			printf("Case #%d: IMPOSSIBLE\n", tc + 1);
			continue;
		}

		if (y >= v+1) {
			y -= v;
		}
		else if (!(v + y == n && y == v) && (v != 0)) {
			printf("Case #%d: IMPOSSIBLE\n", tc + 1);
			continue;
		}

		mset(ans, 0);

		char c = 'R';
		if (b > r && b >= y) {
			c = 'B';
		}
		else if (y > r) c = 'Y';

		bool fo=false, fv=false, fg=false;

		int i;
		for (i = 0; i < n; ++i) {
			ans[i] = c;

			if (c == 'R') {
				if (!fg && g > 0) {
					int oi = i + 2 * g;
					while (g > 0 && i < n) {
						++i;
						if (i == n) i = 0;
						ans[i] = 'G';
						++i;
						if (i == n) i = 0;
						ans[i] = c;
						--g;
					}
					if (i < oi) break;
					fg = true;
				}


				--r;
				if (y > b) c = 'Y';
				else c = 'B';
			}

			else if (c == 'Y') {
				if (!fv && v > 0) {
					int oi = i + 2 * v;
					while (v > 0 && i < n) {
						++i;
						if (i == n) i = 0;
						ans[i] = 'V';
						++i;
						if (i == n) i = 0;
						ans[i] = c;
						--v;
					}
					if (i < oi) break;
					fv = true;
				}

				--y;
				if (b > r) c = 'B';
				else c = 'R';
			}

			else if (c == 'B') {
				if (!fo && o > 0) {
					int oi = i + 2 * o;
					while (o > 0 && i < n) {
						++i;
						if (i == n) i = 0;
						ans[i] = 'O';
						++i;
						if (i == n) i = 0;
						ans[i] = c;
						--o;
					}
					if (i < oi) break;
					fo = true;
				}
					
				--b;
				if (y > r) c = 'Y';
				else c = 'R';
			}
		}

		ans[n] = ans[0];
		bool bad = true;

		int tries = 0;

		while (bad && tries <= n * 100) {
			bad = false;
			// validate
			for (i = 0; i < n; ++i) {
				if (ans[i] == 'R' && (ans[i + 1] == 'V' || ans[i + 1] == 'O' || ans[i + 1] == 'R')) {
					bad = true;
					if (i == 0) swap(ans[i], ans[n-1]);
					else swap(ans[i], ans[i - 1]);
					break;
				}
				else if (ans[i] == 'Y' && (ans[i + 1] == 'Y' || ans[i + 1] == 'O' || ans[i + 1] == 'G')) {
					bad = true;
					if (i == 0) swap(ans[i], ans[n-1]);
					else swap(ans[i], ans[i - 1]);
					break;
				}
				else if (ans[i] == 'B' && (ans[i + 1] == 'B' || ans[i + 1] == 'V' || ans[i + 1] == 'G')) {
					bad = true;
					if (i == 0) swap(ans[i], ans[n-1]);
					else swap(ans[i], ans[i - 1]);
					break;
				}
				else if (ans[i] == 'O' && ans[i + 1] != 'B') {
					bad = true;
					if (i == 0) swap(ans[i], ans[n-1]);
					else swap(ans[i], ans[i - 1]);
					break;
				}
				else if (ans[i] == 'V' && ans[i + 1] != 'Y') {
					bad = true;
					if (i == 0) swap(ans[i], ans[n-1]);
					else swap(ans[i], ans[i - 1]);
					break;
				}
				else if (ans[i] == 'G' && ans[i + 1] != 'R') {
					bad = true;
					if (i == 0) swap(ans[i], ans[n-1]);
					else swap(ans[i], ans[i - 1]);
					break;
				}
			}
			++ tries;
		}

		ans[n] = 0;

		if (bad || r < 0 || b < 0 || y < 0)
			printf("Case #%d: IMPOSSIBLE\n", tc + 1);
		else
			printf("Case #%d: %s\n", tc + 1, ans);
	}

	return 0;
}