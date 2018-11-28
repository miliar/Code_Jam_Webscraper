#include <cstdio>
#include <algorithm>

int r[5];

int main() {
    int T;
    scanf("%d", &T);
    int a;
    for (int t = 1; t <= T; t++) {
        int N, P;
        scanf("%d%d", &N, &P);
        for (int i = 0; i < P; i++)
            r[i] = 0;
        for (int i = 0; i < N; i++) {
            scanf("%d", &a);
            r[a%P]++;
        }
        int ile = 0;
        if (P == 2) {
            ile += r[0];
            ile += (r[1] + 1) / 2;
        } else if (P == 3) {
            ile += r[0];
            int mini = std::min(r[1], r[2]);
            ile += mini;
            r[1] -= mini;
            r[2] -= mini;
            ile += (r[1] + 2) / 3;
            ile += (r[2] + 2) / 3;
        } else {
            ile += r[0];
            ile += r[2] / 2;
            r[2] %= 2;
            int mini = std::min(r[1], r[3]);
            r[1] -= mini;
            r[3] -= mini;
            ile += mini;
            if (r[2] == 1) {
                bool k = false;
                if (r[3] >= 2) {
                    ile++;
                    r[2]--;
                    r[3] -= 2;
                    k = true;
                    ile += (r[3] + 3) / 4;
                }
                if (r[1] >= 2) {
                    ile++;
                    k = true;
                    r[2]--;
                    r[1] -= 2;
                    ile += (r[1] + 3) / 4;
                }
                if (!k) {
                    ile++;
                }
            } else {
                ile += (r[3] + 3) / 4;
                ile += (r[1] + 3) / 4;
            }
        }
        printf("Case #%d: %d\n", t, ile);
    }
    return 0;
}