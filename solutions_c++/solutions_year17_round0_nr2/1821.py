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

bool valid(string const& s)
{
    char last = 0;

    for (char c : s)
    {
        if (c < last) return false;
        last = c;
    }

    return true;
}

int main()
{
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        string in;
        cin >> in;
        while (!valid(in))
        {
            long long idx = in.size() - 1, exp = 0;
            while (in[idx] == '9')
                --idx, ++exp;

            long long num = stoll(in);
            num -= ((long long)pow(10LL, exp));
            in = to_string(num);
        }

        printf("Case #%d: %s\n", CASE, in.c_str());
    }

    return 0;
}
