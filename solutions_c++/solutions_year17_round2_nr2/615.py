#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    freopen("/Users/vadimantiy/Developer/codejam17/task2/task2/input.txt", "r", stdin);
    freopen("/Users/vadimantiy/Developer/codejam17/task2/task2/output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int caseNumber;
    cin >> caseNumber;
    for (int casen = 0; casen < caseNumber; casen++) {
        cerr << casen << '\n';
        cout << "Case #" << casen + 1 << ": ";
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        vector<pair<int, char> > cnt;
        cnt.push_back(make_pair(R, 'R'));
        cnt.push_back(make_pair(Y, 'Y'));
        cnt.push_back(make_pair(B, 'B'));
        sort(cnt.begin(), cnt.end());
        int a = cnt[0].first, b = cnt[1].first, c = cnt[2].first;
        char aa = cnt[0].second, bb = cnt[1].second, cc = cnt[2].second;
        if (c > a + b) {
            cout << "IMPOSSIBLE" << '\n';
            continue;
        }
        // a + b >= c
        string ans = "";
        for (int i = 0; i < c; i++) {
            ans += cc;
            if (b) {
                ans += bb;
                b--;
            } else {
                ans += aa;
                a--;
            }
        }
        string aaa = "";
        aaa += aa;
        while (a--) {
            int j = 0;
            for (int i = 0; i < ans.length() - 1; i++) {
                if (ans[i] != aa && ans[i + 1] != aa) {
                    j = i;
                    break;
                }
            }
            // insert after j
            ans.insert(j + 1, aaa);
        }
        cout << ans << '\n';
    }
    return 0;
}
