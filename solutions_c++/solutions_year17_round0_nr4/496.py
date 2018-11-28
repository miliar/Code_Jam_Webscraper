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
#include <ctime>
#include <list>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;

const LD eps = 1e-9;
const LD pi = acos(-1.0);
const LL inf = 1e+9;

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

struct st
{
    char ch;
    int r, c;
    st () {}
    st(char ch, int r, int c) : ch(ch), r(r), c(c) {}
};

template<class T>
void print(vector<T> &a)
{
    for (int i = 0; i < a.size(); i++)
        cout << a[i].ch << " " << a[i].r + 1 << " " << a[i].c + 1 << endl;

}

void solve()
{
    int t;
    cin >> t;
    for (int q = 0; q < t; q++)
    {
        int n, m;
        cin >> n >> m;
        vector <st> ans;
        int posC = -1;
        vector<int> used(n);
        int sum = 0;
        for (int i = 0; i < m; i++)
        {
            char c;
            int x, y;
            cin >> c >> x >> y;
            x--;y--;
            used[y] = 1;
            if (c == 'x')
            {
                ans.pb(st('o', x, y));
                posC = y;
                sum += 2;
            }else
            if (c == 'o')
            {
                posC = y;
                sum += 2;
            }
            else
                sum += 1;
        }

        if (posC == -1)
        {
            for (int i = 0; i < n; i++)
                if (!used[i])
                {
                    used[i] = 1;
                    posC = i;
                    ans.pb(st('o', 0, i));
                    sum += 2;
                    break;
                }
        }
        if (posC == -1)
        {
            ans.pb(st('o', 0, 0));
            sum += 1;
            posC = 0;
        }

        for (int i = 0; i < n; i++)
        {
            if (!used[i])
            {
                used[i] = 1;
                ans.pb(st('+', 0, i));
                sum += 1;
            }
        }

        for (int i = 1; i < n; i++)
        {
            if (posC != i)
            {
                ans.pb(st('x', i, i));
            }
            else
            {
                ans.pb(st('x', i, 0));
            }
            sum += 1;
        }
        for (int i = 1; i < n - 1; i++)
        {
            ans.pb(st('+', n - 1, i));
            sum += 1;
        }

        cout << "Case #" << q + 1 << ": ";

        cout << sum<< " " << ans.size() << endl;
        print(ans);
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    //START
    //freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
    freopen("D-small-attempt0.in", "r", stdin); freopen("output.txt", "w", stdout);
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
