#include <bits/stdc++.h>
using namespace std;

map <long long, long long> M;

int main()
{
    int t;
    scanf ("%d", &t);

    for (int test=1; test<=t; test++)
    {
        long long n, k;
        scanf ("%lld%lld", &n, &k);
        M[-n] = 1;
        auto it = M.begin();

        while (it->second < k)
        {
            long long m = it->first;
            M[m / 2] += it->second;
            M[(m + 1) / 2] += it->second;
            k -= it->second;
            it++;
        }

        long long m = -(it->first);
        printf("Case #%d: %lld %lld\n", test, m / 2, (m - 1) / 2);
        M.clear();
    }

    return 0;
}