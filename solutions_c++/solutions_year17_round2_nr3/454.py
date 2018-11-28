#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

double dij[105];
long long jarak[105][105];
long long E[105],S[105];
int N,Q,T,start,end;
bool sudah[105];

int main() {
    scanf("%d",&T);
    for (int l=1;l<=T;++l) {
        scanf("%d %d",&N,&Q);
        for (int i=1;i<=N;++i) scanf("%I64d %I64d",&E[i],&S[i]);
        for (int i=1;i<=N;++i) {
            for (int j=1;j<=N;++j) {
                scanf("%I64d",&jarak[i][j]);
            }
        }
        
        for (int k=1;k<=N;++k) {
            for (int i=1;i<=N;++i) {
                for (int j=1;j<=N;++j) {
                    if (jarak[i][k] == -1 || jarak[k][j] == -1) continue;
                    if (jarak[i][j] == -1) jarak[i][j] = jarak[i][k]+jarak[k][j];
                    else jarak[i][j] = min(jarak[i][j],jarak[i][k]+jarak[k][j]);
                }
            }
        }
        
        /*for (int i=1;i<=N;++i) {
            for (int j=1;j<=N;++j) printf("%I64d ",jarak[i][j]);
            printf("\n");
        }*/
        
        printf("Case #%d:",l);
        for (int i=1;i<=Q;++i) {
            scanf("%d %d",&start,&end);
            //printf("kasus %d %d\n",start,end);
            memset(sudah,0,sizeof(sudah));
            for (int j=1;j<=N;++j) dij[j] = 1000000000000000L;
            dij[start] = 0;
            for (int j=1;j<=N && !sudah[end];++j) {
                int ambil = -1;
                for (int k=1;k<=N;++k) {
                    if (sudah[k]) continue;
                    if (ambil == -1 || dij[k] < dij[ambil]) ambil = k;
                }
                
                sudah[ambil] = true;
                //printf("%d : %.6lf\n",ambil,dij[ambil]);
                for (int k=1;k<=N;++k) {
                    if (sudah[k] || jarak[ambil][k] == -1 || jarak[ambil][k] > E[ambil]) continue;
                    dij[k] = min(dij[k],dij[ambil] + (double)jarak[ambil][k] / S[ambil]);
                }
            }
            
            printf(" %.6lf",dij[end]);
        }
        printf("\n");
    }
    return 0;
}
