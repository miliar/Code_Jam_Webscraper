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
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;

const LD eps = 1e-9;
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

string str = "ROYGBV";
vector<int> a(6);

map<char, set<char> > block;

bool check(const string &s)
{
    int n = s.size();
    for (int i = 0; i < n; i++)
    {
        if (block[s[i]].count(s[(i + 1) % n]))
            return false;
    }
    return true;
}

void findAndInsert(string &ans, const string & temp, char ch)
{
    int pos = ans.find(ch);
    if (pos == string::npos)
        pos = 0;
    ans = ans.substr(0, pos) + temp + ans.substr(pos, ans.size() - pos);
}



string getAns(vector<pair<int, char> > mas)
{
    string res;
    for (int i = 0; i < mas[0].X; i++)
    {
        if (mas[1].X > 0) {
            res += string(1, mas[1].Y);
            mas[1].X--;
        }
        res += string(1, mas[0].Y);
    }
    reverse(all(res));

    string res2;
    int j = 0;
    for (int i = 0; i < mas[2].X; i++, j++)
        res2 += res[i] + string(1, mas[2].Y);

    res2 += res.substr(j);

    if (check(res2))
        return res2;
    else
        return "IMPOSSIBLE";
}

string genStr(const string &st, int count)
{
    string res = "";
    for (int i = 0; i < count; i++)
        res += st;
    return res;
}
void solve()
{
    block['R'].insert('R');
    block['R'].insert('O');
    block['R'].insert('V');
    block['Y'].insert('Y');
    block['Y'].insert('O');
    block['Y'].insert('G');
    block['B'].insert('B');
    block['B'].insert('G');
    block['B'].insert('V');

    block['O'].insert('O');
    block['O'].insert('R');
    block['O'].insert('Y');
    block['O'].insert('G');
    block['O'].insert('V');

    block['G'].insert('G');
    block['G'].insert('Y');
    block['G'].insert('B');
    block['G'].insert('O');
    block['G'].insert('V');

    block['V'].insert('V');
    block['V'].insert('B');
    block['V'].insert('R');
    block['V'].insert('O');
    block['V'].insert('G');

    int t;
    cin >> t;
    for (int q = 0; q < t; q++)
    {
        int n;
        cin >> n;
        for (int i = 0; i < 6; i++)
            cin >> a[i];

        string ans;

        int &R = a[0];
        int &O = a[1];
        int &Y = a[2];
        int &G = a[3];
        int &B = a[4];
        int &V = a[5];

        if (B < O || Y < V || R < G)
            ans = "IMPOSSIBLE";
        else {
            B -= O;
            Y -= V;
            R -= G;

            string BO = genStr("BO", O);
            string YV = genStr("YV", V);
            string RG = genStr("RG", G);

            vector<pair<int, char> > mas;
            mas.pb(mp(a[0], 'R'));
            mas.pb(mp(a[2], 'Y'));
            mas.pb(mp(a[4], 'B'));
            sort(mas.rbegin(), mas.rend());

            ans = getAns(mas);
            if (ans != "IMPOSSIBLE") {
                findAndInsert(ans, BO, 'B');
                findAndInsert(ans, YV, 'Y');
                findAndInsert(ans, RG, 'R');
                if (!check(ans))
                    ans = "IMPOSSIBLE";
            }
        }
        cout << "Case #" << q + 1 << ": " << ans << endl;
    }
}

int main()
{

    ios_base::sync_with_stdio(false);
    cout.setf(ios::fixed);
    cout.precision(10);
    //START
    //freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
    freopen("B-large.in", "r", stdin); freopen("output.txt", "w", stdout);
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