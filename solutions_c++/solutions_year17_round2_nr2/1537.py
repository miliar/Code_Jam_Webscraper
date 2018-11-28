#include <bits/stdc++.h>

using namespace std;
#define int64 long long

namespace lazyc97
{
    const int module = 1000000007;
    const int n_max = 1010;

    pair<int, char> A[6];
    string so, sg, sv, res;
    int n;
    int n_test;

    void create_str(int i, int j, string &s)
    {
        s.clear();
        if (A[j].first == 0) return;

        s += A[i].second;
        for (int k = 0; k < A[j].first; ++k)
        {
            s += A[j].second;
            s += A[i].second;
        }

        A[i].first -= A[j].first + 1;
        A[j].first = 0;
    }

    inline void select(int i)
    {
        res += A[i].second; A[i].first--;
    }

    void enter()
    {
        cin >> n;
        for (int i = 0; i < 6; ++i) cin >> A[i].first;

        A[0].second = 'R';
        A[1].second = 'O';
        A[2].second = 'Y';
        A[3].second = 'G';
        A[4].second = 'B';
        A[5].second = 'V';
    }

    void solve()
    {
        if (n % 2 == 0)
        {
            char c1 = 0, c2 = 0;
            if (A[1].first == n / 2 && A[4].first == n / 2) c1 = A[1].second, c2 = A[4].second;
            if (A[3].first == n / 2 && A[0].first == n / 2) c1 = A[3].second, c2 = A[0].second;
            if (A[5].first == n / 2 && A[2].first == n / 2) c1 = A[5].second, c2 = A[2].second;

            if (c1 > 0)
            {
                for (int i = 1; i <= n; i += 2) cout << c1 << c2;
                cout << "\n";
                return;
            }
        }

        if ((A[1].first > 0 && A[1].first >= A[4].first) ||
            (A[3].first > 0 && A[3].first >= A[0].first && A[3].first + A[0].first < n) ||
            (A[5].first > 0 && A[5].first >= A[2].first && A[5].first + A[2].first < n))
        {
            cout << "IMPOSSIBLE\n";
            return;
        }

        create_str(4, 1, so);
        create_str(0, 3, sg);
        create_str(2, 5, sv);

        sort(A, A + 6);
        reverse(A, A + 6);

        res = "";
        if (A[0].second == 'R') res = so + sg + sv;
        if (A[0].second == 'Y') res = so + sv + sg;
        if (A[0].second == 'B') res = sg + so + sv;
        bool bc = !res.empty();

        if (A[0].first > A[1].first + A[2].first + bc)
        {
            cout << "IMPOSSIBLE\n";
            return;
        }

        if (A[0].first > 0)
        {
            if (bc) A[0].first--;

            while (A[1].first > A[2].first) select(0), select(1);

            int k = 1;
            while (A[0].first > 0) select(0), select(k), k = 3 - k;

            while (A[k].first > 0) select(k), k = 3 - k;

            if (bc) res += A[0].second;
        }

        cout << res << "\n";
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
