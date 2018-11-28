#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef pair<i64, i64> pi64;

void flip(string& S)
{
    replace(S.begin(), S.end(), '-', '*');
    replace(S.begin(), S.end(), '+', '-');
    replace(S.begin(), S.end(), '*', '+');
}

int flip_count(string S, int K)
{
    auto pos = S.find('-');
    if (pos == S.npos)
        return 0;

    string S1 = S.substr(pos, K);
    if (S1.length() < K)
        return -1;

    flip(S1);
    S.replace(pos, K, S1);

    int rs = flip_count(S, K);
    if (rs < 0)
        return -1;

    return rs + 1;
}

int main()
{
    int T;
    cin >> T;
    for1(tc, T)
    {
        cout << "Case #" << tc << ": ";

        //Solve problem here.
        string S;
        int K;
        cin >> S;
        cin >> K;

        auto rs = flip_count(S, K);
        if (rs >= 0)
            cout << rs;
        else
            cout << "IMPOSSIBLE";

        cout << endl;
    }
    return 0;
}
