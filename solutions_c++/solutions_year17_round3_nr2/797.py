#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int t;

int main()
{
    ifstream cin("B-small-attempt0.in");
    ofstream cout("out.txt");
    ios_base::sync_with_stdio(false), cin.tie(nullptr);

    cin >> t;
    for (int step = 1; step <= t; step++)
    {
        int n, m, ans = 0, sum = 0;
        vector <int> seg;
        vector <pair <int, int> > ac, aj;

        cin >> n >> m;
        ac.resize(n);
        aj.resize(m);
        for (int i = 0; i < n; i++)
            cin >> ac[i].first >> ac[i].second;
        for (int i = 0; i < m; i++)
            cin >> aj[i].first >> aj[i].second;

        sort(ac.begin(), ac.end());
        sort(aj.begin(), aj.end());

        if (n == 1 || m == 1)
        {
            cout << "Case #" << step << ": ";
            cout << 2 << endl;
            continue;
        }
        else if (n == 0)
        {
            swap(n, m);
            swap(ac, aj);
        }

        seg.push_back(1440 + ac[0].first - ac[n - 1].second);
        for (int i = 1; i < n; i++)
            seg.push_back(ac[i].first - ac[i - 1].second);

        sort(seg.begin(), seg.end());

        for (int i = (int)seg.size() - 1; i >= 0; i--)
            if (sum < 720)
            {
                sum += seg[i];
                ans++;
            }

        cout << "Case #" << step << ": ";
        cout << 2 * ans << endl;
    }
    return 0;
}
