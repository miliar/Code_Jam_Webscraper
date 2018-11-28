// Copyright 2017 Parallelc
#include <bits/stdc++.h>
#include <ext/numeric>
using namespace std;  // NOLINT
using namespace __gnu_cxx;
using LL = int64_t;
const int INF = 0x3f3f3f3f;
const LL mod = 1000000007;

int main() {
    int t;
    cin >> t;
    int k = t;
    while (t--) {
        cout << "Case #" << k - t << ": ";
        string s;
        int k;
        cin >> s >> k;
        vector<int> dir(s.length());
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '-') dir[i] = 1;
            else dir[i] = 0;
        }
        vector<int> f(s.length());
        int res = 0, sum = 0;
        for (int i = 0; i + k <= dir.size(); i++) {
            if ((sum + dir[i]) & 1) {
                res++;
                f[i] = 1;
            }
            sum += f[i];
            if (i - k + 1 >= 0) sum -= f[i - k + 1];
        }
        int flag = 1;
        for (int i = dir.size() - k + 1; i < dir.size(); i++) {
            if ((sum + dir[i]) & 1) {
                flag = 0;
                break;
            }
            if (i - k + 1 >= 0) sum -= f[i - k + 1];
        }
        if (flag) cout << res << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
}
