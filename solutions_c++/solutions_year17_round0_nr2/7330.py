#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define scanf nope
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

vector<int> lim;

map<tuple<int, int, bool>, string> dp;

string itoa(int i) {
        stringstream ss;
        ss << i;
        return ss.str();
}

string go(int at, int last, bool follows) {
        if (at == sz(lim)) return "";
        string mx = "-1";
        auto key = make_tuple(at, last, follows);
        auto it = dp.find(key);
        if (it != dp.end()) return it->second;

        int thelim = 9;
        if (follows) thelim = lim[at];
        for (int i = last; i <= thelim; i++) {
                string sub = go(at + 1, i, follows && i == thelim);
                if (sub != "-1") mx = itoa(i) + sub;
        }
        return dp[key] = mx;
}

void solve() {
        ll N;
        cin >> N;
        lim.clear();
        dp.clear();
        while(N) {
                lim.push_back(int(N % 10));
                N /= 10;
        }
        reverse(all(lim));

        string ans = go(0, 0, true);
        while (ans[0] == '0') ans = ans.substr(1);
        cout << ans << endl;
}

int main() {
        int N;
        cin >> N;
        rep(i,1,N+1) {
                cout << "Case #" << i << ": ";
                solve();
        }
}
