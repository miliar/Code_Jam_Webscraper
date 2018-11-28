#include <cstdio>

double result[105];

int main(){
    int totalCases;
    scanf("%d", &totalCases);
    for(int T = 1; T <= totalCases; ++T){
        int D, N;
        scanf("%d%d", &D, &N);
        double ans;
        for(int i = 1; i <= N; ++i){
            int K, S;
            scanf("%d%d", &K, &S);
            double hour = ((double)D-K)/S;
            if(i == 1)
                ans = hour;
            else{
                if(hour > ans)
                    ans = hour;
            }
        }
        result[T] = D/ans;
    }
    for(int T = 1; T <= totalCases; ++T){
        printf("Case #%d: %.6lf\n", T, result[T]);
    }
    return 0;
}
