#include<cstdio>
#include<algorithm>

using namespace std;
bool cmp(double lhs, double rhs) {
    return lhs < rhs;
}

int main() {
    int T;
    int N, K;
    double U;
    double core[60];

    scanf("%d", &T);
    int cnt = 0;

    while(T--) {


        scanf("%d%d", &N, &K);
        scanf("%lf", &U);

        for(int i = 0; i < N; ++i) {
            scanf("%lf", &core[i]);
        }

        sort(core, core+N, cmp);
        /*
        for(int i = 0; i < N; ++i) {
            printf("%f ", core[i]);
        }
        printf("\n");
        */

        double ans = 0.0;
        if(N == 1) {
            ans = core[0] + U;
        } else {
            for(int i = 0; i < N-1; ++i) {
                /*
                for(int q = 0; q < N; ++q) {
                    printf("%f ", core[q]);
                }
                printf("\n");
                */
                double diff = core[i+1] - core[i];
                /*
                printf("diff = %f\n", diff);
                printf("U = %f\n", U);
                */
                if(U > diff*(i+1)) {
                    U = U - (diff*(i+1));
                    for(int j = 0; j <= i; ++j) {
                        core[j] = core[i+1];
                    }
                } else {
                    for(int j = 0; j <= i; ++j) {
                        core[j] += U / (i+1);
                    }
                    U = 0.0;
                    break;
                }
            }
            for(int i = 0; i < N; ++i) {
                core[i] += U / N;
            }
            /*
            for(int i = 0; i < N; ++i) {
                printf("%f ", core[i]);
            }
            printf("\n");
            */
            ans = core[0];
            for(int i = 1; i < N; ++i) {
                ans *= core[i];
            }
        }

        printf("Case #%d: %f\n", ++cnt, ans);
    }
}
