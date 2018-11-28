#include <cstdio>
#include <cstring>

char in[1010];

int main() {
    int T, k;
    scanf("%d", &T);

    for (int times = 0; times < T; times++) {
        scanf("%s%d", in, &k);
        int len = strlen(in);

        int cnt = 0;
        for (int i = 0; i < len-k+1; i++) {
            if (in[i] == '-') {
                cnt += 1;
                for (int j = 0; j < k; j++) {
                    if (in[i+j] == '+') {
                        in[i+j] = '-';
                    } else {
                        in[i+j] = '+';
                    }
                }
            }
        }

        bool check = true;
        for (int j = 0; j < k; j++) {
            if (in[len-k+j] == '-') {
                check = false;
            }
        }

        if (check == false) {
            printf("Case #%d: IMPOSSIBLE\n", times+1);
        } else {
            printf("Case #%d: %d\n", times+1, cnt);
        }
    }
}
