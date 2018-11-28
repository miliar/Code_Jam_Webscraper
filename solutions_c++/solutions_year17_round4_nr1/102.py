#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int n, P, C[4], w[110], D[110][110][110], D2[110][110];
int main(){
    freopen("/Users/joseunghyeon/Downloads/A-large (3).in","r",stdin);
    freopen("/Users/joseunghyeon/Desktop/code/160929/0409/0409/output.txt","w",stdout);
    int i, a, j, k;
    int TT, TC;
    scanf("%d",&TC);
    for(i=0;i<=100;i++){
        for(j=0;j<=100;j++){
            for(k=0;k<=100;k++){
                D[i+4][j][k] = max(D[i+4][j][k], D[i][j][k]+1);
                D[i][j][k+4] = max(D[i][j][k+4], D[i][j][k]+1);
                D[i][j+2][k] = max(D[i][j+2][k], D[i][j][k]+1);
                D[i+1][j][k+1] = max(D[i+1][j][k+1], D[i][j][k]+1);
                D[i+2][j+1][k] = max(D[i+2][j+1][k], D[i][j][k]+1);
                D[i][j+1][k+2] = max(D[i][j+1][k+2], D[i][j][k]+1);
            }
            D2[i+3][j] = max(D2[i+3][j],D2[i][j]+1);
            D2[i][j+3] = max(D2[i][j+3],D2[i][j]+1);
            D2[i+1][j+1] = max(D2[i+1][j+1],D2[i][j]+1);
        }
    }
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ",TT);
        scanf("%d%d",&n,&P);
        for(i=0;i<4;i++)C[i]=0;
        for(i=0;i<n;i++){
            scanf("%d",&a);
            C[a%P]++;
        }
        if(P == 2){
            printf("%d\n", n - C[1]/2);
            continue;
        }
        if(P == 3){
            if(C[1]+C[2]==0){
                printf("%d\n",n);
                continue;
            }
            int r = 0;
            if(C[1])r = max(r, D2[C[1]-1][C[2]]);
            if(C[2])r = max(r, D2[C[1]][C[2]-1]);
            printf("%d\n",r+C[0]+1);
        }
        if(P == 4){
            if(C[1]+C[2]+C[3]==0){
                printf("%d\n",n);
                continue;
            }
            int r = 0;
            if(C[1])r = max(r, D[C[1]-1][C[2]][C[3]]);
            if(C[2])r = max(r, D[C[1]][C[2]-1][C[3]]);
            if(C[3])r = max(r, D[C[1]][C[2]][C[3]-1]);
            printf("%d\n",r+C[0]+1);
        }
    }
}
/*
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int n, m, K, C[1010], w[1010], S[1010];
int main(){
     freopen("/Users/joseunghyeon/Downloads/B-large (2).in","r",stdin);
    freopen("/Users/joseunghyeon/Desktop/code/160929/0409/0409/output.txt","w",stdout);
    int i, a, j, k, b, r;
    int TT, TC;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ",TT);
        scanf("%d%d%d",&n,&K,&m);
        for(i=1;i<=n;i++)w[i]=S[i]=0;
        for(i=1;i<=K;i++)C[i]=0;
        for(i=1;i<=m;i++){
            scanf("%d%d",&a,&b);
            w[a]++;
            C[b]++;
        }
        r = 0;
        for(i=1;i<=K;i++)r = max(r, C[i]);
        for(i=1;i<=n;i++){
            S[i]=S[i-1]+w[i];
            r = max(r, (S[i]+i-1)/i);
        }
        int ss = 0;
        for(i=1;i<=n;i++){
            if(w[i] > r)ss+=w[i]-r;
        }
        printf("%d %d\n",r,ss);
    }
}*/
