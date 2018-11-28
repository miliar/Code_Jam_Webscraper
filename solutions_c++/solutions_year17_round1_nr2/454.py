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

const int max_N = 55;
const int max_P = max_N;
const int max_R = 1e6 + 10;
const int inf = 0x7f7f7f7f;

int inp[max_N][max_P];
int R[max_N];
int max_packs[max_R];
int currP[max_N];

int main()
{
	fast_cin();

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		int N, P;
		cin >> N >> P;
		for (int i = 1; i <= N; ++i) {
			cin >> R[i];
		}

		for (int i = 1; i <= N; ++i) {
			for (int j = 0; j < P; ++j) {
				cin >> inp[i][j];
			}
			sort(inp[i], inp[i] + P);
		}

		memset(max_packs, 0x7f, sizeof(max_packs));
		memset(currP, 0, sizeof(currP));

		int ans = 0;
		for (int r = 1; r < max_R; ++r) {
			int maxA = inf;
			for (int i = 1; i <= N; ++i) {
				int cnt = 0;
				for (int j = currP[i]; j < P; ++j) {
					if (R[i] * r * 9 <= inp[i][j] * 10 &&
							inp[i][j] * 10 <= R[i] * r * 11) {
						++cnt;
					} else if (R[i] * r * 9 > inp[i][j] * 10) {
						++currP[i];
					} else if (inp[i][j] * 10 > R[i] * r * 11) {
						break;
					}
				}
				maxA = min(maxA, cnt);
			}
			ans += maxA;
			for (int i = 1; i <= N; ++i) {
				currP[i] += maxA;
			}
		}

		printf("Case #%d: %d\n", tc, ans);
	}
}
