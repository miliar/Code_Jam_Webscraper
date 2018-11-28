#include <stdio.h>
#define min(x,y) ((x)>(y) ? (y) : (x))

int T;
int N, P;
int grp[101];
int spl[5][101];
int sp[5];
int res;

int main(){
    scanf("%d",&T);
    for (int t = 1; t <= T; t++){
        scanf("%d %d",&N, &P);
        for (int i = 0; i < P; i++){
            sp[i] = 0;
        }
        for (int i = 0; i < N; i++){
            scanf("%d",&grp[i]);
        }
        for (int i = 0; i < N; i++){
            int tmp = grp[i]%P;
            spl[tmp][sp[tmp]++] = grp[i];
        }
        if (P == 2){
            res = sp[0] + (sp[1]+1)/2;
        }
        else{
            int tmp = min(sp[1], sp[2]);
            res = sp[0] + tmp;
            sp[1] -= tmp;
            sp[2] -= tmp;
            res += (sp[1]+2)/3 + (sp[2]+2)/3;
        }
        printf("Case #%d: %d\n", t, res);
    }
    return 0;
}
