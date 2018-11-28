#include <bits/stdc++.h>

using namespace std;
#define int64 long long

namespace lazyc97
{
    const int module = 1000000007;
    const int n_max = 200010;

    string A;
    int n;
    int n_test;

    void enter()
    {
        cin >> A;
        n = (int) A.size();
    }

    void solve()
    {
        int r = 1;
        while (r < n && A[r] >= A[r - 1]) r++;

        if (r == n) { cout << A << "\n"; return; }

        int l = r - 1;
        while (l > 0 && A[l - 1] == A[l]) l--;

        if (l == 0 && A[l] == '1')
        {
            A.pop_back();
            fill(A.begin(), A.end(), '9');
        } else
        {
            A[l]--;
            for (int i = l + 1; i < n; ++i) A[i] = '9';
        }

        cout << A << "\n";
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
