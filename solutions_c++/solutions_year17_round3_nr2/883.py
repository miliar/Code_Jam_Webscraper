#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <cmath>
using namespace std;

int Ac, Aj, C[100], D[100], J[100], K[100], i, j, best;

bool overlap(int A1, int B1, int A2, int B2) {
    static bool q[2881];
    static int i;
    for (i = 0; i <= 2880; i++) q[i] = false;
    for (i = A1; i < B1; i++) {
        q[i] = true;
        q[i + 1440] = true;
    }
    for (i = A2; i < B2; i++) {
        if (q[i] || q[i + 1440]) return true;
    }
    return false;
}

int main() {
    int cases;
    scanf("%d", &cases);
    for (int kejs = 1; kejs <= cases; kejs++) {
        printf("Case #%d: ", kejs);
        scanf("%d%d", &Ac, &Aj);
        for (i = 0; i < Ac; i++) {
            scanf("%d%d", &C[i], &D[i]);
        }
        for (i = 0; i < Aj; i++) {
            scanf("%d%d", &J[i], &K[i]);
        }
        bool change;
        do {
            change = false;
            for (i = 1; i < Ac; i++) {
                if (C[i-1] > C[i]) {
                    swap(C[i-1], C[i]);
                    swap(D[i-1], D[i]);
                    change = true;
                }
            }
            for (i = 1; i < Aj; i++) {
                if (J[i-1] > J[i]) {
                    swap(J[i-1], J[i]);
                    swap(K[i-1], K[i]);
                    change = true;
                }
            }
        } while (change);
        
        for (i = 0; i <= 720; i++) {
            int A1 = i;
            int B1 = A1 + 720;
            int A2 = i + 720;
            int B2 = A2 + 720;
            for (j = 0; j < Ac; j++) {
                if (overlap(A1, B1, C[j], D[j])) break;
            }
            if (j >= Ac) {
                for (j = 0; j < Aj; j++) {
                    if (overlap(A2, B2, J[j], K[j])) break;
                }
                if (j >= Aj) break;
            }
            for (j = 0; j < Ac; j++) {
                if (overlap(A2, B2, C[j], D[j])) break;
            }
            if (j >= Ac) {
                for (j = 0; j < Aj; j++) {
                    if (overlap(A1, B1, J[j], K[j])) break;
                }
                if (j >= Aj) break;
            }
        }
        if (i <= 720) best = 2;
        else best = 4;

        printf("%d\n", best);
    }
    return 0;
}
