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

bool good(char a, char b, bool stop = false)
{
    //red+blue=v
    //red=r
    //red+yellow=o
    //yellow=y
    //yellow+blue=g
    //blue=b
    //red+blue=v

    bool z1 = a == 'V'&&b == 'B';
    bool z2 = a == 'R'&&b == 'Y';
    bool z3 = a == 'R'&&b == 'G';
    bool z4 = a == 'R'&&b == 'B';
    bool z5 = a == 'O'&&b == 'B';
    bool z6 = a == 'Y'&&b == 'B';
    bool z7 = a == 'Y'&&b == 'V';
    bool z8 = stop ? false : good(b, a, true);

    return z1 || z2 || z3 || z4 || z5 || z6 || z7 || z8;
}

string build(int N, int R, int O, int Y, int G, int B, int V, char start)
{
    set<tuple<int, int, int, char>, greater<tuple<int, int, int, char>>> que;//count&color

    string imp = "IMPOSSIBLE";

    if (R)
        que.insert({ R, 0, 0, 'R' });
    if (O)
        que.insert({ O, 1, 0, 'O' });
    if (Y)
        que.insert({ Y, 0, 0, 'Y' });
    if (G)
        que.insert({ G, 1, 0, 'G' });
    if (B)
        que.insert({ B, 0, 0, 'B' });
    if (V)
        que.insert({ V, 1, 0, 'V' });

    string curr = "";

    for (auto it = que.begin(); it != que.end(); ++it)
    {
        if (get<3>(*it) != start)
            continue;

        curr = { start };
        auto t = *it;
        que.erase(t);
        get<2>(t)++;
        get<0>(t)--;
        if (get<0>(t))
            que.insert(t);

        break;
    }

    if (curr.size() == 0)
        return imp;

    auto dec = [&](tuple<int, int, int, char> p)
    {
        que.erase(p);
        get<0>(p)--;
        if (get<0>(p))
            que.insert(p);
    };

    for (int i = 0; i < N - 1; ++i)
    {
        switch (curr.back())
        {
        case 'R':
            for (auto& x : que)
                if (get<3>(x) == 'Y' || get<3>(x) == 'G' || get<3>(x) == 'B')
                {
                    curr += get<3>(x);
                    dec(x);
                    break;
                }
            break;
        case 'O':
            for (auto& x : que)
                if (get<3>(x) == 'B')
                {
                    curr += get<3>(x);
                    dec(x);
                    break;
                }
            break;
        case 'Y':
            for (auto& x : que)
                if (get<3>(x) == 'R' || get<3>(x) == 'B' || get<3>(x) == 'V')
                {
                    curr += get<3>(x);
                    dec(x);
                    break;
                }
            break;
        case 'G':
            for (auto& x : que)
                if (get<3>(x) == 'R')
                {
                    curr += get<3>(x);
                    dec(x);
                    break;
                }
            break;
        case 'B':
            for (auto& x : que)
                if (get<3>(x) == 'R' || get<3>(x) == 'O' || get<3>(x) == 'Y')
                {
                    curr += get<3>(x);
                    dec(x);
                    break;
                }
            break;
        case 'V':
            for (auto& x : que)
                if (get<3>(x) == 'Y')
                {
                    curr += get<3>(x);
                    dec(x);
                    break;
                }
            break;
        }
    }

    if (curr.length() != N || !good(curr[0], curr.back()))
        curr = imp;

    return curr;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;

    //cout.setf(ios::fixed);
    //cout.precision(20);

    for (int q = 1; q <= t; ++q)
    {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;

        string curr = build(N, R, O, Y, G, B, V, 'R');
        if (curr == "IMPOSSIBLE")
            curr = build(N, R, O, Y, G, B, V, 'O');
        if (curr == "IMPOSSIBLE")
            curr = build(N, R, O, Y, G, B, V, 'Y');
        if (curr == "IMPOSSIBLE")
            curr = build(N, R, O, Y, G, B, V, 'G');
        if (curr == "IMPOSSIBLE")
            curr = build(N, R, O, Y, G, B, V, 'B');
        if (curr == "IMPOSSIBLE")
            curr = build(N, R, O, Y, G, B, V, 'V');

        cout << "Case #" << q << ": " << curr << "\n";
    }

    return 0;
}