#include <bits/stdc++.h>
using namespace std;

const char letterz[] = "ROYGBV";
const int maxN = 1024;
char t[maxN];

void prog() {
    int A, B, C, N;
    int a, b, c;
    char cA = 'R', cc = 'O', cB = 'Y', ca = 'G', cC = 'B', cb = 'V';
    scanf("%d%d%d%d%d%d%d", &N, &A, &c, &B, &a, &C, &b);
    A -= a;
    B -= b;
    C -= c;
    if(min(min(A, B), C) < 0) {
        printf("IMPOSSIBLE\n");
        return;
    }
    int n = A + B + C;
    if(A < B) { swap(A, B); swap(a, b); swap(cA, cB); swap(ca, cb); }
    if(B < C) { swap(C, B); swap(c, b); swap(cC, cB); swap(cc, cb); }
    if(A < B) { swap(A, B); swap(a, b); swap(cA, cB); swap(ca, cb); }

    if(A > n / 2) {
        printf("IMPOSSIBLE\n");
        return;
    }

    // cases....
    if(B && !C) {
        if(c) {
            printf("IMPOSSIBLE\n");
            return;
        }
    } else if(A && !B) {
        if(b|c) {
            printf("IMPOSSIBLE\n");
            return;
        }
    } else if(!A) {
        if(a < b) { swap(A, B); swap(a, b); swap(cA, cB); swap(ca, cb); }
        if(b < c) { swap(C, B); swap(c, b); swap(cC, cB); swap(cc, cb); }
        if(a < b) { swap(A, B); swap(a, b); swap(cA, cB); swap(ca, cb); }
        if(b|c) {
            printf("IMPOSSIBLE\n");
            return;
        }
        while(a) {
            printf("%c%c", cA, ca);
            a--;
        }
        puts("");
        return;
    }
    
    // normal situation
    t[n] = '\0';
    for(int i = 0; i < A; ++i) t[2 * i] = cA;
    for(int i = 2 * A; i < n; i += 2) {
        t[i] = cB;
        B--;
    }
    for(int i = 0; i < B; ++i) t[2 * i + 1] = cB;
    for(int i = 0; i < C; ++i) t[2 * (i + B) + 1] = cC;
    
    for(int i = 0; i < n; ++i) {
        printf("%c", t[i]);
        while(a && t[i] == cA) {
            printf("%c%c", ca, cA);
            a--;
        }
        while(b && t[i] == cB) {
            printf("%c%c", cb, cB);
            b--;
        }
        while(c && t[i] == cC) {
            printf("%c%c", cc, cC);
            c--;
        }
    }
    puts("");
}

int main() {
    int _t;
    scanf("%d", &_t);
    for(int i = 1; i <= _t; ++i) {
        printf("Case #%d: ", i);
        fprintf(stderr, "test %d... ", i);
        prog();
        fprintf(stderr, "OK\n");
    }
}