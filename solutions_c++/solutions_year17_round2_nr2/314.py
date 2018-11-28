#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

const int MAXN = 1010;

int T, N, R, O, Y, G, B, V;

pair<char, char> split(char a) {
    switch (a) {
        case 'R': return make_pair('R', 'R');
        case 'Y': return make_pair('Y', 'Y');
        case 'B': return make_pair('B', 'B');
        case 'O': return make_pair('R', 'Y');
        case 'G': return make_pair('Y', 'B');
        case 'V': return make_pair('R', 'B');
        default: assert(false);
    }
}

bool can(char a, char b) {
    pair<char, char> ha = split(a);
    pair<char, char> hb = split(b);
    if (ha.first == hb.first ||
        ha.first == hb.second ||
        ha.second == hb.first ||
        ha.second == hb.second) {
        return false;
    } else {
        return true;
    }
}

void impossible() {
    printf("IMPOSSIBLE\n");
}

void work(char a, int na, char b, int nb, char c, int nc) {
    int extrac = nb + nc - na;
    nc -= extrac;
    for (int i = 0; i < na; ++i) {
        printf("%c", a);
        if (nb > 0) {
            printf("%c", b);
            nb--;
        } else {
            printf("%c", c);
            nc--;
        }
        if (extrac > 0) {
            printf("%c", c);
            extrac--;
        }
    }
    printf("\n");
}

int main() {
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {
        scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

        printf("Case #%d: ", t);
        // small: R, B, Y
        if (R >= B && R >= Y) {
            if (R > B + Y) {
                impossible();
            } else {
                work('R', R, 'B', B, 'Y', Y);
            }
        } else if (B >= R && B >= Y) {
            if (B > R + Y) {
                impossible();
            } else {
                work('B', B, 'R', R, 'Y', Y);
            }
        } else {
            if (Y > R + B) {
                impossible();
            } else {
                work('Y', Y, 'R', R, 'B', B);
            }
        }
    }

    return 0;
}
