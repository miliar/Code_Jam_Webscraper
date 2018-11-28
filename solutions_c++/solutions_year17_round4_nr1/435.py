#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define print_var(x) cerr << #x << " = " << x << endl
#define print_array(arr, len) {cerr << #arr << " = "; for (int i = 0; i < len; i++) cerr << arr[i] << " "; cerr << endl;}
#define print_iterable(it) {cerr << #it << " = "; for (const auto &e : it) cerr << e << " "; cerr << endl;}
#else
#define eprintf(...) (void)0
#define print_var(x) (void)0
#define print_array(arr, len) (void)0
#define print_iterable(it) (void)0
#endif

typedef long long ll;
const int N = 105;
const int INF = (int)1e9;

int dp[5][N][N][N][4];

void relax(int &a, int b)
{
    a = max(a, b);
}

void init()
{
    for (int p = 2; p <= 4; p++)
    {
        for (int r1 = 0; r1 < N; r1++)
            for (int r2 = 0; r2 < N; r2++)
                for (int r3 = 0; r3 < N; r3++)
                    for (int rem = 0; rem < p; rem++)
                        dp[p][r1][r2][r3][rem] = -INF;

        for (int rem = 0; rem < p; rem++)
            dp[p][0][0][0][rem] = 0;

        for (int r1 = 0; r1 < N; r1++)
            for (int r2 = 0; r2 < N; r2++)
                for (int r3 = 0; r3 < N; r3++)
                    for (int rem = 0; rem < p; rem++)
                    {
                        int val = dp[p][r1][r2][r3][rem];
                        if (val == -INF)
                            continue;

                        if (r1 + 1 < N)
                        {
                            int new_rem = (rem - 1 + p) % p;
                            int new_val = val + (new_rem == 0);
                            relax(dp[p][r1 + 1][r2][r3][new_rem], new_val);
                        }

                        if (2 < p && r2 + 1 < N)
                        {
                            int new_rem = (rem - 2 + p) % p;
                            int new_val = val + (new_rem == 0);
                            relax(dp[p][r1][r2 + 1][r3][new_rem], new_val);
                        }

                        if (3 < p && r3 + 1 < N)
                        {
                            int new_rem = (rem - 3 + p) % p;
                            int new_val = val + (new_rem == 0);
                            relax(dp[p][r1][r2][r3 + 1][new_rem], new_val);
                        }
                    }
    }
}

void solve()
{
    int n, p;
    scanf("%d%d", &n, &p);
    int r0 = 0, r1 = 0, r2 = 0, r3 = 0;
    for (int i = 0; i < n; i++)
    {
        int x;
        scanf("%d", &x);
        if (x % p == 0)
            r0++;
        if (x % p == 1)
            r1++;
        if (x % p == 2)
            r2++;
        if (x % p == 3)
            r3++;
    }

    int ans = dp[p][r1][r2][r3][0] + r0;
    printf("%d\n", ans);
}

int main()
{
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    init();
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }

    eprintf("\n\ntime = %.3lf\n", (double)clock() / CLOCKS_PER_SEC);
}
