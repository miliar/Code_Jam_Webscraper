#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector< vector<int> > vvi;
typedef vector<ll> vl;
typedef vector< vector<ll> > vvl;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())
#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back

bool check(const string& s, bool checkLast = false) {
    int n = (int)s.size();
    forn(i, n - 1) {
        if (s[i] == s[i + 1]) return false;
    }
    if (checkLast && s[0] == s[n - 1]) return false;
    return true;
}

bool append(string& s, string c, bool checkLast = false) {
    for (int i = (int)s.size(); i >= 0; i--) {
        string t = s;
        t.insert(i, c);
        if (check(t, checkLast)) {
            s = t;
            return true;
        }
    }
    return false;
}

void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;
    int n;
    int r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    
    vector< pair<int, string> > c = {
        mp(r, "R"),
        mp(y, "Y"),
        mp(b, "B")
    };
    
    string s;
    forn(i, n) {
        bool ok = false;
        forn(j, 3) {
            if (c[j].first && append(s, c[j].second, i == n - 1)) {
                c[j].first--;
                ok = true;
                break;
            }
        }
        if (!ok) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << s << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
