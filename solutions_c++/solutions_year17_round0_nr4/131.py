#include<bits/stdc++.h>
using namespace std;
main(){
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int T,cse;
    scanf("%d",&T);
    for(cse=1;cse<=T;cse++){
        int i,j,n,m,ans=0,o=0;
        int xgrid[110][110]={0},xmark[110]={0},ygrid1[210][110]={0},ygrid2[210][110]={0}
            ,ymark1[110]={0},ymark2[110]={0},xtag[110]={0},ytag[210]={0},
            org[110][110]={0},grid[110][110]={0};
        scanf("%d %d",&n,&m);
        for(i=0;i<m;i++){
            char ch;
            int x,y;
            scanf(" %c %d %d",&ch,&x,&y);
            if(ch=='x'||ch=='o'){
                org[x][y]+=1;
                grid[x][y]+=1;
                xgrid[x][y]=1;
                xmark[y]=1;
                xtag[x]=1;
                ans++;
            }
            if(ch=='+'||ch=='o'){
                org[x][y]+=2;
                grid[x][y]+=2;
                ytag[x+y-1]=1;
                if(y>=x){
                    ygrid1[x+y-1][y-x+1]=1;
                    ymark1[y-x+1]=1;
                }
                else{
                    ygrid2[x+y-1][x-y+1]=1;
                    ymark2[x-y+1]=1;
                }
                ans++;
            }
        }
        for(i=1;i<=n;i++){
            if(xtag[i])continue;
            for(j=1;j<=n;j++){
                if(xmark[j]==0){
                    ans++;
                    xmark[j]=1;
                    xgrid[i][j]=1;
                    grid[i][j]+=1;
                    break;
                }
            }
        }
        for(i=1;i<=2*n-1;i++){
            if(ytag[i])continue;
            if(i<=n)j=i;
            else j=2*n-i;
            for(;j>=1;j-=2){
                if(ymark1[j]==0){
                    ans++;
                    ymark1[j]=1;
                    ygrid1[i][j]=1;
                    grid[(i-j+2)/2][(i+j)/2]+=2;
                    break;
                }
                if(j!=1&&ymark2[j]==0){
                    ans++;
                    ymark2[j]=1;
                    ygrid2[i][j]=1;
                    grid[(i+j)/2][(i-j+2)/2]+=2;
                    break;
                }
            }
        }
        int dif=0;
        char p[5]=".x+o";
        for(i=1;i<=n;i++)for(j=1;j<=n;j++)
            if(grid[i][j]!=org[i][j])dif++;
        printf("Case #%d: %d %d\n",cse,ans,dif);
        for(i=1;i<=n;i++)for(j=1;j<=n;j++)
            if(grid[i][j]!=org[i][j])printf("%c %d %d\n",p[grid[i][j]],i,j);
    }
}
