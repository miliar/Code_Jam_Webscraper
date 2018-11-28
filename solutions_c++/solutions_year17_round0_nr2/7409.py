#include <bits/stdc++.h>

using namespace std;

int tc, n;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> n;
        for (int i = n; i >= 1; i--) {
            vector<int> dig;
            int ii = i;
            while (ii) {
                dig.push_back(ii % 10);
                ii /= 10;
            }
            bool flag = 0;
            for (int i = 0; i < dig.size() - 1; i++) {
                if (dig[i] < dig[i + 1]) {
                    flag = 1;
                    break;
                }
            }
            if (!flag) {
                cout << i << "\n";
                break;
            }
        }
    }
}
