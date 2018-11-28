#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <functional>
#include <limits>

using namespace std;

#ifndef M_PI
const double M_PI = 3.14159265358979323846;
#endif

class comparePancakes
{
public:
    bool operator()(const pair<double, double>& a, const pair<double, double>& b)
    {
        return a.first * a.second > b.first * b.second;
    };
};

int main()
{
    cout.precision(numeric_limits<double>::max_digits10);

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int NR;
    cin >> NR;
    for(int r = 1; r <= NR; r++)
    {
        cout << "Case #" << r << ": ";

        int n, k;
        cin >> n >> k;

        pair<double, double> pancakes[1000];

        for(int i = 0; i < n; i++)
        {
            double r, h;
            cin >> r >> h;
            pancakes[i] = pair<double, double>(r, h);
        }

        sort(pancakes, pancakes + n, comparePancakes());

        // Ext surface of the k - 1 bigger pancakes
        double extSurface = 0;
        for(int i = 0; i < k - 1; i++)
           extSurface += 2 * M_PI * pancakes[i].first * pancakes[i].second;

        double maxRayon = 0;
        for(int i = 0; i < k - 1; i++)
            maxRayon = max(maxRayon, pancakes[i].first);
        double maxIntSurface = M_PI * maxRayon * maxRayon;

        double maxSurface = 0;
        for(int i = k - 1; i < n; i++)
        {
            double intSurface = M_PI * pancakes[i].first * pancakes[i].first;
            intSurface = max(maxIntSurface, intSurface);

            maxSurface = max(maxSurface, intSurface + 2 * M_PI * pancakes[i].first * pancakes[i].second);
        }

        double finalSurface = extSurface + maxSurface;

        cout << finalSurface << endl;
    }

    return 0;
}
