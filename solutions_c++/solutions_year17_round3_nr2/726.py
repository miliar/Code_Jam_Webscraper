#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
int T,ac,aj,a[1500],b[1500],dp[1500][3][3500];
int main()
{
    freopen("in","r",stdin);
    freopen("out.txt","w",stdout);
    //int T,ac,aj,a[1500],b[1500];
    cin>>T;
    for(int ca=1;ca<=T;ca++){
            cerr<<ca<<endl;
        cin>>ac>>aj;
        memset(a,0,sizeof(a));
        int be=0;int f=0;int ff=0;
        for(int i=1;i<=ac;i++){
            int l,r;
            cin>>l>>r;
            for(int j=l+1;j<=r;j++){
                    be=j;
                    a[j]=1;
                    f=1;
            }
        }
        for(int i=1;i<=aj;i++){
            int l,r;
            cin>>l>>r;
            for(int j=l+1;j<=r;j++){
                    be=j;
                    f=2;
                    a[j]=2;
            }
        }
        ff=f;
        memset(dp,0x3f,sizeof(dp));
        if(f==1){
            dp[be][1][1501]=0;
        }else dp[be][2][1499]=0;
        for(int i=1;i<1440;i++){
            f=i;
            i=i+be;
            if(i>1440)i-=1440;
            int cy=i-1;
            if(cy==0)cy=1440;
            for(int j=-800;j<=800;j++){
                int tmp=j;
                j+=1500;
                if(a[i]==1){
                    dp[i][1][j]=min(dp[i][1][j],dp[cy][1][j-1]);
                    dp[i][1][j]=min(dp[i][1][j],dp[cy][2][j-1]+1);
                }else if(a[i]==2){
                    dp[i][2][j]=min(dp[i][2][j],dp[cy][2][j+1]);
                    dp[i][2][j]=min(dp[i][2][j],dp[cy][1][j+1]+1);
                }else{
                    dp[i][1][j]=min(dp[i][1][j],dp[cy][1][j-1]);
                    dp[i][1][j]=min(dp[i][1][j],dp[cy][2][j-1]+1);
                    dp[i][2][j]=min(dp[i][2][j],dp[cy][2][j+1]);
                    dp[i][2][j]=min(dp[i][2][j],dp[cy][1][j+1]+1);
                }
                j=tmp;
            }
            i=f;
        }
        be--;
        if(be==0)be=1440;
        int ans=1500;
        if(ff==1)ans=min(ans,min(dp[be][1][1500],dp[be][2][1500]+1));
        else ans=min(ans,min(dp[be][1][1500]+1,dp[be][2][1500]));
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
