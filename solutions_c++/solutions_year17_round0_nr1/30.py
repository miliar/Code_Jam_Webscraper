#include <string>
#include <iostream>
using namespace std;

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    ios::sync_with_stdio(0);

    int T;
    cin >> T;
    for (int __ = 1; __ <= T; ++__) {
        string s;
        int K;
        int answer = 0;

        cin >> s >> K;
        for (int i = 0; i + K <= (int)s.length(); ++i) {
            if (s[i] == '-') {
                ++answer;
                for (int j = 0; j < K; ++j) {
                    s[i + j] = '+' + '-' - s[i + j];
                }
            }
        }

        cout << "Case #" << __ << ": ";
        if (s.find('-') != string::npos) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << answer << "\n";
        }

    }

    return 0;
}
