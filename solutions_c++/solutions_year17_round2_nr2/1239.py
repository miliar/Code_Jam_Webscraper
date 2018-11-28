#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++cas) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        int ma = max(max(r, y), b);
        int num[3] = {r, y, b};
        string color = "RYB";
        string ans;
        if (ma > n - ma) {
            ans = "IMPOSSIBLE";
        } else {
            string s = "";
            int k = 0;
            for (int i = 1; i < 3; ++i) {
                if (num[i] > num[k]) k = i;
            }
            s += color[k];
            num[k]--;
            for (int pre = k, i = 1; i < n; ++i) {
                int x = -1;
                for (int j = 0; j < 3; ++j) {
                    if (j == pre || num[j] == 0) continue;
                    if (x == -1 || num[j] > num[x]) x = j;
                }
                if (k != pre && num[x] == num[k]) x = k;
                s += color[x];
                num[x]--;
                pre = x;
            }
            ans = s;
        }
        cout << "Case #" << cas << ": " << ans << '\n';
    }
}
