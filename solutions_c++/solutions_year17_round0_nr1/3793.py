#include <bits/stdc++.h>
using namespace std;

const int MAX = 1005;

int K;
char S[MAX];

int main() {
    freopen("A-output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; testcase++) {
        scanf("%s %d", S, &K);
        int e = strlen(S) - K;
        int ans = 0;
        for (int i = 0; i <= e; i++) {
            if (S[i] == '-') {
                ++ans;
                for (int j = 0; j < K; j++) {
                    S[i + j] = (S[i + j] == '+' ? '-' : '+');
                }
            }
        }

        bool impossible = false;
        for (int i = 0; i < K; i++) {
            if (S[e + i] == '-') {
                impossible = true;
                break;
            }
        }

        if (impossible) {
            printf("Case #%d: IMPOSSIBLE\n", testcase);
        }
        else {
            printf("Case #%d: %d\n", testcase, ans);
        }
    }
}
