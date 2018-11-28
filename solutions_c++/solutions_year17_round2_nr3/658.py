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
    int n, q;
    cin >> n >> q;
    vector<ll> e;
    vector<ld> s;
    e.resize(n);
    s.resize(n);
    for (int i = 0; i < n; i++)
        cin >> e[i] >> s[i];
    vector<vector<ll> > d, mn;
    d.resize(n);
    mn.resize(n);
    for (int i = 0; i < n; i++)
        d[i].assign(n, 0);
    for (int i = 0; i < n; i++)
        mn[i].assign(n, INF);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
    {
        cin >> d[i][j];
        if (i == j)
        {
            mn[i][j] = 0;
            continue;
        }
        if (d[i][j] != -1)
            mn[i][j] = d[i][j];
    }
    for (int h = 0; h < n; h++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                mn[i][j] = min(mn[i][j], mn[i][h] + mn[h][j]);
    vector<vector<ld> > dist;
    dist.resize(n);
    for (int i = 0; i < n; i++)
        dist[i].assign(n, 0);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        {
            if (mn[i][j] > e[i]) ///!
                dist[i][j] = INF;
            else
                dist[i][j] = (1.0 * mn[i][j]) / s[i];
        }
    for (int h = 0; h < n; h++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                dist[i][j] = min(dist[i][j], dist[i][h] + dist[h][j]);
    for (int i = 0; i < q; i++)
    {
        int s, f;
        cin >> s >> f;
        s--, f--;
        cout << dist[s][f] << " ";
    }
}

int main()
{
    freopen("C-large.in", "r", stdin);
    //freopen("small_input.txt", "r", stdin);
    freopen("small_output.txt", "w", stdout);
    //*
    cout << fixed << setprecision(15);
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
