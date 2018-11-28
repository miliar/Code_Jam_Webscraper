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
        int d, n;
        cin >> d >> n;

        double res = 0;
        for (int i = 0; i < n; ++i)
        {
            int k, s;
            cin >> k >> s;


            double dist = d - k;
            double time = dist / s;
            res = max(res, time);
        }

        printf("Case #%d: ", CASE);
        cout << 1.0 * d / res << endl;

    }

    return 0;
}
