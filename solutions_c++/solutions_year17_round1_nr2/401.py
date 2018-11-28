#include<bits/stdc++.h>

typedef long long lnt;
lnt a[100][100],p[100];
double eps=1e-9;
lnt x,y;
void find(lnt a,lnt b){
    y=a*10/b/9;
    x=a*10;
    if(x%(11*b)==0) x=x/11/b;
    else x=1+x/11/b;
    return;
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-out.txt","w",stdout);
    int T,t=0;
    //find(660,300);
    //printf("%lld %lld\n",x,y);
    scanf("%d",&T);
    while(T--){
        t++;
        int n,m;
        scanf("%d%d",&n,&m);
        for(int k=1;k<=n;k++) scanf("%lld",&p[k]);
        for(int k=1;k<=n;k++){
            for(int i=1;i<=m;i++){
                scanf("%lld",&a[k][i]);
            }
        }
        for(int k=1;k<=n;k++){
            std::sort(a[k]+1,a[k]+m+1);
        }
        int now[100];
        for(int k=1;k<=n;k++) now[k]=1;
        int ans=0;
        while(1){
            lnt min=1e7,in=1,L=-1e7,R=1e7;
            for(int k=1;k<=n;k++){
                if(a[k][now[k]]*p[in] < a[in][now[in]]*p[k]) in=k;
                find(a[k][now[k]],p[k]);
                if(x>L) L=x;
                if(y<R) R=y;
            }
            if(L<=R){
                for(int k=1;k<=n;k++) now[k]++;
                ans++;
            }
            else now[in]++;
            bool ok=true;
            for(int k=1;k<=n;k++) if(now[k]>m) ok=false;
            if(!ok) break;
        }
        printf("Case #%d: ",t);
        printf("%d\n",ans);
    }
}
