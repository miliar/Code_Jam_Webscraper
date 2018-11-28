#include <bits/stdc++.h>

using namespace std;

const int N = 1e6 + 100;

int L[N], R[N], a[N];

int main()
{
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("1.out", "w", stdout);

    int tests;
    cin >> tests;

    for (int testNum = 1; testNum <= tests; ++testNum)
    {
        long long n, k, k1 = 0, k2 = 0;

        cin >> n >> k;

        for (int i = 0; i <= n + 1; ++i)
            a[i] = 0;
        a[0] = a[n + 1] = 1;

        for (int i = 0; i < k; ++i)
        {
            for (int j = 1; j <= n; ++j)
            {
                if (a[j]) continue;
                if (a[j - 1]) L[j] = j - 1;
                         else L[j] = L[j - 1];
            }
            for (int j = n; j >= 1; --j)
            {
                if (a[j]) continue;
                if (a[j + 1]) R[j] = j + 1;
                         else R[j] = R[j + 1];
            }
            int mx1 = -1, mx2 = -1, pos = 0;
            for (int j = 1; j <= n; ++j)
            {
                if (a[j]) continue;
                L[j] = j - L[j] - 1;
                R[j] = R[j] - j - 1;
               // cout << j << ' '<< min(L[j], R[j]) << ' ' << max(R[j], L[j]) << "\n";
                if (min(L[j], R[j]) > mx1)
                {
                    mx1 = min(L[j], R[j]);
                    mx2 = max(L[j], R[j]);
                    pos = j;
                } else
                if (min(L[j], R[j]) == mx1 && max(L[j], R[j]) > mx2)
                {
                    mx2 = max(L[j], R[j]);
                    pos = j;
                }
            }
            a[pos] = 1;
            //cout << pos << "\n";
            if (i == k - 1)
            {
                cout << "Case #" << testNum << ": " << mx2 << ' ' << mx1 << "\n";
            }
        }
    }
}
