#include<bits/stdc++.h>
typedef long long lnt;
int pe[1010],se[1010];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-out.txt","w",stdout);
    int T,t=0;
    scanf("%d",&T);
    while(T--){
        int n,c,m;
        scanf("%d%d%d",&n,&c,&m);
        memset(pe,0,sizeof(pe));
        memset(se,0,sizeof(se));
        for(int k=1;k<=m;k++){
             int x,y;
             scanf("%d%d",&x,&y);
             se[x]++;
             pe[y]++;
        }
        int sit=0,tmp=0;
        for(int k=1;k<=n;k++){
            tmp+=se[k];
            int q=(tmp/k)+1;
            if(tmp%k==0) q--;
            if(q>sit) sit=q;
        }
        for(int k=1;k<=c;k++){
            if(sit<pe[k]) sit=pe[k];
        }
        int pro=0;
        tmp=0;
        for(int k=1;k<=n;k++){
            if(se[k]>sit) pro+=(se[k]-sit);
        }
        t++;
        printf("Case #%d:",t);
        printf(" %d %d\n",sit,pro);
    }
}
