#include <stdio.h>

int T;
int res;
int C, J;
struct act_t{
    int C;
    int D;
    int who;
};
act_t act[302];
int times[2] = {0,};
int remain[2][302], rp[2];
int best;

void proc(){
    int res = !(act[0].who == act[C+J+1].who);
    rp[0] = rp[1] = 0;
    for (int i = 1; i <= C+J+1; i++){
        if (act[i-1].who == act[i].who){
            remain[!act[i].who][rp[!act[i].who]++] = act[i].C - act[i-1].D;
            res+=2;
        } else{
            res++;
        }
    }
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < rp[i]; j++){
            for (int k = j+1; k < rp[i]; k++){
                if (remain[i][j] > remain[i][k]){
                    int tmp = remain[i][j];
                    remain[i][j] = remain[i][k];
                    remain[i][k] = tmp;
                }
            }
        }
    }
    int tmp[2] = {720-times[0], 720-times[1]};
    for (int i = 0; i < 2; i++){
        for (int j = 0; j <rp[i]; j++){
            if (tmp[i] >= remain[i][j]){
                tmp[i] -= remain[i][j];
                res-=2;
            }
        }
    }
    if (best > res)
        best = res;
}

int main(){
    scanf("%d",&T);
    for (int t = 1; t <= T; t++){
        scanf("%d %d",&C, &J);
        times[0] = times[1] = 0;
        for (int i = 1; i <= C; i++){
            scanf("%d %d", &act[i].C, &act[i].D);
            act[i].who = 0;
            times[1] += act[i].D - act[i].C;
        }
        for (int i = 1; i <= J; i++){
            scanf("%d %d", &act[C+ i].C, &act[C + i].D);
            act[C + i].who = 1;
            times[0] += act[C + i].D - act[C + i].C;
        }
        for (int i = 1; i <= C+J; i++){
            for (int j = i+1; j <= C+J; j++){
                if (act[i].C > act[j].C){
                    act_t swp = act[i];
                    act[i] = act[j];
                    act[j] = swp;
                }
            }
        }
        act[0].C = 0;
        act[0].D = 0;
        act[C+J+1].C = 1440;
        act[C+J+1].D = 1440;
        best = 999999999;
        for (int i = 0; i <2; i++){
            for (int j = 0; j < 2; j++){
                act[0].who = i;
                act[C+J+1].who = j;
                proc();
            }
        }
        printf("Case #%d: %d\n", t, best);
    }
    return 0;
}
