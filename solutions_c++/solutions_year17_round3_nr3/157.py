#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 55;

double p[MAXN];

int main()
{
    freopen("inputC.in" , "r" , stdin );
    freopen("output.out" , "w" , stdout );

    int T;
    cin >> T;

    cout << setprecision(10) << fixed;
    for (int _t = 1 ; _t <= T; _t++ )
    {
        int N, K;
        double U;
        cin >> N >> K;
        cin >> U;
        assert(N == K);

        for (int i = 1; i <= N; i++)
        {
            cin >> p[i];
        }

        sort(p + 1, p + N + 1);

        p[N + 1] = 1.0;
        for (int i = 1; i <= N; i++)
        {
            double extra = min(p[i + 1] - p[i], U / i);
            for (int j = 1; j <= i; j++)
            {
                p[j] += extra;
            }

            U -= extra * i;
        }

        double ans = 1.0;
        for (int i = 1; i <= N; i++)
        {
            ans *= p[i];
        }

        cout << "Case #" << _t << ": " << ans << endl;
    }

    return 0;
}
