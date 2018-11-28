#include<iostream>
#include<queue>
#include<vector>
#include<cstdio>
#include <set>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

double solution()
{
    int n, k;
    cin >> n >> k;
    double u;
    cin >> u;
    vector<double> p(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> p[i];
    }

    sort(p.begin(), p.end());
    double ans = 0.0;
    for (int i = 0; i < p.size(); ++i)
    {
        double sum = 0;
        for (int j = 0; j <= i; ++j)
        {
            sum += p[j];
        }
        sum += u;
        sum /= i + 1;
        sum = min(1.0, sum);
        if (sum < p[i])
        {
            break;
        }
        double res = 1.0;
        for (int j = 0; j < p.size(); ++j)
        {
            if (j <= i)
            {
                res *= sum;
            }
            else
            {
                res *= p[j];
            }
        }
        ans = res;
    }
    return ans;
}

int main()
{
    freopen("222.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": " << setprecision(9) << solution() << endl;
    }
    return 0;
}
