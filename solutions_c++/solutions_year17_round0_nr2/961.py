#include<bits/stdc++.h>

#define show(x) cout << #x << " = " << x << endl;

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<double, ii> iii;

const int MAX = 200005;
const double EPS = 1e-5;
const int INF = INT_MAX;

bool seen[30][11][2];

string ans = "";

bool go(int pos, int last, bool same, string &s) {
    if(seen[pos][last][same]) return false;
    if(pos == s.size()) {
        return true;
    }

    int limit = same ? s[pos]-'0' : 9;
    for(int i = limit; i >= last; i--) {
        if(i != 0) ans.push_back(i+'0');
        if(go(pos+1, i, same && (s[pos] - '0' ==  i), s))
            return true;
        if(i != 0) ans.pop_back();
    }

    return false;
}

int cases;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    #ifdef FSOCIETY
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif // FSOCIETY

    int t; cin >> t;
    while(t--) {
        memset(seen, false, sizeof seen);
        string s; cin >> s;
        ans = "";
        go(0, 0, 1, s);

        cout << "Case #" << ++cases << ": " << ans << "\n";
    }

}
