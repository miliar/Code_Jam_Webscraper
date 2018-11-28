#include <bits/stdc++.h>
using namespace std;

#ifndef LOCAL
#define endl "\n"
#endif

#define mp(a, b) make_pair(a, b)
#define forn(i, n) for (int i = 0; i < n; ++i)
#define form(i, n, m) for (int i = n; i < m; ++i)
#define pb push_back

signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int test_count;
    cin >> test_count;
    for (int test_num = 1; test_num <= test_count; ++test_num)
    {
        int n, k;
        cin >> n >> k;
        vector < bool > a(n + 2);
        a[0] = true;
        a.back() = true;
        int best_l = 0;
        int best_r = 0;
        for (int i = 0; i < k; ++i)
        {
            best_l = 0;
            best_r = 0;
            int prev = -1;
            for (int j = 0; j < n + 2; ++j)
            {
                if (a[j])
                {
                    if (best_r - best_l < j - prev - 1)
                    {
                        best_r = j;
                        best_l = prev + 1;
                    }
                    prev = j;
                }
            }
            a[best_l + (best_r - best_l - 1) / 2] = 1;
        }
        cout << "Case #" << test_num << ": " << (best_r - best_l) / 2 << " " << (best_r - best_l - 1) / 2 << endl;
    }
    return 0;
}

