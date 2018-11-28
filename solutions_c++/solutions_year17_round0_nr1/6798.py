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
const ll INF = 1e9, MAX = 1010, mod = 1000000007;
char s[MAX], S[MAX];
int n, K;

int fflip()
{
	int ans = 0;
	for (int i = 0; i + K - 1 < n; i++)
	{
		if (s[i] == '+')
			continue;
		ans++;
		for (int j = 0; j < K; j++)
			s[i + j] = ((s[i + j] == '+') ? '-' : '+');
	}
	return ans;
}

int bflip()
{
	int ans = 0;
	for (int i = n - 1; i >= K - 1; i--)
	{
		if (s[i] == '+')
			continue;
		ans++;
		for (int j = 0; j < K; j++)
			s[i - j] = ((s[i - j] == '+') ? '-' : '+');
	}
	return ans;
}

bool check()
{
	for (int i = 0; i < n; i++)
		if (s[i] == '-')
			return 0;
	return 1;
}

int main() {
	#ifdef LOCAL_PROJECT
		freopen("../input.txt", "r", stdin);
		freopen("../output.txt", "w", stdout);
	#endif
	// ios_base::sync_with_stdio(0);	cin.tie(0);	cout.tie(0);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> S >> K;
		n = strlen(S);
		for (int i = 0; i < n; i++)
			s[i] = S[i];
		s[n] = '\0';
		cout << "Case #" << t << ": ";
		if (n < K)
		{
			if (check())
				cout << "0\n";
			else
				cout << "IMPOSSIBLE\n";
			continue;
		}
		int a = fflip(), b;
		if (!check())
			a += bflip();
		if (!check())
			a = mod;
		for (int i = 0; i < n; i++)
			s[i] = S[i];
		s[n] = '\0';
		b = bflip();
		if (!check())
			b += fflip();
		if (!check())
			b = mod;
		a = min(a, b);
		if (a == mod)
			cout << "IMPOSSIBLE\n";
		else
			cout << a << endl;
	}
	return 0;
}