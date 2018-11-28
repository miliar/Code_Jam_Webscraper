#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <utility>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <cassert>
using namespace std;

#define REPP(i,a,b) for(int i=(a); i < (b); ++i)
#define REP(i,a) for(int i = 0; i < (a); ++i)
#define PER(i,a) for(int i = (a) - 1; i >= 0; --i)
#define SIZE(x) ((int)(x).size())
#define ALL(x) (x).begin(), (x).end()
#define MP make_pair

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, char> pic;

int solve() {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    vector<pic> a;
    a.push_back(MP(r, 'R'));
    a.push_back(MP(y, 'Y'));
    a.push_back(MP(b, 'B'));
    sort(ALL(a));
    string s = "";
    if (a[2].first > n / 2) return !printf("IMPOSSIBLE\n");
    REP(i, n) {
        int sz = SIZE(s);
        if (sz == 0 || a[2].second != s[sz - 1]) s += a[2].second, a[2].first -= 1;
        else s += a[1].second, a[1].first -= 1;
        sort(ALL(a));
    }
    if (s[0] == s[n - 1]) swap(s[n - 2], s[n - 1]);
    REP(i, n) {
        int aa = i % n, bb = (i + 1) % n;
        assert(s[aa] != s[bb]);
    }
    cout << s << endl;
    return 0;
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0);
    int T; cin >> T;
    REP(i, T) {
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}
