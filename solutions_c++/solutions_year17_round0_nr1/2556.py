#include <bits/stdc++.h>

using namespace std;
#define int64 long long

namespace lazyc97
{
    const int module = 1000000007;
    const int n_max = 200010;

    string A;
    int n, m;
    int n_test;

    void flip(int x)
    {
        for (int i = x; i < x + m; ++i)
            A[i] = (A[i] == '+') ? '-' : '+';
    }

    void enter()
    {
        cin >> A >> m;
        n = (int) A.size();
    }

    void solve()
    {
        int cnt = 0;
        for (int i = 0; i + m <= n; ++i)
            if (A[i] == '-')
            {
                flip(i);
                cnt++;
            }

        if (count(A.begin(), A.end(), '-') == 0)
            cout << cnt << "\n";
        else
            cout << "IMPOSSIBLE\n";
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
