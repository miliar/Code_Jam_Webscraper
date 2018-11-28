#include <stdio.h>

int T;
double res;
int N, K;
double U;
double P[201];

int main(){
    scanf("%d",&T);
    for (int t = 1; t <= T; t++){
        scanf("%d %d",&N, &K);
        scanf("%lf", &U);
        for (int i = 0; i < N; i++){
            scanf("%lf", &P[i]);
        }
        for (int i = 0; i <N; i++){
            for (int j = i+1; j <N; j++){
                if (P[i] > P[j]){
                    double p = P[i];
                    P[i] = P[j];
                    P[j] = p;
                }
            }
        }
        for (int i = 0; i < N-1; i++){
            if (U >= (P[i+1]-P[i])*(i+1)){
                U -= (P[i+1]-P[i])*(i+1);
                for (int j = 0; j <= i; j++){
                    P[j] = P[i+1];
                }
            } else {
                U /= (i+1);
                for (int j = 0; j <= i; j++){
                    P[j] += U;
                }
                U = 0;
                break;
            }
        }
        if (U > 0){
            U /= N;
            for (int i = 0; i < N; i++){
                P[i] += U;
            }
        }
        res = 1;
        for (int i = 0; i < N; i++){
            res *= P[i];
        }
        if (res > 1)
            res = 1;
        printf("Case #%d: %lf\n", t, res);
    }
    return 0;
}
