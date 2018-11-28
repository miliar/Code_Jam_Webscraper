#include <iostream>
#include <cstring>
using namespace std;
#define MAXN 1500
#define N 1440
int C[MAXN], D[MAXN], J[MAXN], K[MAXN];
int Ac, Aj;
int a[MAXN];
int dp[MAXN][MAXN * 2][2];
int st;
int solve(int now, int diff, int last)
{
    int now2 = now - st;
    now2 = (now2 + N) % N;
    int diff2 = diff + N;
    int &ans = dp[now2][diff2][last];
    if (ans != -1)
        return ans;
    ans = MAXN;
    if (a[now] != -1) {
        int add = 0;
        if (a[now] != last)
            add = 1;
        diff += (a[now] == 0 ? 1 : -1);
        if (now2 == 0)
            return ans = (diff == 0 ? add : MAXN);
        ans = min(ans, solve((now + 1) % N, diff, a[now]) + add);
    }
    else
        for (int i = 0; i < 2; ++i)
            ans = min(ans, solve((now + 1) % N, diff + (i == 0 ? 1 : -1), i) + (i == last ? 0 : 1));
    return ans;
}
int main()
{
    int T;
    cin >> T;
    for (int Ti = 1; Ti <= T; ++Ti) {
        cin >> Ac >> Aj;
        for (int i = 0; i < Ac; ++i)
            cin >> C[i] >> D[i];
        for (int i = 0; i < Aj; ++i)
            cin >> J[i] >> K[i];
        memset(a, 0xff, sizeof(a));
        for (int i = 0; i < Ac; ++i)
            for (int j = C[i]; j < D[i]; ++j) {
                a[j] = 0;
                st = j;
            }
        for (int i = 0; i < Aj; ++i)
            for (int j = J[i]; j < K[i]; ++j) {
                a[j] = 1;
                st = j;
            }
        memset(dp, 0xff, sizeof(dp));
        int ans = solve((st + 1) % N, 0, a[st]);
        cout << "Case #" << Ti << ": " << ans << endl;
    }
    return 0;
}
