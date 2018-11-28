#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cstdlib>
#include <deque>
using namespace std;










void solve() 
{
    int r, c;
    cin >> r >> c;
    vector<string> cake;
    for (int i = 0; i < r; ++i)
    {
        string s;
        cin >> s;
        cake.push_back(s);
    }
//     cout << "input done" << endl;

    for (int i = 0; i < r; ++i)
    {
        for (int j = 0; j < c; ++j)
        {
            if (cake[i][j] == '?')
                continue;
            char init = cake[i][j];
            for (int k = j - 1; k >= 0; --k)
            {
                if (cake[i][k] != '?')
                    break;
                cake[i][k] = init;
            }
            for (++j; j < c; ++j)
            {
                if (cake[i][j] != '?')
                {
                    --j;
                    break;
                }
                cake[i][j] = init;
            }
        }
    }

//     cout << "fuck" << endl;
    for (int i = 1; i < r; ++i)
    {
        for (int j = 0; j < c; ++j)
        {
            if (cake[i][j] == '?')
                cake[i][j] = cake[i - 1][j];
        }
    }
//     cout << "fuck" << endl;

    for (int i = r - 1; i >= 0; --i)
    {
        for (int j = 0; j < c; ++j)
        {
            if (cake[i][j] == '?')
                cake[i][j] = cake[i + 1][j];
        }
    }

//     cout << "fuck" << endl;

    for (int i = 0; i < r; ++i)
    {
        cout << cake[i] << endl;
    }
}


int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ":" << endl;
        solve();
    }
    return 0;
}
