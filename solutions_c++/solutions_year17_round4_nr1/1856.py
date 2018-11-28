#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ll long long
#define F first
#define S second
#define pp pair<int,int>
using namespace std;
int ans,n,p;
int a[4];

void fill_up(int sum,int x){
    for(int i=0;i<a[x];i++){
        if(sum==0)ans++;
        sum=(sum+x)%p;
    }
    a[x]=0;
}

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int T=0;
        ans=0;
        for(int i=0;i<4;i++)
            a[i]=0;

        cin>>n>>p;
        for(int i=0;i<n;i++){
            int x;
            cin>>x;
            a[x%p]++;
        }

        ans+=a[0]; a[0]=0;

        if(p==2){
            fill_up(0,1);
        }
        else if(p==3){
            int e=min(a[1],a[2]);
            a[1]-=e;
            a[2]-=e;
            ans+=e;

            fill_up(0,1);
            fill_up(0,2);
        }
        else if(p==4){
            int e=min(a[1],a[3]);
            a[1]-=e;
            a[3]-=e;
            ans+=e;

            e=a[2]/2;
            a[2]%=2;
            ans+=e;

            if(a[2]==0){
                fill_up(0,1);
                fill_up(0,3);
            }else{
                fill_up(2,1);
                fill_up(2,3);
            }
        }
        for(int i=0;i<4;i++)
            if(a[i]!=0)assert(0);
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }

    return 0;
}
