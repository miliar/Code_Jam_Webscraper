#include<bits/stdc++.h>
int ori[110][110],now[110][110],use[110];
int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-out.txt","w",stdout);
    int T,t=0,n,m;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%d%d",&n,&m);
        memset(ori,0,sizeof(ori));
        memset(now,0,sizeof(now));
        memset(use,0,sizeof(use));
        for(int k=1;k<=m;k++){
            char c[2];
            int x,y;
            scanf("%s",c);
            scanf("%d%d",&x,&y);
            if(c[0]=='+') ori[x][y]=1;
            if(c[0]=='x') ori[x][y]=2;
            if(c[0]=='o') ori[x][y]=3;
        }
        for(int k=1;k<=n;k++){
            if(ori[1][k]==2||ori[1][k]==3){
                now[1][k]=3;
                use[k]=1;
            }
            else{
                now[1][k]=1;
            }
        }
        bool flag=true;
        for(int k=1;k<=n;k++){
            if(now[1][k]==3) flag=false;
        }
        if(flag){
            now[1][1]=3;
            use[1]=1;
        }
        if(n>1){
            if(use[1]){
                use[n]=1;
                now[n][n]=2;
            }
            else{
                use[1]=1;
                now[n][1]=2;
            }
        }
        for(int k=2;k<=n-1;k++){
            for(int i=1;i<=n;i++){
                if(!use[i]){
                    use[i]=1;
                    now[k][i]=2;
                    break;
                }
            }
        }
        for(int k=2;k<=n-1;k++){
            now[n][k]=1;
        }
        int ans=0,ch=0;
        for(int k=1;k<=n;k++){
            for(int i=1;i<=n;i++){
                if(now[k][i]==1||now[k][i]==2) ans++;
                if(now[k][i]==3) ans+=2;
                if(now[k][i]!=ori[k][i]) ch++;
            }
        }
        printf("Case #%d: ",t);
        printf("%d %d\n",ans,ch);
        for(int k=1;k<=n;k++){
            for(int i=1;i<=n;i++){
                if(now[k][i]!=ori[k][i]){
                    if(now[k][i]==1) printf("+ ");
                    if(now[k][i]==2) printf("x ");
                    if(now[k][i]==3) printf("o ");
                    printf("%d %d\n",k,i);
                }
            }
        }
    }
    
}
