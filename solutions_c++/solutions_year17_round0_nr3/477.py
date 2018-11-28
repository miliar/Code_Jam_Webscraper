#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;
#define int long long

#define pb push_back
#define mp make_pair

map<lli, lli> val;

void update(lli val, lli& a, lli& b) {
    b = val / 2;
    a = (val - 1) / 2;
}

#undef int
int main() {
#define int long long

    ifstream cin ("input.txt");
    ofstream cout ("ans.txt");

    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        lli N, K; cin >> N >> K;

        lli amnt = 0, cur = 1;
        val.clear();
        val[N]++;

        while (amnt + cur < K) {

            vector<pair<lli, lli> > cur_val;
            for (auto v : val) {
                lli a = -1, b = -1;
                update(v.first, a, b);
                cur_val.pb(mp(a, v.second));
                cur_val.pb(mp(b, v.second));
            }

            val.clear();
            for (auto c : cur_val) {
                val[c.first] += c.second;
            }

            amnt += cur;
            cur *= 2;
        }

        vector<pair<lli, lli> > cur_val;
        for (auto v : val) {
            cur_val.pb(mp(v.first, v.second));
        }

        cout << "Case #" << t << ": ";
        if (cur_val.size() == 1) {
            cout << cur_val[0].first / 2 << " " << (cur_val[0].first - 1) / 2 << "\n";
        } else {
            lli remain = K - amnt;
            if (cur_val[1].second >= remain) {
                cout << cur_val[1].first / 2 << " " << (cur_val[1].first - 1) / 2 << "\n";
            } else {
                cout << cur_val[0].first / 2 << " " << (cur_val[0].first - 1) / 2 << "\n";
            }
        }
    }

    return 0;
}