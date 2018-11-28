#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <functional>
#include <limits>
#include <queue>
#include <iomanip>
#include <deque>
#include <stack>
#include <cstdio>
#include <cmath>
#include <complex.h>
#include <cstdio>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

#ifndef ONLINE_JUDGE
    FILE *stream;
    freopen_s(&stream, "input.txt", "r", stdin);
    freopen_s(&stream, "output.txt", "w", stdout);
#endif

    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++)
    {
        int k;
        string s;
        cin >> s >> k;

        int flips = 0;
        int last_id = s.size() - k + 1;
        for (int i = 0; i < last_id; i++)
            if (s[i] == '-')
            {
                flips++;
                for (int j = 0; j < k; j++)
                    s[i + j] = s[i + j] == '-' ? '+' : '-';
            }

        bool possible = true;
        for (auto c : s)
            possible &= c == '+';

        cout << "Case #" << test_case << ": " << (possible ? to_string(flips) : "IMPOSSIBLE") << '\n';
    }
}