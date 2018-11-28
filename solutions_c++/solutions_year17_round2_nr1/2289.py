#include <bits/stdc++.h>
using namespace std;

#ifndef LOCAL
#define endl "\n"
#endif

#define int int64_t

signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int test_count;
    cin >> test_count;
    cout.precision(16);
    for (int test_num = 1; test_num <= test_count; ++test_num)
    {
        int n, d;
        cin >> d >> n;
        long double res = 0;
        for (int i = 0; i < n; ++i)
        {
            int k, s;
            cin >> k >> s;
            res = max(res, (d - k) / ((long double)s));
        }
        cout << "Case #" << test_num << ": " << d / res << endl;
    }
    return 0;
}

