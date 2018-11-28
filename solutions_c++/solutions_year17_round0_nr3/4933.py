#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        int n, k;
        cin >> n >> k;
        multiset<int> s = { n };
        int ansMn, ansMx;
        for (int i = 0; i < k; i++) {
            auto it = s.end();
            --it;
            int cur = *it - 1;
            s.erase(it);
            ansMn = cur/2;
            ansMx = cur - cur/2;
            s.insert(ansMn);
            s.insert(ansMx);
        }

        cout << "Case #" << i << ": " << ansMx << " " << ansMn << endl;
    }
}
