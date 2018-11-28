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

const int max_S = 1e3 + 10;
char S[max_S];

int main()
{
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		int K;
		cin >> S >> K;
		int N = strlen(S);

		int ok = 1, cnt = 0;

		for (int i = 0; i < N; ++i) {
			if (S[i] == '-' && i + K - 1 < N) {
				for (int j = i; j < i + K; ++j) {
					S[j] ^= ('+' ^ '-');
				}
				++cnt;
			} else if (S[i] == '-') {
				ok = 0;
				break;
			}
		}

		printf("Case #%d: ", tc);
		if (!ok) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", cnt);
		}
	}
}
