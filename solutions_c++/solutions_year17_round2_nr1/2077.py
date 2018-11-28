#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>
#include <climits>

#define INF 1000000000

using namespace std;

using ullong = unsigned long long;
using llong = long long;

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

int main()
{
    int t;
    cin >> t;
    int nmax = 10005;
        vector<double> k(nmax);
        vector<double> s(nmax);
    for (int tidx = 1; tidx <= t; ++tidx)
    {
        double d;
        int n;
        cin >> d >> n;
        int i, j;
        for(i=0; i<n; ++i)
        {
            cin >> k[i];
            cin >> s[i];
        }
        double time = 0.0;
        double timemax = 0.0;
        for(i=0; i<n; ++i)
        {
            time = (d - k[i]) / s[i];
            if (time > timemax)
                timemax = time;
        }

        double speed = d / timemax;

        cout << "Case #" << tidx << ": ";
        printf("%.6lf\n", speed);
    }
    return 0;
}
