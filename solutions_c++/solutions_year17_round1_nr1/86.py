#include<bits/stdc++.h>
using namespace std;
main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,cs,i,j;
    scanf("%d",&T);
    for(cs=1;cs<=T;cs++){
        int R,C;
        char grid[30][30];
        scanf("%d%d",&R,&C);
        for(i=0;i<R;i++)scanf("%s",grid[i]);
        for(i=0;i<R;i++){
            int tag=0;
            for(j=0;j<C;j++){
                if(grid[i][j]!='?'){
                    tag=1;
                    break;
                }
            }
            if(tag){
                for(j=0;j<C;j++)
                    if(j&&grid[i][j]=='?')grid[i][j]=grid[i][j-1];
                for(j=C-1;j>=0;j--)
                    if(j<C-1&&grid[i][j]=='?')grid[i][j]=grid[i][j+1];
            }
        }
        for(i=0;i<R;i++){
            int tag=0;
            for(j=0;j<C;j++){
                if(grid[i][j]!='?'){
                    tag=1;
                    break;
                }
            }
            if(tag==0&&i){
                for(j=0;j<C;j++)grid[i][j]=grid[i-1][j];
            }
        }
        for(i=R-1;i>=0;i--){
            int tag=0;
            for(j=0;j<C;j++){
                if(grid[i][j]!='?'){
                    tag=1;
                    break;
                }
            }
            if(tag==0&&i<R-1){
                for(j=0;j<C;j++)grid[i][j]=grid[i+1][j];
            }
        }
        printf("Case #%d:\n",cs);
        for(i=0;i<R;i++)printf("%s\n",grid[i]);
    }
}
