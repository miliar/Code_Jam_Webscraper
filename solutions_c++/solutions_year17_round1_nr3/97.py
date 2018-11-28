#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <random>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const int MAX = 100;
const int INFTY = 1<<28;
int T, Hd, Ad, Hk, Ak, B, D;
int dp[101][101][101][101];

int getdp(int hd, int ad, int hk, int ak)
{
    if (hd <= 0)
        return INFTY;
    if (dp[hd][ad][hk][ak] != -1)
        return dp[hd][ad][hk][ak];
    
    dp[hd][ad][hk][ak] = INFTY;
    if (hk - ad > 0)
        dp[hd][ad][hk][ak] = min(dp[hd][ad][hk][ak], 1 + getdp(hd - ak, ad, hk - ad, ak));
    else
        dp[hd][ad][hk][ak] = min(dp[hd][ad][hk][ak], 1);
    if (ad < MAX)
        dp[hd][ad][hk][ak] = min(dp[hd][ad][hk][ak], 1 + getdp(hd - ak, min(MAX, ad + B), hk, ak));
    dp[hd][ad][hk][ak] = min(dp[hd][ad][hk][ak], 1 + getdp(Hd - ak, ad, hk, ak));
    dp[hd][ad][hk][ak] = min(dp[hd][ad][hk][ak], 1 + getdp(hd - max(ak - D, 0), ad, hk, max(ak - D, 0)));
    return dp[hd][ad][hk][ak];
}

int main()
{
	ios::sync_with_stdio(0);

    freopen("C.in", "r", stdin);
    freopen("Cout.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
        memset(dp, -1, sizeof(dp));
        int ans = getdp(Hd, Ad, Hk, Ak);
        if (ans == INFTY)
            cout << "Case #" << t << ": IMPOSSIBLE\n";
        else
            cout << "Case #" << t << ": " << ans << "\n";
    }

	return 0;
}
