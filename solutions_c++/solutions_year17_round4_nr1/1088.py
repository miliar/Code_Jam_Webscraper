#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <climits>

#include <sstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <utility>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

#define fast_cin() ios_base::sync_with_stdio(false)

typedef long double ld;
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int max_N = 110;
const int max_P = 10;
int G[max_N];
int hsh[max_P];

int main()
{
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		memset(hsh, 0, sizeof(hsh));
		int N, P;
		cin >> N >> P;
		for (int i = 1; i <= N; ++i) {
			cin >> G[i];
			G[i] %= P;
			hsh[G[i]]++;
		}
		int ans = hsh[0];
		for (int i = 1; i < P; ++i) {
			if (i != (-i + P) % P) {
				int pairs = min(hsh[i], hsh[(-i + P)]);
				ans += pairs;
				hsh[i] -= pairs;
				hsh[P - i] -= pairs;
			} else {
				int pairs = hsh[i] >> 1;
				ans += pairs;
				hsh[i] %= 2;
			}
		}
		if (P == 3) {
			ans += hsh[2] / 3 + (hsh[2] % 3 > 0);
			ans += hsh[1] / 3 + (hsh[1] % 3 > 0);
		} else if (P == 4) {
			ans += hsh[3] / 4;
			ans += hsh[1] / 4;
			if (hsh[2]) {
				++ans;
				if (hsh[1] % 4 == 3) {
					++ans;
				}
				if (hsh[3] % 4 == 3) {
					++ans;
				}
			} else {
				ans += (hsh[1] % 4 > 0);
				ans += (hsh[3] % 4 > 0);
			}
		} else if (P == 2) {
			ans += (hsh[1] > 0);
		}

		printf("Case #%d: %d\n", tc, ans);
	}
}
