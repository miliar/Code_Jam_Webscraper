#include <cstdio>
#include <algorithm>
#include <queue>
#include <cmath>


using namespace std;

const int MAXN = 100;

int a[MAXN+5];

int main() {
//    freopen("A-eg.in", "r", stdin);
//    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
//    freopen("A-eg.out", "w", stdout);
//    freopen("A-small.out", "w", stdout);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int n, p;
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; ++i) {
            scanf("%d", a+i);
        }
        if (p == 2) {
            int zero = 0;
            int one = 0;
            for (int i = 0; i < n; ++i) {
                if (a[i]%2 == 0) {
                    ++zero;
                } else {
                    ++one;
                }
            }
            printf("Case #%d: %d\n", t, zero+one/2+one%2);
        } else if (p == 3) {
            int zero = 0;
            int one = 0;
            int two = 0;
            for (int i = 0; i < n; ++i) {
                if (a[i]%3 == 0) {
                    ++zero;
                } else if (a[i]%3 == 1) {
                    ++one;
                } else {
                    ++two;
                }
            }
            if (one < two) {
                two = two-one;
                int part1 = one+two/3;
                int part2;
                if (two%3 == 0) {
                    part2 = 0;
                } else {
                    part2 = 1;
                }
                printf("Case #%d: %d\n", t, zero+part1+part2);
            } else if (two < one) {
                one = one-two;
                int part1 = two+one/3;
                int part2;
                if (one%3 == 0) {
                    part2 = 0;
                } else {
                    part2 = 1;
                }
                printf("Case #%d: %d\n", t, zero+part1+part2);
            } else {
                printf("Case #%d: %d\n", t, zero+one);
            }
        } else { //p == 4
            int zero = 0;
            int one = 0;
            int two = 0;
            int three = 0;
            for (int i = 0; i < n; ++i) {
                if (a[i]%4 == 0) {
                    ++zero;
                } else if (a[i]%4 == 1) {
                    ++one;
                } else if (a[i]%4 == 2) {
                    ++two;
                } else if (a[i]%4 == 3) {
                    ++three;
                }
            }

            int part1 = two/2;
            two %= 2;
            int part2;
            int part3;
            if (one < three) {
                part2 = one;
                three -= one;
                one = 0;

                if (two == 0) {
                    part3 = three/4 + (three%4 != 0);
                } else {
                    if ((three -= 2) > 0) {
                        part3 = three/4 + (three%4 != 0)+1;
                    } else {
                        part3 = 1;
                    }
                }

                printf("Case #%d: %d\n", t, zero+part1+part2+part3);
            } else if (three < one) {
                part2 = three;
                one -= three;
                three = 0;

                if (two == 0) {
                    part3 = one / 4 + (one % 4 != 0);
                } else {
                    if ((one -= 2) > 0) {
                        part3 = one / 4 + (one % 4 != 0) + 1;
                    } else {
                        part3 = 1;
                    }
                }

                printf("Case #%d: %d\n", t, zero + part1 + part2 + part3);
            } else {
                printf("Case #%d: %d\n", t, zero+part1+one+two);
            }}
    }
    return 0;
}