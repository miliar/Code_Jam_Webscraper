#include <stdio.h>
char s[4], ss[4];
int c[4], cc[4];

int main() {
    int tn;
    scanf("%d", &tn);
    for (int cn = 1; cn <= tn; cn++) {
        int n, r, o, y, g, b, v;
        scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
        printf("Case #%d: ", cn);

        if (o > b || g > r || v > y) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        if (o > 0 && o == b) {
            if (o + b == n) {
                for (int i = 0; i < n / 2; i++) {
                    printf("OB");
                }
            } else {
                printf("IMPOSSIBLE");
            }
            printf("\n");
            continue;
        }
        if (g > 0 && g == r) {
            if (g + r == n) {
                for (int i = 0; i < n / 2; i++) {
                    printf("GR");
                }
            } else {
                printf("IMPOSSIBLE");
            }
            printf("\n");
            continue;
        }
        if (v > 0 && v == y) {
            if (v + y == n) {
                for (int i = 0; i < n / 2; i++) {
                    printf("VY");
                }
            } else {
                printf("IMPOSSIBLE");
            }
            printf("\n");
            continue;
        }

        y -= v, r -= g, b -= o;

        if (r >= y && r >= b) {
            s[0] = 'R', c[0] = r;
            if (y >= b) {
                s[1] = 'Y', c[1] = y;
                s[2] = 'B', c[2] = b;
            } else {
                s[1] = 'B', c[1] = b;
                s[2] = 'Y', c[2] = y;
            }
        } else if (y >= r && y >= b) {
            s[0] = 'Y', c[0] = y;
            if (r >= b) {
                s[1] = 'R', c[1] = r;
                s[2] = 'B', c[2] = b;
            } else {
                s[1] = 'B', c[1] = b;
                s[2] = 'R', c[2] = r;
            }
        } else if (b >= r && b >= y) {
            s[0] = 'B', c[0] = b;
            if (r >= y) {
                s[1] = 'R', c[1] = r;
                s[2] = 'Y', c[2] = y;
            } else {
                s[1] = 'Y', c[1] = y;
                s[2] = 'R', c[2] = r;
            }
        }
        if (c[0] > c[1] + c[2]) {
            printf("IMPOSSIBLE");
        } else {
            bool first0 = false;
            bool first1 = false;
            bool first2 = false;
            for (int i = 1; i <= c[0]; i++) {
                printf("%c", s[0]);
                    
                if (!first0) {
                    first0 = true;
                    if (s[0] == 'B' && o > 0) {
                        for (int j = 0; j < o; j++) {
                            printf("OB");
                        }
                    }
                    else if (s[0] == 'R' && g > 0) {
                        for (int j = 0; j < g; j++) {
                            printf("GR");
                        }
                    }
                    else if (s[0] == 'Y' && v > 0) {
                        for (int j = 0; j < v; j++) {
                            printf("VY");
                        }
                    }
                }


                if (c[1] >= i) {
                    printf("%c", s[1]);

                    if (!first1) {
                        first1 = true;
                        if (s[1] == 'B' && o > 0) {
                            for (int j = 0; j < o; j++) {
                                printf("OB");
                            }
                        }
                        else if (s[1] == 'R' && g > 0) {
                            for (int j = 0; j < g; j++) {
                                printf("GR");
                            }
                        }
                        else if (s[1] == 'Y' && v > 0) {
                            for (int j = 0; j < v; j++) {
                                printf("VY");
                            }
                        }
                    }


                    if (c[2] - (c[0] - c[1]) >= i) {
                        printf("%c", s[2]);

                        if (!first2) {
                            first2 = true;
                            if (s[2] == 'B' && o > 0) {
                                for (int j = 0; j < o; j++) {
                                    printf("OB");
                                }
                            }
                            else if (s[2] == 'R' && g > 0) {
                                for (int j = 0; j < g; j++) {
                                    printf("GR");
                                }
                            }
                            else if (s[2] == 'Y' && v > 0) {
                                for (int j = 0; j < v; j++) {
                                    printf("VY");
                                }
                            }
                        }

                    }
                } else {
                    printf("%c", s[2]);

                    if (!first2) {
                        first2 = true;
                        if (s[2] == 'B' && o > 0) {
                            for (int j = 0; j < o; j++) {
                                printf("OB");
                            }
                        }
                        else if (s[2] == 'R' && g > 0) {
                            for (int j = 0; j < g; j++) {
                                printf("GR");
                            }
                        }
                        else if (s[2] == 'Y' && v > 0) {
                            for (int j = 0; j < v; j++) {
                                printf("VY");
                            }
                        }
                    }
                }
            }
        }
        printf("\n");
    }
    return 0;
}
