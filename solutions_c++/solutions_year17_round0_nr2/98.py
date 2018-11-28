#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:10034217728")
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <cmath>

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

string s;

const int N = 50;
const int D = 10;
int dp[N][2][D];
vector<int> ans;

bool f(int pos, bool eq, int digit) {
	if (dp[pos][eq][digit] != -1) {
		return dp[pos][eq][digit];
	}
	if (pos >= s.size()) {
		return true;
	}
	dp[pos][eq][digit] = 0;
	for (int i = D - 1; i >= digit; i--) {
		if (eq && i > s[pos]) continue;
		bool next_eq = (eq && i == s[pos]);
		int next_pos = pos + 1;
		if (f(next_pos, next_eq, i)) {
			dp[pos][eq][digit] = 1;
			ans[pos] = i;
			break;
		}
	}
	return dp[pos][eq][digit];
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int n;
	cin >> n;
	for (int q = 0; q < n; q++) {
		cin >> s;
		ans.resize(s.size());
		for (int i = 0; i < s.size(); i++) s[i] -= '0';
		NEGATE(dp);
		f(0, 1, 0);
		printf("Case #%d: ", q + 1);
		int start_index = 0;
		if (ans[0] == 0) start_index++;
		for (int i = start_index; i < ans.size(); i++) printf("%d", ans[i]);
		printf("\n");
	}

	return 0;
}