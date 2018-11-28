#include <iostream>
#include <string>

using namespace std;

void flip(string& s, int p, int k) {
    for (int i = 0; i < k; ++i)
        s[p+i] = s[p+i] == '+' ? '-' : '+';
}

int solve(string s, int k) {
    string expected(s.size(), '+');

    int cnt = 0;
    for (int i = 0; i <= s.size() - k; ++i) {
        if (s[i] == '-') {
            flip(s, i, k);
            cnt++;
        }
    }

    if (s == expected)
        return cnt;
    return -1;
}

int main() {
    int T;
    cin >> T;

    for (int kase = 1; kase <= T; ++kase) {
        string s;
        int k;
        cin >> s;
        cin >> k;

        int answer = solve(s, k);

        printf("Case #%d: %s\n", kase, answer >=0 ? to_string(answer).data() :  "IMPOSSIBLE");
    }

    return 0;
}
