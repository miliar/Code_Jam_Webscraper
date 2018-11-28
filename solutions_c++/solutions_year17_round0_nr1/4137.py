#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

const int MAXN = 1010;

int T, K, N;
char pancakes[MAXN];

void flip(int i) {
    pancakes[i] = pancakes[i] == '+' ? '-' : '+';
}

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%s %d", pancakes, &K);
        N = strlen(pancakes);

        bool good = true;
        int flips = 0;
        for (int i = 0; i < N; ++i) {
            if (pancakes[i] != '+') {
                if (i <= N - K) {
                    flips++;
                    for (int j = i; j < i + K; ++j) {
                        flip(j);
                    }
                } else {
                    good = false;
                    break;
                }
            }
        }
        if (good) printf("Case #%d: %d\n", t, flips);
        else printf("Case #%d: IMPOSSIBLE\n", t);
    }

    return 0;
}
