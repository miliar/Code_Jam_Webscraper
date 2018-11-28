#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <utility>
using namespace std;

#define fi(i,a,b) for(int i=(a);i<(b); ++i)
#define fd(i,a,b) for(int i=(a);i>(b); --i)
#define fie(i,a,b) for(int i=(a);i<=(b); ++i)
#define fde(i,a,b) for(int i=(a);i>=(b); --i)
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define all(x) x.begin(), x.end()
#define rall(s) (s).rbegin(),(s).rend()
#define C(u) memset((u),0,sizeof((u)))
#define inf 1000000000
typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi > vvi;
typedef pair<int, int> pii;

#define INP_FILE "B-small-attempt1.in"
#define OUT_FILE "output.txt"

typedef pair<int, char> Corn;

bool solve() {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;

    vector<Corn> corn;
    corn.push_back(mp(r, 'R'));
    corn.push_back(mp(y, 'Y'));
    corn.push_back(mp(b, 'B'));
    sort(all(corn));
    if (corn[0].first + corn[1].first < corn[2].first) {
        return false;
    }

    vector<char> a;// (n + 1); a[n] = 0;
    int prev = 0;
    while (corn[0].first + corn[1].first > corn[2].first - 1) {
        prev = 1 - prev;
        if (corn[prev].first == 0) {
            return false;
        }
        corn[prev].first--;
        a.push_back(corn[prev].second);
    }
    corn[2].first--; a.push_back(corn[2].second);
    while (corn[2].first) {
        if (corn[0].first) {
            corn[0].first--; a.push_back(corn[0].second);
        }
        else {
            corn[1].first--; a.push_back(corn[1].second);
        }
        corn[2].first--; a.push_back(corn[2].second);
    }
    a.push_back(0);
    //fi(i,0,3) if (corn[i].first!=0) {
    //    //printf("-----------\n");
    //    cerr << "FUUU";
    //}
    //fi(i, 0, a.size() - 1) if (a[i] == a[i + 1]) {
    //    cerr << "FUUU";
    //}
    //if (a.size()!=n+1) {
    //    cerr << "FUUU";
    //}
    printf("%s\n", &a.front());
    return true;
}

int main()
{
    freopen(INP_FILE, "r", stdin);
    freopen(OUT_FILE, "w", stdout);
    int tstCnt; cin >> tstCnt;
    for (int tst = 1; tst <= tstCnt; tst++)
    {
        printf("Case #%d: ", tst);
        if (!solve()) printf("IMPOSSIBLE\n");
    }

    return 0;
}