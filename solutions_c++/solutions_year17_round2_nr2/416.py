#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;

void putr(int& r, int& g) {
    if (r != 0) {
        printf("R");
        r--;
    } else {
        printf("RGR");
        g--;
    }
}

void puty(int& y, int& v) {
    if (y != 0) {
        printf("Y");
        y--;
    } else {
        printf("YVY");
        v--;
    }
}

void putb(int& b, int& o) {
    if (b != 0) {
        printf("B");
        b--;
    } else {
        printf("BOB");
        o--;
    }
}



int main() {
    int t, cas = 0;
    int r, o, y, g, b, v, n;
    scanf("%d", &t);
    while (t--) {
        cas++;
        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
        r -= 2 * g;
        y -= 2 * v;
        b -= 2 * o;
        if (r < 0 || y < 0 || b < 0) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
            continue;
        }
        int nn = r + o + y + g + b + v;
        if (nn < (r + g) * 2) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
            continue;
        }
        if (nn < (y + v) * 2) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
            continue;
        }
        if (nn < (b + o) * 2) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
            continue;
        }
        printf("Case #%d: ", cas);

        int first = 0;
        int last = 0;
        if (r + g != 0) {
            putr(r, g);
            last = 1;
            nn--;
            first = 1;
        } else if (y + v != 0) {
            puty(y, v);
            last = 2;
            first = 2;
            nn--;
        } else {
            first = 3;
        }
        while(true) {
            if (nn == 0) {
                break;
            }
            if (last != 1 && (last == 2 || r + g >= y + v) && (last == 3 ||r + g >= b + o)) {
                last = 1;
                putr(r, g);
            } else if (last != 2 && (last == 1 || y + v >= r + g) && (last == 3 ||y + v >= b + o)) {
                last = 2;
                puty(y, v);
            } else if (last != 3 && (last == 1 || b + o >= r + g) && (last == 2 || b + o >= y + v)) {
                last = 3;
                putb(b, o);
            } else {
                fprintf(stderr, "err");
            }
            nn--;
        }
        puts("");
        if (first == last) {
            fprintf(stderr, "err : %d\n", cas);
        }
    }
    return 0;
}
