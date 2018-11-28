#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

const int N = 33;
string s[N];

void go(int i1, int j1, int i2, int j2)
{
    int ct = 0;
    pair <int, int> fst, snd;
    fst = make_pair(-1, -1);
    for (int i = i1; i <= i2; i++)
        for (int j = j1; j <= j2; j++)
            if (s[i][j] != '?')
            {
                ct++;
                if (fst.first == -1)
                    fst = make_pair(i, j);
                else
                    snd = make_pair(i, j);
            }

    if (ct == 0)
        return;
    if (ct == 1)
    {
        for (int i = i1; i <= i2; i++)
            for (int j = j1; j <= j2; j++)
                s[i][j] = s[fst.first][fst.second];
        return;
    }

    if (fst.first < snd.first)
    {
        go(i1, j1, fst.first, j2);
        go(fst.first + 1, j1, i2, j2);
    }
    else if (fst.first == snd.first)
    {
        if (fst.second >= snd.second)
            assert(0);
        go(i1, j1, i2, fst.second);
        go(i1, fst.second + 1, i2, j2);
    }
    else
        assert(0);
}

#undef int
int main()
{
#define int long long
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        cerr << "Executing Case #" << tt << "\n";
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n; i++)
             cin >> s[i];
        go(0, 0, n - 1, m - 1);
        cout << "Case #" << tt << ":\n";
        for (int i = 0; i < n; i++)
            cout << s[i] << "\n";
    }
    return 0;
}
