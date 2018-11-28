#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

inline void flip(string& s, const int k, const int a)
{
    for (int i = a; i < a+k; ++i) {
        s[i] = s[i] == '-' ? '+' : '-';
    }
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    vector<string> S(T);
    vector<int> K(T);
    for (int i = 0; i < T; ++i) {
        cin >> S[i] >> K[i];
    }

    for (int i = 0; i < T; ++i) {
        bool flag = true;
        int ans = 0;
        for (int j = 0; j < S[i].size() - K[i] + 1; ++j) {
            if (S[i][j] == '-') {
                flip(S[i], K[i], j);
                ++ans;
            }
        }
        for (int j = S[i].size() - K[i] + 1; j < S[i].size(); ++j) {
            if (S[i][j] == '-') {
                cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
                flag = false;
                break;
            }
        }
        if (flag) cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
