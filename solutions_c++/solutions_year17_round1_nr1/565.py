#include<stdio.h>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<vector>

using namespace std;

typedef long long int lli;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;



int main(void){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tc;
    scanf("%d",&tc);
    char ans[50][50];
    for(int t=1;t<=tc;t++){
        int r, c;
        scanf("%d %d",&r,&c);
        getchar();
        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                ans[i][j]=getchar();
            }
            getchar();
        }
        bool need[50];
        int col[50];
        fill(need, need+50,false);
        fill(col, col+50,-1);
        for(int i=0;i<c;++i){
            if(ans[0][i]=='?'){
                bool found = false;
                for(int j=1;j<r;++j){
                    if(ans[j][i]!='?'){
                        found = true;
                        ans[0][i]=ans[j][i];
                        break;
                    }
                }
                if(!found){
                    need[i]=true;
                }
            }
            if(!need[i]){
                char ac = ans[0][i];
                for(int j=1;j<=r;++j){
                    if(ans[j][i]=='?'){
                        ans[j][i] = ac;
                    }else{
                        ac = ans[j][i];
                    }
                }
            }
        }
        for(int i=0;i<c;++i){
            if(need[i]){
                for(int j=i-1;j>-1;--j){
                    if(!need[j]){
                        col[i]=j;
                        break;
                    }
                }
                if(col[i]==-1){
                    for(int j=i+1;j<c;++j){
                        if(!need[j]){
                            col[i]=j;
                            break;
                        }
                    }
                }
            }else{
                col[i]=i;
            }
        }
        printf("Case #%d:\n",t);
        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                printf("%c",ans[i][col[j]]);
            }
            printf("\n");
        }
    }

    return 0;
}
