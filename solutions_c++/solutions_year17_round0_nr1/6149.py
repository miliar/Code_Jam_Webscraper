#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

int tests, K, N;
string s;

int getFlips() {
    int result = 0;
    for (int i = 0; i < N; i++) {
        if (s[i] == '-') {
            if (i + K > N) {
                return -1;
            }
            result++;
            for (int j = i; j < i + K; j++) {
                s[j] = (s[j] == '-') ? '+' : '-';
            }
        }
    }

    return result;
}

int main() {
    freopen("oversizePancake.in", "r", stdin);
    freopen("oversizePancake.out", "w", stdout);

    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        printf("Case #%d: ", test);

        cin >> s >> K;
        N = s.size();

        int result = getFlips();
        if (result == -1) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", result);
        }
    }
    return 0;
}