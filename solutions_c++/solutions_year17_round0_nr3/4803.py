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
using ld = long double;
using d = double;
using vint = vector<int>;
using vll = vector<ll>;

struct Edge
{
    int to, w;
};

struct Line
{
    ll l, r;

    bool operator >(const Line& line) const
    {
        int diff = (r - l) - (line.r - line.l);
        if (diff != 0)
            return diff > 0;
        return l > line.l;
    }
};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;

    for (int z = 1; z <= t; ++z)
    {
        ll n, k;
        cin >> n >> k;

        set<Line, greater<Line>> lines;
        lines.insert({ 0, n });

        int maxva = 0, minva = 0;

        for (int i = 0; i < k; ++i)
        {
            Line line = *lines.begin();
            lines.erase(lines.begin());

            int midPos = (line.r - 1 + line.l) / 2;

            lines.insert({ line.l, midPos });
            lines.insert({ midPos + 1, line.r });
            maxva = max(midPos - line.l, line.r - midPos - 1);
            minva = min(midPos - line.l, line.r - midPos - 1);
        }

        cout << "Case #" << z << ": ";
        cout << (maxva) << " " << (minva);
        cout << "\n";
    }

    return 0;
}