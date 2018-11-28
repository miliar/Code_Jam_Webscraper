#include<cstdio>
#include<algorithm>
using namespace std;
int n, m, P[110], C[110], cnt, Last[110], PV[110];
struct point{
    int b, e;
    bool operator<(const point &p)const{
        return b!=p.b?b<p.b:e<p.e;
    }
}w[110][110];
int main(){
    freopen("/Users/joseunghyeon/Downloads/B-large (1).in","r",stdin);
    freopen("/Users/joseunghyeon/Desktop/code/160929/0409/0409/output.txt","w",stdout);
    int TC, i, j;
    scanf("%d",&TC);
    for(int TT=1;TT<=TC;TT++){
        printf("Case #%d: ",TT);
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++){
            scanf("%d",&P[i]);
        }
        cnt = 0;
        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                int a;
                scanf("%d",&a);
                int b = (a*10 + P[i]*11-1)/(P[i]*11), e = a*10/(P[i]*9);
                w[i][j].b = b, w[i][j].e = e;
            }
            sort(w[i]+1,w[i]+m+1);
            PV[i] = 1;
        }
        int r = 0;
        while(1){
            int ck = 0, bb = -1e9, ee = 1e9;
            for(i=1;i<=n;i++){
                if(PV[i] > m){
                    ck = 1;
                    break;
                }
                bb = max(bb, w[i][PV[i]].b);
                ee = min(ee, w[i][PV[i]].e);
            }
            if(ck)break;
            if(bb <= ee){
                r++;
                for(i=1;i<=n;i++){
                    PV[i]++;
                }
            }
            else{
                for(i=1;i<=n;i++){
                    if(w[i][PV[i]].e == ee)PV[i]++;
                }
            }
        }
        printf("%d\n",r);
    }
}
