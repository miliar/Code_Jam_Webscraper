#include <cstdio>
#include <cstring>
#include <vector>

int main(){
    int T;
    int D, N;
    scanf("%d", &T);
    int t = 1;
    while(t < T+1){
        scanf("%d %d\n", &D, &N);
        int start, speed;
        float maxTime = 0;
        for(int i = 0; i < N; i++){
            scanf("%d %d", &start, &speed);
            float time = float(D-start)/speed;
            if(time > maxTime)
                maxTime = time;
        }
        printf("Case #%d: %f\n", t, float(D)/maxTime);
        t++;
    }
}
