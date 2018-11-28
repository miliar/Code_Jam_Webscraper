#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#define MAXN 1002
#define eps 1e-6
using namespace std;
int T,N,P;
double R[MAXN];
double Q[MAXN][MAXN];
int ind[MAXN];

int inside(double x, double y){
    if(x<y*0.9) return -1;
    if(x<=y*1.1 && x>= y*0.9)
        return 0;
    if(x>y*1.1) return 1;
}
int solve(){
    int ans=0;
    for(int i=0;i<N;++i)
        for(int j=0;j<P;++j){
            Q[i][j]/=R[i];
        }
    for(int i=0;i<P;++i){
        sort(Q[i],Q[i]+P);
    }
    double b,t;
    for(int i=0;i<P;++i){
        b = ceil(Q[0][i]/1.1);
        t = floor(Q[0][i]/0.9);
        //cout<<b<<" "<<t<<"\n";
        if(N==1){
            if(t>=b) ans++;
                continue;
        }
        for(int j=b;j<=t;++j){
            int cnt=0;
            for(int k=1;k<N;++k){
                while( inside(Q[k][ind[k]],j)==-1 ){
                    ind[k]++;
                    if(ind[k]==P) return ans;
                }
                if( inside(Q[k][ind[k]],j)==0 )
                    cnt++;
                else break;
            }
            if(cnt==N-1){
                ans++;
                for(int k=1;k<N;++k){
                    ind[k] ++;
                    if(ind[k]==P) return ans;
                }
                break;
            }
        }
    }
    return ans;
}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    for(int c=1;c<=T;++c){
        scanf("%d%d",&N,&P);
        memset(R,0,sizeof(R));
        memset(Q,0,sizeof(Q));
        memset(ind,0,sizeof(ind));
        for(int i=0;i<N;++i)
            scanf("%lf",&R[i]);
        for(int i=0;i<N;++i)
            for(int j=0;j<P;++j)
                scanf("%lf",&Q[i][j]);

        printf("Case #%d: %d\n",c,solve());

    }
    return 0;
}
