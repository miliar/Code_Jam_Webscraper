#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <ctime>
#include <vector>
#include <queue>
#include <bitset>
#include <cmath>
#include <time.h>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <stdlib.h>
#include <deque>
#include <iomanip>
#include <complex>

using namespace std;

typedef long long ll;
typedef long double ld;

#define TIME (clock() * 1.0 / CLOCKS_PER_SEC)
#define rand_int ((rand() << 15) | rand())

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;
const ll prime = 239;
const ll MOD = 1e9 + 7;
const ll INF = 1e18;
const int BIG = 1e9 + 239;
const int MAX_N = 1e5 + 1;
const int MAX_T = (1 << 18);
const int MAX_LOG = 19;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {-1, 0, 1, 0};

void solve()
{
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    n -= 2 * o;
    b -= o;
    n -= 2 * g;
    r -= g;
    n -= 2 * v;
    y -= v;
    if (b < 0 || y < 0 || r < 0)
    {
        cout << "IMPOSSIBLE";
        return;
    }
    if (2 * b > n || 2 * y > n || 2 * r > n)
    {
        cout << "IMPOSSIBLE";
        return;
    }
    if (b == 0 && o > 0)
    {
        if (r == 0 && y == 0 && g == 0 && v == 0)
        {
            for (int i = 0; i < o; i++)
                cout << "BO";
            return;
        }
        cout << "IMPOSSIBLE";
        return;
    }
    if (r == 0 && g > 0)
    {
        if (o == 0 && y == 0 && g == 0 && b == 0)
        {
            for (int i = 0; i < g; i++)
                cout << "RG";
            return;
        }
        cout << "IMPOSSIBLE";
        return;
    }
    if (y == 0 && v > 0)
    {
        if (r == 0 && o == 0 && g == 0 && b == 0)
        {
            for (int i = 0; i < v; i++)
                cout << "VY";
            return;
        }
        cout << "IMPOSSIBLE";
        return;
    }
    string s = "";
    for (int i = 0; i < n; i++)
        s += ' ';
    vector<int> pos;
    for (int i = 0; i < n; i += 2)
        pos.push_back(i);
    for (int i = 1; i < n; i += 2)
        pos.push_back(i);
    vector<pair<int, char> > vv;
    vv.push_back(make_pair(r, 'R'));
    vv.push_back(make_pair(y, 'Y'));
    vv.push_back(make_pair(b, 'B'));
    sort(vv.begin(), vv.end());
    reverse(vv.begin(), vv.end());
    string t = "";
    for (int i = 0; i < vv[0].first; i++)
        t += vv[0].second;
    for (int i = 0; i < vv[2].first; i++)
        t += vv[2].second;
    for (int i = 0; i < vv[1].first; i++)
        t += vv[1].second;
    for (int i = 0; i < n; i++)
        s[pos[i]] = t[i];
    map<char, int> l;
    for (int i = 0; i < n; i++)
        l[s[i]] = i;
    string sr, sb, sy;
    sr = "";
    sb = "";
    sy = "";
    for (int i = 0; i < o; i++)
        sr += "OB";
    for (int i = 0; i < g; i++)
        sr += "GR";
    for (int i = 0; i < v; i++)
        sr += "VY";
    for (int i = 0; i < n; i++)
    {
        if (l.find(s[i]) != l.end() && l[s[i]] != i)
        {
            cout << s[i];
            continue;
        }
        cout << s[i];
        if (s[i] == 'B' && o > 0)
            cout << sb;
        if (s[i] == 'Y' && v > 0)
            cout << sy;
        if (s[i] == 'R' && g > 0)
            cout << sr;
    }
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    //freopen("small_input.txt", "r", stdin);
    freopen("small_output.txt", "w", stdout);
    //*
    //cout << fixed << setprecision(15);
    cin.sync_with_stdio(0);
    int number_of_tests;
    cin >> number_of_tests;
    for (int z = 0; z < number_of_tests; z++)
    {
        cout << "Case #" << z + 1 << ": ";
        solve();
        cout << endl;
    }
    /**/
    /*
    int number_of_tests;
    scanf("%d", &number_of_tests);
    for (int z = 0; z < number_of_tests; z++)
    {
        cout << "Case #" << z + 1 << ": ";
        solve();
        cout << "\n";
    }
    /**/
    return 0;
}
