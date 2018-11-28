#include <stdio.h>

int main() {
    int T;
    int Ac, Aj;
    int C[2], D[2], J[2], K[2];
    int i, j, t;
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &T);
    for(i = 0; i < T; i++) {
        scanf("%d %d", &Ac, &Aj);
        printf("Case #%d: ", i + 1);
        for(j = 0; j < Ac; j++) scanf("%d %d", &C[j], &D[j]);
        for(j = 0; j < Aj; j++) scanf("%d %d", &J[j], &K[j]);
        if(Ac + Aj == 1) printf("2\n");
        else if(Ac == 1) printf("2\n");
        else {
            if(Ac == 2) {
                J[0] = C[1];
                K[0] = D[1];
            }
            else {
                C[0] = J[1];
                D[0] = K[1];
            }
            if(C[0] > J[0]) {
                t = C[0];
                C[0] = J[0];
                J[0] = t;
                t = D[0];
                D[0] = K[0];
                K[0] = t;
            }
            if(K[0] - C[0] <= 720 || J[0] - D[0] >= 720) printf("2\n");
            else printf("4\n");
        }
    }
    return 0;
}
