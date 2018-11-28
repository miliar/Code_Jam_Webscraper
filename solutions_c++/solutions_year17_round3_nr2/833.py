#include <bits/stdc++.h>

#define ll long long

using namespace std;

void solve(int test_number) {
    int ac, aj;
    cin >> ac >> aj;
    vector<pair<int, int>> c(ac), j(aj);
    vector<pair<pair<int, int>, bool>> times;

    int tm_c = 0;
    for (int i=0; i<ac; ++i) {
        cin >> c[i].first >> c[i].second;
        tm_c += (c[i].second - c[i].first + 24*60) % (24*60);
        times.push_back(make_pair(c[i], 0));
    }
    int tm_j = 0;
    for (int i=0; i<aj; ++i) {
        cin >> j[i].first >> j[i].second;
        tm_j += (j[i].second - j[i].first + 24*60) % (24*60);
        times.push_back(make_pair(j[i], 1));
    }

    int ans = 0;
    sort(times.begin(), times.end());
    vector<int> free_cc, free_jj, free_cj;
    for (int ii=0; ii<ac+aj; ++ii) {
        int jj = (ii-1+ac+aj) % (ac+aj);
        if (times[ii].second != times[jj].second) {
            ++ans;
        }
        int rest = (times[ii].first.first - times[jj].first.second + 24*60) % (24*60);
        if (rest > 0) {
            if (times[ii].second == 0) {
                if (times[jj].second == 0) {
                    free_cc.push_back(rest);
                } else {
                    free_cj.push_back(rest);
                }
            } else {
                if (times[jj].second == 1) {
                    free_jj.push_back(rest);
                } else {
                    free_cj.push_back(rest);
                }
            }
        }
    }
    sort(free_cc.begin(), free_cc.end());
    sort(free_jj.begin(), free_jj.end());

    for (int i=0; i<free_cc.size(); ++i) {
        if (tm_c + free_cc[i] > (12*60)) {
            ans += 2*(free_cc.size() - i);
            cout << "Case #" << test_number << ": " << ans << endl;
            return;
        }
        tm_c += free_cc[i];
    }

    for (int i=0; i<free_jj.size(); ++i) {
        if (tm_j + free_jj[i] > (12*60)) {
            ans += 2*(free_jj.size() - i);
            cout << "Case #" << test_number << ": " << ans << endl;
            return;
        }
    }

    cout << "Case #" << test_number << ": " << ans << endl;
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t)
        solve(t);

    return 0;
}
