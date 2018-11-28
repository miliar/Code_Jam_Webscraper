#include <bits/stdc++.h>
using namespace std;
int main(){
    int tc;
    scanf("%d",&tc);
    for(int t = 1; t <= tc; t++){
        int N;
        double D;
        scanf("%lf%d",&D,&N);
        double init[2000], speed[2000];
        double time = 0;
        for(int i = 0; i < N; i++){
            scanf("%lf%lf",&init[i],&speed[i]);
            double temp = (D - init[i])/speed[i];
            time = max(time, temp);
        }

        printf("Case #%d: ",t);
        printf("%f\n", D/time);
    }
    return 0;
}
