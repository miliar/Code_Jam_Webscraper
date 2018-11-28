#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

#define INF 1000000000

using namespace std;

using ullong = unsigned long long;
using llong = long long;
using Pair = pair<llong, llong>;

template<typename T>
T Pow(T a, T n)
{
    T res = 1;
    while (n)
    {
        if (n & 1)
            res *= a;
        a *= a;
        n >>= 1;
    }
    return res;
}


struct Solver
{
    void solve()
    {
    }

    void print()
    {
    }
};

int main()
{
    int t;
    cin >> t;
    for (int tidx = 1; tidx <= t; ++tidx)
    {
        int n, k;
        cin >> n >> k;
        vector<Pair> v(n);
        int i, j;
        for(i=0; i<n; ++i)
        {
            cin >> v[i].first >> v[i].second;
        }
        sort(v.begin(), v.end(), [] (const Pair& a, const Pair& b) {
            return a.first > b.first ||
                (a.first == b.first && a.second > b.second);
        });

        llong tmax = -1;
        llong curr = 0;
        for (i=0; (i+k-1) < n; ++i)
        {
            curr = v[i].first * v[i].first + 2 * v[i].first * v[i].second;
            vector<Pair> v2((v.begin()+i+1), v.end());
            sort(v2.begin(), v2.end(), [](const Pair& a, const Pair& b) {
                 return a.first * a.second > b.first * b.second;
            });
            for(j=0; j<(k-1); ++j)
                curr += 2 * v2[j].first * v2[j].second;
            if (curr > tmax)
                tmax = curr;
        }

        cout << "Case #" << tidx << ": ";
        printf("%.9lf\n", (double)tmax * M_PI);

    }
    return 0;
}
