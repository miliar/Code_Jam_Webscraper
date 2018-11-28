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

int main()
{
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		string N;
		cin >> N;

		string ans = N;

		for (int rep = 0; rep < N.length(); ++rep) {
			for (int i = 0; i + 1 < N.length(); ++i) {
				if (ans[i] > ans[i + 1]) {
					--ans[i];
					for (int j = i + 1; j < N.length(); ++j) {
						ans[j] = '9';
					}
				}
			}
		}

		ll ans_int;
		sscanf(ans.c_str(), "%lld", &ans_int);
		printf("Case #%d: %lld\n", tc, ans_int);
	}
}
