#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    int cases=0;
    scanf("%d",&T);
    while(T--){
        int N,P;
        scanf("%d%d",&N,&P);
        cases++;
        int arr[4];
        memset(arr,0,sizeof arr);
        for(int i=0;i<N;i++){
            int tmp;
            scanf("%d",&tmp);
            arr[tmp%P]++;
        }
        if(P==2){
            cout<<"Case #"<<cases<<": "<<arr[0]+(arr[1]+1)/2<<endl;;
        }
        else if(P==3){
            int ans=arr[0];
            ans+=(min(arr[1],arr[2]));
            int k=min(arr[1],arr[2]);
            arr[1]-=k;
            arr[2]-=k;
            ans+=(arr[1]+2)/3;
            ans+=(arr[2]+2)/3;
            cout<<"Case #"<<cases<<": "<<ans<<endl;
        }
        else{
            int ans=arr[0];
            ans+=min(arr[3],arr[1]);
            int k=min(arr[3],arr[1]);
            arr[3]-=k;
            arr[1]-=k;
            ans+=arr[2]/2;
            arr[2]%=2;
            int lft=max(arr[1],arr[3]);
            if(arr[2]&&lft>1){
                ans++;
                lft-=2;
            }
            ans+=(lft+3)/4;
            cout<<"Case #"<<cases<<": "<<ans<<endl;
        }
    }
}
