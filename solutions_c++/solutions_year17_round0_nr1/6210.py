#include <iostream>
#include <string>

using namespace std;

typedef unsigned int uint;

int solve() {
    string s;
    int k;
    cin >> s >> k;
    int result = 0;
    for (uint i = 0; i < s.length() - k + 1; i++) {
        if (s[i] == '-') {
            result++;
            for (int j = 0; j < k; j++) {
                s[i + j] = s[i + j] == '-' ? '+' : '-';
            }
        }
    }
    for (auto c : s) {
        if (c == '-') {
            return -1;
        }
    }
    return result;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        auto result = solve();
        if (result == -1) {
            printf("Case #%d: IMPOSSIBLE\n", i + 1);
        } else {
            printf("Case #%d: %d\n", i + 1, result);
        }
    }
}
