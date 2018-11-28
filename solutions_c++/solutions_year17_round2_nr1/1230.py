#include <bits/stdc++.h>

using namespace std;

#define int int64_t

ifstream in("A-large.in");
ofstream out("A_big_ans.txt");

#define cin in
#define cout out

double solve()
{
    int d, n;
    cin >> d >> n;
    double mx = 0;
    for (int i = 0; i < n; ++i)
    {
        int k, s;
        cin >> k >> s;
        mx = max(mx, (double)(d - k) / (double)s);
    }
    return (double)d / mx;
}

signed main()
{
    int t;
    cin >> t;
    cout.precision(12);
    for (int itt = 0; itt < t; ++itt)
    {
        cout << "Case #" << itt + 1 << ": " << solve() << endl;
    }
    return 0;
}

