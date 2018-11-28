#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iterator>
#include <ctime>
#include <iomanip>

using namespace std;

int main()
{
    cout << setprecision(16);
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        int n, q;
        cin >> n >> q;

        vector<pair<int, int>> horses(n);
        vector<int> road(n);

        for (int i = 0; i < n; ++i)
            cin >> horses[i].first >> horses[i].second;

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                int len;
                cin >> len;

                if (len != -1)
                    road[i] = len;
            }
        }

        for (int i = 0; i < q; ++i)
        {
            int a, b;
            cin >> a >> b;
        }

        vector<double> res(n + 1);
        for (int i = n-1; i >= 0; --i)
        {
            int d = horses[i].first;
            int s = horses[i].second;
            long long dDone = road[i];


            res[i] = res[i+1] + 1.0 * road[i] / s;

            for (int j = i + 1; j < n; ++j)
            {
                if (dDone + road[j] > d)
                    break;

                dDone += road[j];
                res[i] = min(res[i], 1.0 * dDone / s + res[j + 1]);
            }
        }

        printf("Case #%d: ", CASE);
        cout << res[0] << endl;

    }

    return 0;
}
