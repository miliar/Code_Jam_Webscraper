#include<bits/stdc++.h>
typedef long long lnt;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-out.txt","w",stdout);
    int T,t=0;
    scanf("%d",&T);
    while(T--){
        int n,p;
        scanf("%d%d",&n,&p);
        int a[5]={0},ans=0;
        if(p==2){
            for(int k=1;k<=n;k++){
                int x;
                scanf("%d",&x);
                if(x%2==0) a[0]++;
                else a[1]++;
            }
            ans=a[0]+(a[1]+1)/2;
        }
        else if(p==3){
            for(int k=1;k<=n;k++){
                int x;
                scanf("%d",&x);
                if(x%3==0) a[0]++;
                else if(x%3==1) a[1]++;
                else a[2]++;
            }
            ans+=a[0];
            int y=std::min(a[1],a[2]);
            ans+=y;
            a[1]-=y;a[2]-=y;
            int x=std::max(a[1],a[2]);
            ans+=(x/3 +1);
            if(x%3==0) ans--;
        }
        else{
            for(int k=1;k<=n;k++){
                int x;
                scanf("%d",&x);
                if(x%4==0) a[0]++;
                else if(x%4==1) a[1]++;
                else if(x%4==2) a[2]++;
                else a[3]++;
            }
            ans+=a[0];
            ans+=a[2]/2;
            a[2]%=2;
            int y=std::min(a[1],a[3]);
            ans+=y;
            a[1]-=y;a[3]-=y;
            int x=std::max(a[1],a[3]);
            if(a[2]==0){
                ans+=(x/4 + 1);
                if(x%4==0) ans--;
            }
            else{
                if(x<=1) ans++;
                else{
                    ans++;
                    x-=2;
                    ans+=(x/4 + 1);
                    if(x%4==0) ans--;
                }
            }
        }
        t++;
        printf("Case #%d:",t);
        printf(" %d\n",ans);
    }
}
