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
    cout.precision(20);

    for (int q = 1; q <= t; ++q)
    {
        int d, n;
        cin >> d >> n;

        vector<intpair> h(n);

        double slowestReach = -1;

        for (auto& x : h)
        {
            cin >> x.first >> x.second;
            slowestReach = max(slowestReach, (d - x.first) / (double)x.second);
        }

        cout << "Case #" << q << ": " << d / slowestReach << "\n";
    }
    return 0;
}