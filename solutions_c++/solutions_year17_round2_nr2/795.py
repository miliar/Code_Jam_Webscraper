#include <bits/stdc++.h>

using namespace std;

int main() {

    // freopen("B-large.in", "r", stdin);
    // freopen("B-large.out", "w", stdout);

    int T, k = 0, N, C[6], D[6], i, j, c, ok, l, ll[3], m;
    char S[1010], SS[3][1010], L[7] = "RBYGOV";

    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++k);
        scanf("%d", &N);
        memset(C, 0, sizeof(C));
        c = 0;
        for(i=0;i<6;i++) {
            if (i == 1 || i == 4) j = 5 - i;
            else j = i;
            scanf("%d", &C[j]);
            D[j] = C[j];
            if (C[j] != 0) c++;
        }
        memset(ll, 0, sizeof(ll));
        ok = 1;
        l = 0;
        for(i=0;i<3&&ok;i++) {
            if (D[i+3] != 0) {
                if (c == 2) {
                    if (D[i] >= D[i+3]) {
                        D[i] -= D[i+3] - 1;
                        while(D[i+3]--) {
                            SS[i][ll[i]++] = L[i+3];
                            SS[i][ll[i]++] = L[i];
                        }
                    } else ok = 0;
                } else {
                    if (D[i] >= D[i+3]+1) {
                        SS[i][ll[i]++] = L[i];
                        D[i] -= D[i+3];
                        while(D[i+3]--) {
                            SS[i][ll[i]++] = L[i+3];
                            SS[i][ll[i]++] = L[i];
                        }
                    } else ok = 0;
                }
            }
        }
        if (!ok) {
            puts("IMPOSSIBLE");
            continue;
        }
        c = 0;
        for(i=0;i<3;i++) if (D[i] != 0) c++;
        if (c == 1) {
            for(i=0;i<3;i++) {
                if (D[i] == 1) {
                    if (ll[i] > 0) {
                        SS[i][ll[i]] = '\0';
                        puts(SS[i]);
                    } else {
                        printf("%c\n", L[i]);
                    }
                    break;
                } else if (D[i] > 1) {
                    puts("IMPOSSIBLE");
                    break;
                }
            }
        } else if (c == 2) {
            for(i=0;i<3;i++) {
                if (D[i] != 0) {
                    for(j=i+1;j<3;j++) {
                        if (D[j] != 0) {
                            if (D[i] == D[j]) {
                                if (ll[i] > 0) {
                                    SS[i][ll[i]] = '\0';
                                    printf("%s", SS[i]);
                                } else {
                                    printf("%c", L[i]);
                                }
                                if (ll[j] > 0) {
                                    SS[j][ll[j]] = '\0';
                                    printf("%s", SS[j]);
                                } else {
                                    printf("%c", L[j]);
                                }
                                D[i]--;
                                while(D[i]--) {
                                    putchar(L[i]); putchar(L[j]);
                                }
                                D[i] = 0;
                                putchar('\n');
                            } else {
                                puts("IMPOSSIBLE");
                            }
                        }
                    }
                }
            }
        } else {
            for(i=0;i<3;i++) {
                j = (3+i-1)%3;
                m = (i+1)%3;
                if (D[i] >= D[j] && D[i] >= D[m]) {
                    if (D[i] > D[m] + D[j]) {
                        puts("IMPOSSIBLE");
                    } else {
                        while(D[i]) {
                            if (ll[i] > 0) {
                                SS[i][ll[i]] = '\0';
                                printf("%s", SS[i]);
                                ll[i] = 0;
                            } else {
                                printf("%c", L[i]);
                            }
                            if (D[j]) {
                                if (ll[j] > 0) {
                                    SS[j][ll[j]] = '\0';
                                    printf("%s", SS[j]);
                                    ll[j] = 0;
                                } else {
                                    printf("%c", L[j]);
                                }
                            } else {
                                if (ll[m] > 0) {
                                    SS[m][ll[m]] = '\0';
                                    printf("%s", SS[m]);
                                    ll[m] = 0;
                                } else {
                                    printf("%c", L[m]);
                                }
                            }
                            if (D[j] && D[m] && D[j] + D[m] > D[i]) {
                                if (ll[m] > 0) {
                                    SS[m][ll[m]] = '\0';
                                    printf("%s", SS[m]);
                                    ll[m] = 0;
                                } else {
                                    printf("%c", L[m]);
                                }
                                D[m]--;
                            }
                            D[i]--;
                            if (D[j]) D[j]--;
                            else D[m]--;
                        }
                        puts("");
                    }
                    break;
                }
            }
        }
    }

    return 0;
}
