#include <stdio.h>
#define PIE 3.141592653589793

long long res;
long long last_top;
int T;
int N, K;

struct cake_t{
    long long R;
    long long H;
};
cake_t cakes[1001];

int main(){
    scanf("%d",&T);
    for (int t = 1; t <= T; t++){
        scanf("%d %d",&N, &K);
        for (int i = 0; i < N; i++){
            scanf("%lld %lld",&cakes[i].R, &cakes[i].H);
        }
        for (int i = 0; i < N; i++){
            for (int j = i; j < N; j++){
                if (cakes[i].R*(2 * cakes[i].H) < cakes[j].R * (2 * cakes[j].H)){
                    cake_t swp = cakes[i];
                    cakes[i] = cakes[j];
                    cakes[j] = swp;
                }
            }
        }
        res = 0;
        long long max = 0;
        long long max2 = 0;
        for (int i = 0; i < K-1; i++){
            res += 2 * cakes[i].R * cakes[i].H;
            if (max < cakes[i].R * cakes[i].R)
                max = cakes[i].R * cakes[i].R;
        }
        max2 = res + max;
        for (int i = K-1; i < N; i++){
            if (cakes[i].R * cakes[i].R > max){
                if (max2 < res + cakes[i].R *( cakes[i].R + 2 * cakes[i].H)){
                    max2 = res + cakes[i].R *( cakes[i].R + 2 * cakes[i].H);
                }
            }
            else{
                if (max2 < res + max + cakes[i].R * 2 * cakes[i].H){
                    max2 = res + max + cakes[i].R * 2 * cakes[i].H;
                }
            }
        }
        printf("Case #%d: %lf\n", t, max2 * PIE);
    }
    return 0;
}
