#if 1
#include <functional>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <stdio.h>
#include <ctime>
#include <list>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;
typedef pair<LD, LD> pll;

 LD eps = 1e-7;
const LD pi = acos(-1.0);
const LL inf = 1e+9;
const LL inf64 = inf * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second

#define dbg(x) { cerr << #x << " = " << x << endl; }

// extended template
#pragma comment(linker, "/STACK:36777216")
typedef vector<int> vi;
typedef vector<vi> vvi;

#define forn(i, n) for (int i = 0; i < n; ++i)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

template<typename T> istream & operator >> (istream &, vector<T> &);
template<typename T> ostream & operator << (ostream &, const vector<T> &);

#define START clock_t _clock = clock();
#define END cerr << endl << "time: " << (clock() - _clock) / LD(CLOCKS_PER_SEC) << endl;

#define NAME "angle2"

vector <int> best;
int check(int P, vector <int> a)
{
    sort(all(a));
    int maxAns = 0;
    do{
        int ans = 0;
        int ost = 0;
        for (int i = 0; i < a.size(); i++)
        {
            if (ost == 0)
                ans++;
            ost = (ost + a[i]) % P;
        }
        if (ans > maxAns)
        {
            best = a;
        }
        maxAns = max(maxAns, ans);

    } while(next_permutation(all(a)));
    return maxAns;
}

void gen(int size, vector <int> &test)
{
    test.assign(size, 0);
    for (int i = 0; i < size; i++)
        test[i] = rand() % 100 + 1;
}

int solve(int P, const vector <int> &a)
{
    vector <int> ost(P);
    for (int i = 0; i < a.size(); i++)
        ost[a[i] % P]++;

    if (P == 2) {
        return ost[0] + (ost[1] + 1) / 2;
    }
    else if (P == 3)
    {
        int q = min(ost[1], ost[2]);
        ost[1] -= q;
        ost[2] -= q;

        return ost[0] + q + (ost[2] + 2) / 3 + (ost[1] + 2) / 3;
    } else
    {
        int q2 = ost[2] / 2;
        ost[2] -= 2 * q2;

        int q3 = min(ost[3], ost[1]);
        ost[3] -= q3;
        ost[1] -= q3;

        int add = 0;
        if (ost[1] > 0)
        {
            if (ost[2] > 0 && ost[1] >= 2)
            {
                add++;
                ost[1] -= 2;
            }

            add += (ost[1] + 3) / 4;
        } else if (ost[3] > 0)
        {
            if (ost[2] > 0 && ost[3] >= 2)
            {
                add++;
                ost[3] -= 2;
            }

            add += (ost[3] + 3) / 4;
        } else if (ost[2] > 0)
           add++;
        return ost[0] + q2 + q3 + add;

    }
}

void solve()
{
    int t;
    cin >> t;
    for (int q = 0; q < t; q++)
    {
        dbg(q);
        int p, n;
        cin >> n >> p;
        vector <int> g(n);
        for (int i = 0; i < n; i++)
            cin >> g[i];

        cout << "Case #" << q + 1 << ": "<< solve(p, g) << endl;
    }

    /*vector <int> a;
    for (int i = 0; i < 1000; i++)
    {
        int sz = rand() % 10 + 1;
        gen(sz, a);
        int P = 4;
        dbg(i);
        if (check(P, a) != solve(P, a))
        {
            dbg(check(P, a));
            dbg(solve(P, a));

            dbg(P);
            cout << a << endl;
            cerr << best << endl;;
            break;
        }
    }*/
}

int main()
{

    ios_base::sync_with_stdio(false);
    cout.setf(ios::fixed);
    cout.precision(19);
    //START
    //freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
    freopen("A-large.in", "r", stdin); freopen("output.txt", "w", stdout);
    solve();


    //END
    return 0;
}
/*******************************************
*******************************************/

template<typename T> istream & operator >> (istream &is, vector<T> &v)
{
    forn(i, v.size())
        is >> v[i];
    return is;
}
template<typename T> ostream & operator << (ostream &os, const vector<T> &v)
{
    forn(i, v.size())
        os << v[i] << " ";
    return os;
}
#endif