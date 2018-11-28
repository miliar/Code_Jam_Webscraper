#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 0;
const double pi = acos(-1);

vector<pair<long long, long long> > p;
vector<long long> upper;

int main()
{
    freopen("inputA.in" , "r" , stdin );
    freopen("output.out" , "w" , stdout );

    int T;
    cin >> T;

    cout << setprecision(10) << fixed;
    for (int _t = 1 ; _t <= T; _t++ )
    {
        p.clear();
        upper.clear();

        int N, K;
        cin >> N >> K;

        for (int i = 1; i <= N; i++)
        {
            long long R, H;
            cin >> R >> H;
            p.push_back({R * R, R * H});
        }

        sort(p.begin(), p.end());

        long long ans = 0;
        for (int i = 0; i < N; i++)
        {
            long long res = p[i].first + 2 * p[i].second;
            if (upper.size() >= K - 1)
            {
                for (int j = 0; j < K - 1; j++)
                {
                    res += 2 * upper[j];
                }
                ans = max(res, ans);
            }

            upper.push_back(p[i].second);
            sort(upper.begin(), upper.end());
            reverse(upper.begin(), upper.end());
        }

        cout << "Case #" << _t << ": " << pi * ans << endl;
    }

    return 0;
}
