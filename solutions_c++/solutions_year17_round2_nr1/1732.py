#include <bits/stdc++.h>

using namespace std;
#define int64 long long

namespace lazyc97
{
    const int module = 1000000007;
    const int n_max = 1010;

    pair<int, int> A[n_max];
    int n, m;
    int n_test;

    void enter()
    {
        cin >> m >> n;
        for (int i = 1; i <= n; ++i) cin >> A[i].first >> A[i].second;
        sort(A + 1, A + n + 1);
    }

    void solve()
    {
        double et = (double)(m - A[1].first) / A[1].second;
        for (int i = 2; i <= n; ++i)
            if (A[1].second > A[i].second)
            {
                double t = (double)(A[i].first - A[1].first) / (A[1].second - A[i].second);
                double rt = (m - A[i].first - A[i].second * t) / A[i].second;
                et = max(et, t + rt);
            }

        cout << setprecision(14) << fixed << m / et << "\n";
    }

    void run()
    {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        if (ifstream("../test.inp")) cin.rdbuf((new ifstream("../test.inp"))->rdbuf());
        cout.rdbuf((new ofstream("../test.out"))->rdbuf());

        cin >> n_test;
        for (int i = 1; i <= n_test; ++i)
        {
            cout << "Case #" << i << ": ";
            enter();
            solve();
        }
    }
}

int main() { lazyc97::run(); }
