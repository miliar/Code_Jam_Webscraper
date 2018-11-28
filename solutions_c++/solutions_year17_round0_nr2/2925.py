#include <cassert>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <cstddef>
#include <cctype>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <list>
#include <string>
#include <functional>
#include <utility>
using namespace std;
typedef long long llint;
llint solve(llint n)
{
    stringstream ss;
    string s;
    ss << n;
    ss >> s;
    while (true)
    {
        string::size_type i;
        for (i = 1; i < s.size(); ++i)
        {
            if (s[i] < s[i - 1])
            {
                s[i - 1] -= 1;
                fill(s.begin() + i, s.end(), '9');
                break;
            }
        }
        if (i == s.size())
        {
            break;
        }
    }
    llint ret;
    stringstream ss_;
    ss_ << s;
    ss_ >> ret;
    return ret;
}
int main()
{
    int tc;
    cin >> tc;
    for (int cc = 1; cc <= tc; ++cc)
    {
        llint n;
        cin >> n;
        cout << "Case #" << cc << ": " << solve(n) << endl;
    }
    return 0;
}
