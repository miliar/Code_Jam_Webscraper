#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int n;
    int r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    if (max({r, y, b}) > n / 2) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    pair<char, int> chs[3] = { {'R', r}, {'Y', y}, {'B', b} };
    sort(chs, chs + 3, [](pair<char, int> a, pair<char, int> b) { return a.second > b.second; });
    string ans;
    ans.resize(n);
    int maxi = 0;
    for (int i = 0; i < chs[0].second; i++) {
        ans[2 * i] = chs[0].first;
        maxi = 2 * i;
    }
    for (int i = maxi + 2; i < ans.size(); i++) {
        int curc = i % 2 + 1;
        ans[i] = chs[curc].first;
        chs[curc].second--;
    }
    for (int i = 0; i < chs[0].second; i++) {
        if (chs[1].second > 0) {
            ans[2 * i + 1] = chs[1].first;
            chs[1].second--;
        } else {
            ans[2 * i + 1] = chs[2].first;
            chs[2].second--;
        }
    }
    cout << ans << endl;
}

int main() {
    int cntTests;
    cin >> cntTests;
    for (int curTest = 0; curTest < cntTests; curTest++) {
        cout << "Case #" << curTest + 1 << ": ";
        solve();
    }
}