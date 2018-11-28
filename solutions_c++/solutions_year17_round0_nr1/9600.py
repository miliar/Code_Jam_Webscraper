#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

int main(int argc, char* argv[])
{
    int testCount;
    cin >> testCount;

    forn(test, testCount)
    {
        string s;
        int k, ans = 0;
        cin >> s >> k;

        for (int i = 0; i <= s.length() - k; i++)
            if (s[i] == '-') {
                ans++;
                forn(j, k)
                    s[i + j] = s[i + j] == '-' ? '+' : '-';
            }

        if (s == string(s.length(), '+'))
            cout << "Case #" << (test + 1) << ": " << ans << endl;
        else
            cout << "Case #" << (test + 1) << ": " << "IMPOSSIBLE" << endl;
    }

    return 0;
}
