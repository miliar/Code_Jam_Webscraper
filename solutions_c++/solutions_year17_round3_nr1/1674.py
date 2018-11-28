#include <iostream>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#define NLIMIT 1001
#define PI 3.14159265359

using namespace std;

double dp[NLIMIT][NLIMIT];

double solve(vector< pair<double, double> >& cakes, int n, int k)
{
    for(int i=1; i <= n; ++i)
    {
        dp[1][i] = PI * cakes[i].first * cakes[i].first +
                   2.0 * PI * cakes[i].first * cakes[i].second;
    }
    for(int i=0; i <= n; ++i)
        dp[i][0] = 0.0;

    double maxArea;
    for(int i=2; i <= k; ++i)
    {
        maxArea = dp[i][0];
        for(int j=1; j <= n; ++j)
        {
            maxArea = max(maxArea, dp[i-1][j-1]);

            double diskArea = PI * cakes[j].first * cakes[j].first;
            double lateralArea = 2.0 * PI * cakes[j].first * cakes[j].second;
            dp[i][j] = maxArea + lateralArea;
        }
    }

    maxArea = dp[k][0];
    for(int i=1; i <= n; ++i)
        maxArea = max(maxArea, dp[k][i]);

}

int main()
{
    int T;

    cin >> T;
    for(int t=1; t <= T; ++t)
    {
        int n, k;
        cin >> n >> k;

        vector< pair<double, double> > cakes(n+1);
        for(int i =1; i <= n; ++i)
            cin >> cakes[i].first >> cakes[i].second;
        vector< pair<double, double> >::iterator it = cakes.begin();
        it++;
        sort(it++, cakes.end());
        it = cakes.begin();
        it++;
        reverse(it, cakes.end());

        double res = solve(cakes, n, k);

        cout << "Case #" << t << ": ";
        printf("%.9f\n", res);
    }

    return 0;
}
