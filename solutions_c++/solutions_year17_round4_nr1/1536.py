#include <bits/stdc++.h>
#define maxn 100010
#define inf 0x3f3f3f3f
#define REP(i,x,y) for(int i=x;i<(y);i++)
#define RREP(i,x,y) for(int i=x;i>(y);i--)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
int dp[110][110][110],cnt[4];
int a[110];
int main()
{
    freopen("A-large(3).in","r",stdin);
    freopen("data.out","w",stdout);
    int T,cas=1;scanf("%d",&T);
    while(T--){
        memset(dp,0,sizeof(dp));memset(cnt,0,sizeof(cnt));
        int ans=0;
        int n,p;scanf("%d %d",&n,&p);
        REP(i,1,n+1) {
            scanf("%d",&a[i]);
            a[i]%=p;
            cnt[a[i]]++;
        }
        if(p==2){
            int tmp=0;
            REP(i,1,n+1){
            if(a[i]==0) ans++;
            else tmp++;
            }
            ans+=(tmp+1)/2;
            printf("Case #%d: %d\n",cas++,ans);
        }
        else if(p==3){
            int tmp1=0,tmp2=0;
            REP(i,1,n+1){
                if(a[i]==0) ans++;
                else if(a[i]==1) tmp1++;
                else tmp2++;
            }
            ans+=min(tmp1,tmp2);
            ans+=(max(tmp1,tmp2)-min(tmp1,tmp2)+2)/3;
            printf("Case #%d: %d\n",cas++,ans);
        }
        else if(p==4){
            //REP(i,1,n+1) cout<<a[i]<<endl;
            //cout<<cnt[1]<<" "<<cnt[2]<<" "<<cnt[3]<<endl;
            dp[0][0][0]=0;
            REP(i,0,cnt[1]+1){
                REP(j,0,cnt[2]+1){
                    REP(k,0,cnt[3]+1){
                        if(i) {
                            int sum=(i-1+2*j+3*k)%p;
                            if(sum) dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k]);
                            else dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k]+1);
              //              cout<<i<<" "<<j<<" "<<k<<" "<<dp[i][j][k]<<endl;
                        }
                        if(j){
                            int sum=(i+2*(j-1)+3*k)%p;
                            if(sum) dp[i][j][k]=max(dp[i][j][k],dp[i][j-1][k]);
                            else dp[i][j][k]=max(dp[i][j][k],dp[i][j-1][k]+1);
                //            cout<<i<<" "<<j<<" "<<k<<" "<<dp[i][j][k]<<endl;
                        }
                        if(k){
                            int sum=(i+2*j+3*(k-1))%p;
                            if(sum) dp[i][j][k]=max(dp[i][j][k],dp[i][j][k-1]);
                            else dp[i][j][k]=max(dp[i][j][k],dp[i][j][k-1]+1);
                  //          cout<<i<<" "<<j<<" "<<k<<" "<<dp[i][j][k]<<endl;
                        }
                    }
                }
            }
            int ans=dp[cnt[1]][cnt[2]][cnt[3]];
            printf("Case #%d: %d\n",cas++,ans+cnt[0]);
        }
    }
}
