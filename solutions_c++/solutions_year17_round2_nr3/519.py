#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <fstream>
#include <string>
#include <stack>
#include <deque>
#include <algorithm>
#include <random>
#include <ctime>
#include <sstream>
#include <bitset>
#include <functional>
using namespace std;

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define mp make_pair
#define sq(x) ((x)*(x))
#define ifthen(x,y,z) ((x)?(y):(z))

using ll = long long;
using ull = unsigned long long;
using intpair = pair<int, int>;
using llpair = pair<ll, ll>;
using dpair = pair<double, double>;
using ld = long double;
using d = double;
using vint = vector<int>;
using vll = vector<ll>;

struct Edge
{
    int to, w;
};
//===========================================================================

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;

    cout.setf(ios::fixed);
    cout.precision(8);

    for (int xx = 1; xx <= t; ++xx)
    {
        int n, q;
        cin >> n >> q;

        vector<intpair> horses(n);//maxDist && speed
        for (auto& x : horses)
            cin >> x.first >> x.second;

        vector<vector<ll>> dist(n, vector<ll>(n));

        for (auto& y : dist)
            for (auto& x : y)
            {
                cin >> x;
                if (x == -1)
                    x = 1e18;
            }

        for (int i = 0; i < n; ++i)
            dist[i][i] = 0;

        for (int k = 0; k < n; ++k)
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);

        vector<vector<double>> V(n, vector<double>(n, 1e18));

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
            {
                if (i == j)
                {
                    V[i][j] = 0;
                    continue;
                }

                if (dist[i][j] <= horses[i].first)
                    V[i][j] = dist[i][j] / (double)horses[i].second;
            }

        for (int k = 0; k < n; ++k)
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    V[i][j] = min(V[i][j], V[i][k] + V[k][j]);

        int a, b;
        cout << "Case #" << xx << ": ";
        for (int i = 0; i < q; ++i)
        {
            cin >> a >> b;
            a--;
            b--;
            cout << V[a][b] << " ";
        }
        cout << endl;
    }

    return 0;
}