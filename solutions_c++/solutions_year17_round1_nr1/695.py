#include <cstdio>

int main() {
    int T;
    scanf("%d", &T);

    for (int times = 0; times < T; times++) {
        int r, c;
        scanf("%d%d", &r, &c);

        char in[26][26];
        for (int i = 0; i < r; i++) {
            scanf("%s", in[i]);
        }

        int fr = -1;
        int cr = -1;
        for (int i = 0; i < r; i++) {
            bool all = true;
            for (int j = 0; j < c; j++) {
                if (in[i][j] != '?') {
                    all = false;
                }
            }

            if (all == true) {
                for (int j = 0; j < c; j++) {
                    in[i][j] = in[cr][j];
                }
            } else {
                if (fr == -1) {
                    fr = i;
                }

                int fc = -1;
                int cc = -1;
                for (int j = 0; j < c; j++) {
                    if (in[i][j] == '?') {
                        if (c != -1) {
                            in[i][j] = in[i][cc];
                        }
                    } else {
                        if (fc == -1) {
                            fc = j;
                        }
                        cc = j;
                    }
                }

                for (int j = 0; j < fc; j++) {
                    in[i][j] = in[i][fc];
                }
                cr = i;
            }

            for (int i = 0; i < fr; i++) {
                for (int j = 0; j < c; j++) {
                    in[i][j] = in[fr][j]; 
                }
            }
        }
        
        printf("Case #%d:\n", times+1);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                printf("%c", in[i][j]);
            }
            puts("");
        }
    }
}
