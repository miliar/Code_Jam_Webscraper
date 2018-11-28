#include <iostream>

using namespace std;

const static int IMPOSSIBLE = -1;

int solve(string s, int K) {
    int start = 0, ans = 0;
    while(start < s.length()) {
        size_t x = s.find('-');
        if (x == string::npos) {
            return ans;
        }
        s = s.substr(x);
        for (int i = 0; i < K; ++i) {
            if (i >= s.length()) return IMPOSSIBLE;
            s[i] = s[i]=='-'?'+':'-';
        }
        ans++;
    }
    return ans;
}

int main(int argn, char* argv[]) {
    freopen("/Users/jorgemoag/Downloads/A-large.in.txt", "r", stdin);
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s; int K; cin >> s >> K;
        int ans = solve(s, K);
        if (ans == IMPOSSIBLE) {
            printf("Case #%d: IMPOSSIBLE\n", t);
        } else {
            printf("Case #%d: %d\n", t, ans);
        }
    }
}
