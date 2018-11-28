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
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        long long n, k;
        cin >> n >> k;

        vector<long long> size(2), count(2);
        size[0] = count[0] = 0;
        size[n % 2] = n;
        count[n % 2] = 1;

        if (size[1] == 0)
            size[1] = n + (((n / 2) % 2) ? -1 : 1);
        else
            size[0] = n + (((n / 2) % 2) ? 1 : -1);

        long long toArrive = k;
        long long oddSplit, evenSplit;
        while (toArrive > count[0] + count[1])
        {
            //cout << count[0] << "x" << size[0] << " " << count[1] << "x" << size[1] << endl;
            vector<long long> newSize(2), newCount(2);

            oddSplit = (size[1] - 1) / 2;
            newSize[oddSplit % 2] = oddSplit;
            evenSplit = size[0] ? size[0] - 1 - oddSplit : 0;
            newSize[evenSplit % 2] = evenSplit;

            if (oddSplit > 0)
                newCount[oddSplit % 2] = 2 * count[1] + count[0];

            if (evenSplit > 0)
                newCount[evenSplit % 2] += count[0];

            toArrive -= count[0] + count[1];
            count = newCount;
            size = newSize;
        }
        //cout << count[0] << "x" << size[0] << " " << count[1] << "x" << size[1] << endl;

        printf("Case #%d: ", CASE);

        long long maxx, minn;
        if (size[0] > size[1])
        {
            if (count[0] >= toArrive)
                maxx = size[0] / 2, minn = (size[0] - 1) / 2;
            else
                maxx = minn = size[1] / 2;
        }
        else
        {
            if (count[1] >= toArrive)
                maxx = minn = size[1] / 2;
            else
                maxx = size[0] / 2, minn = (size[0] - 1) / 2;
        }
        cout << maxx << " " << minn << endl;
    }

    return 0;
}
