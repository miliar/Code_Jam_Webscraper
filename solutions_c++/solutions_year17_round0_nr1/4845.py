#include <iostream>
#include <string>

using namespace std;

char toggle(char in) {
    if (in == '+') return '-';
    if (in == '-') return '+';
    return 0;
}

void flip(string &S, int offset, int length) {
    for (int i = offset; i < offset + length; i++)
        S[i] = toggle(S[i]);
}

int solve() {
    string S;
    int K;
    cin >> S >> K;

    int tot = 0;

    for (int i = 0; i < S.length() - K + 1; i++) {
        if (S[i] == '-') {
            flip(S, i, K);
            tot++;
        }
    }
    for (char i : S)
        if (i != '+')
            return -1;
    return tot;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int result = solve();
        cout << "Case #" << i+1 << ": ";
        if (result == -1) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << result << "\n";
        }
    }
}
