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

bool check(string s)
{
    char last = s.back();
    for (char c : s)
        if (last == c)
            return false;
        else
            last = c;

    return true;
}

int main()
{
    cout << setprecision(16);
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;


        if (r + y < b || r + b < y || y + b < r)
        {
            printf("Case #%d: IMPOSSIBLE\n", CASE);
        }
        else
        {
            vector<pair<int, char>> arr = { {r, 'R'}, {y, 'Y'}, {b, 'B'} };
            sort(arr.begin(), arr.end());
            reverse(arr.begin(), arr.end());

            string res;
            while (n--)
            {
                int most = 0;
                if (res.size() && res.back() == arr[0].second)
                    ++most;

                if (arr[1].first > arr[most].first && (!res.size() || res.back() != arr[1].second))
                    most = 1;
                if (arr[2].first > arr[most].first && (!res.size() || res.back() != arr[2].second))
                    most = 2;

                res += arr[most].second;
                --arr[most].first;

                //cout << arr[0].first << ' ' << arr[1].first << ' ' << arr[2].first << endl;
            }

            assert(check(res));

            printf("Case #%d: ", CASE);
            cout << res << endl;
        }

    }

    return 0;
}
