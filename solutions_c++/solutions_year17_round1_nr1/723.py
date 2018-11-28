/*#include<cstdio>
#include<algorithm>
using namespace std;
long long Calc(long long a, long long b, long long h){
    long long i, r = 1e10;
    for(i=0;i<=100000;i++){
        r = min(r, i + (h + (a+i*b - 1))/(a+i*b));
    }
    return r;
}
long long Get(int h, int H, int A, int K){
    int t = (h-1)/A;
    if(t+1>=K)return K;
    int r = t+1;
    K-=t;
    int g = (H-1)/A;
    if(g==1)return 1e15;
    return r+K+(K-2)/(g-1);
}
long long Do(int H, int A, int M, int K, int D){
    int i, c = 0;
    int h = H;
    long long res = 2e10;
    M = min(M,K+2);
    for(i=0;i<=M;i++){
        res = min(res,0ll+Get(h,H,A,K)+i+c);
        A-=D;
        if(A<=0){
            res = min(res, 0ll+i+1+c+K);
            break;
        }
        h-=A;
        if(h <= A-D){
            c++;
            h = H-A;
        }
    }
    return res;
}
int main(){
    long long H1, A1, H2, A2, B, D;
    freopen("/Users/joseunghyeon/Downloads/C-small-attempt1.in","r",stdin);
    //freopen("/Users/joseunghyeon/Desktop/code/160929/0409/0409/output.txt","w",stdout);
    int TC, i, j;
    scanf("%d",&TC);
    for(int TT=1;TT<=TC;TT++){
        printf("Case #%d: ",TT);
        scanf("%lld%lld%lld%lld%lld%lld",&H1,&A1,&H2,&A2,&B,&D);
        if(A1 >= H2){
            printf("1\n");
            continue;
        }
        else if(A2 - D >= H1){
            printf("IMPOSSIBLE\n");
            continue;
        }
        else if(A2 <H1 && (A1*2 >= H2 || A1+B>=H2)){
            printf("2\n");
            continue;
        }
        else if(A2*2 - D*3 >= H1){
            printf("IMPOSSIBLE\n");
            continue;
        }
        long long K = Calc(A1,B,H2);
        int M;
        if(D==0)M = 0;
        else M = (A2+D-1)/D;
        printf("%lld\n",Do(H1,A2,M,K,D));
    }
}*/
#include<cstdio>
#include<algorithm>
using namespace std;
int n, m;
char p[30][30];
int main(){
    freopen("/Users/joseunghyeon/Downloads/A-large (2).in","r",stdin);
    freopen("/Users/joseunghyeon/Desktop/code/160929/0409/0409/output.txt","w",stdout);
    int TC, T, i, j;
    scanf("%d",&TC);
    for(T=1;T<=TC;T++){
        printf("Case #%d:\n",T);
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++){
            scanf("%s",p[i]+1);
        }
        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                if(p[i][j]=='?'){
                    if(j>1 &&p[i][j-1]!='?')p[i][j]=p[i][j-1];
                }
            }
            for(j=m;j>=1;j--){
                if(p[i][j]=='?'){
                    if(j<m &&p[i][j+1]!='?')p[i][j]=p[i][j+1];
                }
            }
        }
        for(i=1;i<=m;i++){
            for(j=1;j<=n;j++){
                if(p[j][i]=='?'){
                    if(j>1 &&p[j-1][i]!='?')p[j][i]=p[j-1][i];
                }
            }
            for(j=n;j>=1;j--){
                if(p[j][i]=='?'){
                    if(j<n &&p[j+1][i]!='?')p[j][i]=p[j+1][i];
                }
            }
        }
        for(i=1;i<=n;i++){
            printf("%s\n",p[i]+1);
        }
    }
}
