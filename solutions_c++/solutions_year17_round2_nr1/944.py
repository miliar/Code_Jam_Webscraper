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
#define pi acos(-1.0)
#define ff first
#define ss second

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
const ll INF = 1e18, MAX = 1010, mod = 1000000007;
ll D, n, K[MAX], s[MAX];

int main()
{
#ifdef LOCAL_PROJECT
    freopen("../input.txt", "r", stdin);
	freopen("../output.txt", "w", stdout);
#endif
    // ios_base::sync_with_stdio(0);	cin.tie(0);	cout.tie(0);
    int t, T;
    long double one = 1.0;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
    	cin >> D >> n;
    	for (int i = 0; i < n; i++)
    		cin >> K[i] >> s[i];
    	long double mx = (D - K[0]) * one / (s[0] * one);
    	for (int i = 1; i < n; i++)
    	{
    		long double cur = (D - K[i]) * one / (s[i] * one);
    		mx = max(mx, cur);
    	}
    	long double ans = D * one / mx;
    	cout << "Case #" << t << ": " << fixed << setprecision(6) << ans << endl;
    }
    return 0;
}
