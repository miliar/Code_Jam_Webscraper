#include <bits/stdc++.h>

using namespace std;

#define FROM_FILE freopen("input.txt", "r", stdin)
#define TO_FILE freopen("output.txt", "w", stdout)

#define ull unsigned long long
#define ll long long

#define PI 3.1415926535
#define INF 1e9
#define EPS 1e-6
#define prv(v) for (int iqiq = 0; iqiq < v.size(); iqiq++) cout << v[iqiq] << " "; cout << "\n"


double solve()
{
    int n, k;
    cin >> n >> k;
    double u;
    cin >> u;
    vector<double> vd(n + 1);
    for (int i = 0; i < n; ++i)
        cin >> vd[i];
    vd[n] = 1;

    sort(vd.begin(), vd.end());

    while (u > EPS)
    {
        int j = 1;
        while (j < n && abs(vd[0] - vd[j]) < EPS) j++;
        double add = std::min(u / j, vd[j] - vd[0]);
        for (int i = 0; i < j; ++i)
        {
            vd[i] += add;
            u -= add;
        }
    }

    double ans = 1;
    for (int i = 0; i < n; ++i)
        ans *= vd[i];
    return ans;
}

int main()
{
    FROM_FILE;
    TO_FILE;

    int tt;
    cin >> tt;
    cout.precision(8);
    for (int cs = 1; cs <= tt; ++cs)
    {
        cout << "Case #" << cs << ": " << fixed << solve() << "\n";
    }

    return 0;
}
