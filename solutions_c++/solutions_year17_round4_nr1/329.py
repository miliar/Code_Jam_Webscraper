
#include <iostream>
#include<cstring>
#include <cstdio>
#include <algorithm>
#include<queue>
#include<cmath>
#define N 350000
#define M 750000
#define INF 2000000000
using namespace std;
int n,p;
int x[300];
//2 2 2 1 1 1
//2 1 2 1 2 1
int cnt[5];
//0 1 1 2
int main(int argc, const char * argv[])
{
    
    
    freopen("1.txt","r",stdin);
    freopen("1.out","w",stdout);
    int  tt,x,ans,tmp;
    cin>>tt;
    for(int cas=1;cas<=tt;cas++)
    {
        cin>>n>>p;
        for(int i=0;i<=4;i++)cnt[i]=0;
        for(int i=1;i<=n;i++){cin>>x;cnt[x%p]++;}
        if(p==2)
        {
            ans=cnt[0]+(cnt[1]+1)/2;
        }
        if(p==3)
        {
            ans=cnt[0]+min(cnt[1],cnt[2]);
         //   cout<<"ans:"<<ans<<endl;
            cnt[1]=abs(cnt[1]-cnt[2]);
         //   cout<<"cnt1"<<cnt[1]<<endl;
            ans+=(cnt[1]+2)/3;
    //        cout<<ans<<endl;
        }
        if(p==4)
        {
            tmp=min(cnt[3],cnt[1]);
            cnt[3]-=tmp;
            cnt[1]-=tmp;
            ans=cnt[0]+tmp;
            if(cnt[2]>1)
            {
                ans+=cnt[2]/2;
                cnt[2]%=2;
            }
            if(cnt[3])
            {
                if(cnt[2]>=1&&cnt[3]>=2){ans++;cnt[2]--;cnt[3]-=2;}
                ans+=cnt[3]/4;
                cnt[3]%=4;
                //3 3 2
            }
            else if(cnt[1])
            {
                if(cnt[2]>=1&&cnt[1]>=2){ans++;cnt[2]--;cnt[1]-=2;}
                ans+=cnt[1]/4;
                cnt[1]%=4;
            }
            if(cnt[2]>0||cnt[3]>0||cnt[1]>0)ans++;
            
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    
}
