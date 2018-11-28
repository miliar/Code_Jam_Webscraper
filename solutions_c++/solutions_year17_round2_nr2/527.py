#include <bits/stdc++.h>
using namespace std;

const int maxn = 101;
const long long INF = 1E18;

int No() {
    cout << "IMPOSSIBLE\n";
    return 0;
}

void push(string& ans, map<char, int>& cnt, char x, char y) {
    while(cnt[x] > 0 && cnt[y] > 0) {
        ans += x;
        ans += y;
        cnt[x]--;
        cnt[y]--;
    }
    if (!ans.empty() && ans.back() == x && cnt[y] > 0) {
        ans += y;
        cnt[y]--;
    }
}

int solve() {
    map<char, int> cnt;
    int n;
    cin >> n >> cnt['R'] >>
                cnt['O'] >>
                cnt['Y'] >>
                cnt['G'] >>
                cnt['B'] >>
                cnt['V'];

    string ans;
    push(ans, cnt, 'O', 'B');
    push(ans, cnt, 'G', 'R');
    push(ans, cnt, 'V', 'Y');
    if (cnt['O'] || cnt['G'] || cnt['V'])
        return No();

    while(cnt['B'] || cnt['R'] || cnt['Y']) {
        if (cnt['B'] + cnt['R'] + cnt['Y'] > 8) {
            vector<pair<int, char>> prs;
            prs.push_back(make_pair(cnt['B'], 'B'));
            prs.push_back(make_pair(cnt['R'], 'R'));
            prs.push_back(make_pair(cnt['Y'], 'Y'));
            sort(prs.begin(), prs.end());
            reverse(prs.begin(), prs.end());

            if (!ans.empty() && ans.back() != prs[0].second) {
                ans += prs[0].second;
                cnt[prs[0].second]--;
            }
            else {
                char cl = prs[1].second;
                ans += cl;
                cnt[prs[1].second]--;
                if (cnt[cl] == -1)
                    return No();
            }
        }
        else {
            int lft = cnt['B'] + cnt['R'] + cnt['Y'];
            map<char, int> mem = cnt;

            int mask_size = 1;
            for (int i = 0; i < lft; i++)
                mask_size *= 3;

            bool found = false;
            for (int mask = 0; mask < mask_size; mask++) {
                cnt = mem;
                int ms = mask;
                bool bad = false;
                char last = ans.empty() ? 'B' : ans.back();
                char fs = ans.empty() ? '#' : ans[0];

                for (int i = 0; i < lft; i++) {
                    char cl = ((ms % 3 == 0) ? 'B' : ((ms % 3 == 1) ? 'R' : 'Y'));
                    if (fs == '#') fs = cl;
                    if (last == cl || cnt[cl] == 0) {
                        bad = true;
                        break;
                    }
                    last = cl;
                    cnt[cl]--;
                    ms /= 3;
                }
                if (last == fs)
                    bad = true;

                if (bad)
                    continue;

                cnt = mem;
                ms = mask;
                last = ans.empty() ? 'B' : ans.back();
                for (int i = 0; i < lft; i++) {
                    char cl = ((ms % 3 == 0) ? 'B' : ((ms % 3 == 1) ? 'R' : 'Y'));
                    last = cl;
                    ans += cl;
                    cnt[cl]--;
                    ms /= 3;
                }
                found = true;
                break;
            }
            if (!found)
                return No();
            else {
                cout << ans << endl;
                return 0;
            }
        }
    }
    cout << ans << endl;
}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        //return 0;
    }
    return 0;
}
