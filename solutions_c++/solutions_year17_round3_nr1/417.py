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
    int k, n;
    cin >> n >> k;
    vector<pair<int, int> > v; v.resize(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> v[i].first >> v[i].second;
    }
    class comparator
    {
    public:
        bool operator()(int v1, int v2) const
        {
            return v1 > v2;
        }
    };
    sort(v.begin(), v.end(), greater<pair<int, int> >());

    double ans = 0;
    for (int i = 0; i < v.size(); ++i)
    {
        priority_queue<double> pq;
        for (int j = i + 1; j < v.size() && k > 1; ++j)
        {
            double res = -M_PI * v[j].second * v[j].first * 2;
            if (pq.size() < k - 1 || pq.top() > res)
            {
                pq.push(res);
            }
            if (pq.size() > k - 1)
            {
                pq.pop();
            }
        }
        pq.push(-M_PI * v[i].first * 2 * v[i].second);
        double sum = M_PI * v[i].first * v[i].first;
        while(pq.size() > 0)
        {
            sum -= pq.top();
            pq.pop();
        }
        ans = max(ans, sum);
    }
    return ans;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt2", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": " << setprecision(30) << solution() << endl;
    }
    return 0;
}
