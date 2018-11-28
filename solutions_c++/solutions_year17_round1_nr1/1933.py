#include <bits/stdc++.h>
#define maxn 26
#define inf 0x3f3f3f3f
#define REP(i,x,y) for(int i=x;i<(y);i++)
#define RREP(i,x,y) for(int i=x;i>(y);i--)

using namespace std;
char ma[maxn][maxn];
int n,m;
int vis[maxn];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,cas=1;scanf("%d",&T);
    while(T--){
        memset(vis,0,sizeof(vis));
        scanf("%d %d",&n,&m);getchar();
        REP(i,1,n+1){
            int flag=1;
            REP(j,1,m+1){
                scanf("%c",&ma[i][j]);
                if(ma[i][j]!='?') flag=0;
            }
            if(flag) vis[i]=1;
            getchar();
        }
        int flag1=0;
        REP(i,1,n+1){
            int pos=i,tmp=i;
            while(tmp) {
                if(!vis[tmp]){
                    flag1=1;break;
                }
                tmp--;
            }
            if(!flag1){
            tmp=i;
            while(tmp<=n) {
                if(!vis[tmp]){
                    break;
                }
                tmp++;
            }
            }
            REP(j,1,m+1){
                if(ma[tmp][j]=='?') continue;
               // cout<<ma[tmp][j]<<endl;
                RREP(k,j-1,0){
                    if(ma[tmp][k]!='?') break;
                    else ma[tmp][k]=ma[tmp][j];
                }
            }
            char tt;
            REP(j,1,m+1){
                if(ma[tmp][j]=='?') ma[tmp][j]=tt;
                else tt=ma[tmp][j];
            }
            if(flag1){
                RREP(j,pos,tmp){
                    REP(k,1,m+1){
                        ma[j][k]=ma[tmp][k];
                    }
                }
            }
            else {
                REP(j,pos,tmp){
                    REP(k,1,m+1){
                        ma[j][k]=ma[tmp][k];
                    }
                }
            }
        }
        printf("Case #%d:\n",cas++);
        REP(i,1,n+1){
            REP(j,1,m+1){
                printf("%c",ma[i][j]);
            }
            puts("");
        }
    }
}
