#include <bits/stdc++.h>
using namespace std;

int T,R,O,Y,G,B,V,n;

int vis[10];
int main(){
    freopen("out.txt","w",stdout);
    int _case=0;
    cin>>T;
    while(T--){
        cout<<"Case #"<<++_case<<": ";
        memset(vis,0,sizeof(vis));
       // scanf(" %d %d %d %d %d %d %d %d",&n,&R,&O,&Y,&G,&B,&V);
        cin>>n>>R>>O>>Y>>G>>B>>V;
        int bob,rgr,yvy;
        int minn = min(R,Y);
        minn = min(minn,B);
        int maxx = max(R,Y);
        maxx = max(maxx,B);
        int mid = n - maxx - minn;
        if(maxx>(minn+mid)){
            printf("IMPOSSIBLE\n");
            continue;
        }
        //cout<<maxx<<" "<<mid<<" "<<minn<<endl;
        char a1,a2,a3;
        int b1=maxx,b2=mid,b3=minn;
        vis[1] = B,vis[2] = R,vis[3] = Y;
        for(int i=1;i<=3;i++){
            if(vis[i]==b1&&b1){
                vis[i]=0;
                b1=0;
                if(i==1){a1='B';}
                else if(i==2){a1='R';}
                else {a1='Y';}
                //cout<<"1 "<<a1<<endl;
                continue;
            }
            else if(vis[i]==b2&&b2){
                vis[i]=0;
                b2=0;
                if(i==1)a2='B';
                else if(i==2)a2='R';
                else a2='Y';
                //cout<<"2 "<<a2<<endl;
                continue;
            }
            else if(vis[i]==b3&&b3){
                vis[i]=0;
                b3=0;
                if(i==1)a3='B';
                else if(i==2)a3='R';
                else a3='Y';
               // cout<<"3 "<<a3<<endl;
            }
        }
        int k1=minn-(maxx-mid);
        for(int i=1;i<=maxx;i++){
            cout<<a1;
            if(i<=mid)cout<<a2;
            if(i<=k1||i>mid)cout<<a3;
        }
        printf("\n");

    }
    return 0;
}
