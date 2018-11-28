#include <bits/stdc++.h>

using namespace std;
#define int64 long long

namespace lazyc97
{
    const int module = 1000000007;
    const int n_max = 200010;

    int64 n, m;
    int n_test;

    void enter()
    {
        cin >> n >> m;
    }

    void solve()
    {
        map<int64, int64> P;
        P[n] = 1;

        while (true)
        {
            auto k = --P.end();
            m -= k->second;

            if (m <= 0)
            {
                cout << k->first / 2 << " " << (k->first - 1) / 2 << "\n";
                return;
            }

            if (k->first % 2 == 1) P[k->first / 2] += k->second * 2;
            else
            {
                P[(k->first - 1) / 2] += k->second;
                P[(k->first - 1) / 2 + 1] += k->second;
            }

            P.erase(k);
        }

        assert(false);
    }

    void solve_small()
    {
        bool M[1010] = {};

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
