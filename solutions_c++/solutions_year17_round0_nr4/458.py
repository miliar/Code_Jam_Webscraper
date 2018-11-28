#include <cstdio>

bool r[109][109];
bool rl[109];
bool ru[109];
bool d[109][109];
bool ds[209];
bool dd[209];
bool ir[109][109];
char ic[109][109];

char c[10009];
int R[10009];
int C[10009];

int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("Dsmalloutput.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        int N, M;
        scanf("%d %d", &N, &M);
        for (int i = 0; i < M; i++){
            scanf(" %c %d %d", &c[i], &R[i], &C[i]);
            ir[R[i]][C[i]] = true;
            ic[R[i]][C[i]] = c[i];
            if (c[i]=='x'||c[i]=='o'){
                r[R[i]][C[i]] = true;
                ru[R[i]] = true;
                rl[C[i]] = true;
            }
            if (c[i]=='+'||c[i]=='o'){
                d[R[i]][C[i]] = true;
                ds[R[i]+C[i]] = true;
                dd[R[i]-C[i]+100] = true;
            }
        }
        int rrr = 0, ccc = 0;
        while (rrr<=N&&ccc<=N){
            do {
                rrr++;
            } while (rrr<=N&&ru[rrr]);
            do {
                ccc++;
            } while (ccc<=N&&rl[ccc]);
            ru[rrr] = true;
            rl[ccc] = true;
            r[rrr][ccc] = true;
        }
        for (int i = 1; i <= N; i++){
            d[1][i] = true;
        }
        for (int i = 2; i < N; i++){
            d[N][i] = true;
        }
        printf("Case #%d: ",t);
        int ct = 0, score = 0;
        for (int i = 1; i <= N; i++){
            for (int j = 1; j <= N; j++){
                if (r[i][j]&&!d[i][j]){
                    if (!(ir[i][j]&&ic[i][j]=='x')){
                        ct++;
                    }
                    score++;
                }
                else if (!r[i][j]&&d[i][j]){
                    if (!(ir[i][j]&&ic[i][j]=='+')){
                        ct++;
                    }
                    score++;
                }
                else if (r[i][j]&&d[i][j]){
                    if (!(ir[i][j]&&ic[i][j]=='o')){
                        ct++;
                    }
                    score += 2;
                }
            }
        }
        printf("%d %d\n", score, ct);
        for (int i = 1; i <= N; i++){
            for (int j = 1; j <= N; j++){
                if (r[i][j]&&!d[i][j]){
                    if (!(ir[i][j]&&ic[i][j]=='x')){
                        printf("%c %d %d\n",'x',i,j);
                    }
                    r[i][j] = false;
                    ru[i] = false;
                    rl[j] = false;
                }
                else if (!r[i][j]&&d[i][j]){
                    if (!(ir[i][j]&&ic[i][j]=='+')){
                        printf("%c %d %d\n",'+',i,j);
                    }
                    d[i][j] = false;
                    ds[i+j] = false;
                    dd[i-j+100] = false;
                }
                else if (r[i][j]&&d[i][j]){
                    if (!(ir[i][j]&&ic[i][j]=='o')){
                        printf("%c %d %d\n",'o',i,j);
                    }
                    r[i][j] = false;
                    ru[i] = false;
                    rl[j] = false;
                    d[i][j] = false;
                    ds[i+j] = false;
                    dd[i-j+100] = false;
                }
                ir[i][j] = false;
                ic[i][j] = '.';
            }
        }
    }
}
