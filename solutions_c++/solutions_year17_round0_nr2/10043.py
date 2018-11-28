#include <cstdio>
#include <cstring>

int main() {
    int T;
    char N[100];

    scanf("%d ", &T);
    
    for (int t = 1; t < T + 1; ++t) {
        scanf("%s ", N);
        int n = strlen(N);
        char pre_last = '0';
        char last = '0';
        for (int i = 0; i < n; ++i) {
            if (N[i] >= last) {
                pre_last = last;
                last = N[i];
                continue;
            }
            // oops! decreasing.
            int j = i - 1;
            while (j > 0 && N[j] == pre_last) {
                --j;
            }
            N[j] -= 1;
            for (int k = j + 1; k < n; ++k) {
                N[k] = '9';
            }
            break;
        }
        char *answer = N;
        while (*answer == '0') ++answer;
        printf("Case #%d: %s\n", t, answer);
    }
    return 0;
}
