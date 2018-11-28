#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

#define INF 1000000000

using namespace std;

using ullong = unsigned long long;
using llong = long long;
using Pair = pair<llong, llong>;

Pair f(llong n, llong k)
{
    if (k == 1)
        return Pair((n-1)/2, n/2);

    // k odd
    if (k & 1 == 1)
        return f((n-1)/2, k/2);

    // k even
    return f(n/2, k/2);
}

int main()
{
    int t;
    cin >> t;
    for (int tidx = 1; tidx <= t; ++tidx)
    {
        llong n, k;
        cin >> n >> k;

        Pair p = f(n, k);
        if (p.first < p.second)
            std::swap(p.first, p.second);

        cout << "Case #" << tidx << ": " << p.first << ' ' << p.second << endl;
    }
    return 0;
}
