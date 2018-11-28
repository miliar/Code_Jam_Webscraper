#include <cstdio>
#include <cstring>

int main() {
    int T, S, K;
    char buffer[2000];

    scanf("%d ", &T);

    for (int t = 0; t < T; ++t) {
        scanf("%s %d ", buffer, &K);
        S = strlen(buffer);
        int swap_start = 0;
        int swap_end = 0;
        int nswaps = 0;
        int bad = 0;
        for (int s = 0; s < S - K + 1; ++s) {
            int swapped = (s >= swap_start && s < swap_end);
            if (swapped && buffer[s] == '-') {
                continue;
            }
            if (!swapped && buffer[s] == '+') {
                continue;
            }
            nswaps++;
            if (swap_end > s) {
                swap_start = swap_end;
            } else {
                swap_start = s;
            }
            swap_end = s + K;
        }
        for (int s = S - K + 1; s < S; ++s) {
            int swapped = (s >= swap_start && s < swap_end);
            if (swapped && buffer[s] == '+') {
                bad = 1;
            }
            if (!swapped && buffer[s] == '-') {
                bad = 1;
            }
        }
        if (bad) {
            printf("Case #%d: IMPOSSIBLE\n", t + 1);
        } else {
            printf("Case #%d: %d\n", t + 1, nswaps);
        }
    }
}
