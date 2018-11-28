//mohitbindal
#include <iostream>
#include <cstring>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <bitset>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define bitcnt(x) __builtin_popcountll(x)
#define MS0(x) memset(x, 0, sizeof(x))
#define MS1(x) memset(x, -1, sizeof(x))
#define mp(x, y) make_pair(x, y)
#define inputL(x) scanf("%lld", &x)
#define input(x) scanf("%d", &x)
#define inputS(x) scanf("%s", x)
#define printL(x) printf("%lld\n", x)
#define print(x) printf("%d\n", x)
#define PI acos(-1.0)
#define ff first
#define ss second

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
const ll INF = 1e9, MAX = 100100, mod = 1000000007;
char s[50];
int n;
ll dp[2][50][15], N[20], ten[20];

ll rec(int pos, int cur, int flag)
{
	if (pos == n - 1)
		return cur;
	ll ans = -1;
	if (flag)
	{
		ans = (cur * 1LL * ten[n - pos - 1]) + N[n - pos - 1];
		return ans;
	}
	if (cur > s[pos + 1] - '0')
		return -1;
	for (int i = cur; i < s[pos + 1] - '0'; i++)
	{
		ll tmp = rec(pos + 1, i, 1);
		if (tmp == -1)
			continue;
		tmp = (cur * 1LL * ten[n - pos - 1]) + tmp;
		ans = max(ans, tmp);
	}
	ll tmp = rec(pos + 1, s[pos + 1] - '0', 0);
	if (tmp != -1)
	{
		tmp = (cur * 1LL * ten[n - pos - 1]) + tmp;
		ans = max(ans, tmp);
	}
	return ans;
}

int main() {
#ifdef LOCAL_PROJECT
	freopen("../input.txt", "r", stdin);
	freopen("../output.txt", "w", stdout);
#endif
	// ios_base::sync_with_stdio(0);	cin.tie(0);	cout.tie(0);
	int T;
	ten[0] = 1;
	for (int i = 1; i < 19; i++)
	{
		N[i] = (N[i - 1] * 10LL) + 9LL;
		ten[i] = ten[i - 1] * 10LL;
	}
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		cin >> s;
		n = strlen(s);
		MS1(dp);
		ll ans = -1;
		for (int i = 1; i < (s[0] - '0'); i++)
		{
			ans = max(ans, rec(0, i, 1));
		}
		ans = max(ans, rec(0, s[0] - '0', 0));
		if (ans == -1)
		{
			for (int i = 1; i < n; i++)
				cout << 9;
			cout << endl;
		}
		else
			cout << ans << endl;
	}
	return 0;
}