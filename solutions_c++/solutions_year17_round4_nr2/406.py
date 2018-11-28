#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int arr[1010];
int tickets[1010];

int main() {
    freopen("hi.txt","r",stdin);
    freopen("hi2.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    int n,p;
    for(int t=1;t<=tc;t++){
        //printf("%d\n",t);
        int n,c,m;
        scanf("%d%d%d",&n,&c,&m);
        memset(arr,0,sizeof(arr));
        memset(tickets,0,sizeof(tickets));
        int a,b;
        int ans=0;
        for(int i=0;i<m;i++){
            scanf("%d%d",&a,&b);
            tickets[b]++;
            arr[a]++;
            ans=max(ans,tickets[b]);
        }
        int presum[n+10];
        presum[1]=arr[1];
        for(int i=2;i<=n;i++){
            presum[i]=presum[i-1]+arr[i];
        }
        for(int i=1;i<=n;i++){
            ans=max(ans,(int)(ceil((double)presum[i]/i)+0.01));
        }
        int ans2=0;
        for(int i=1;i<=n;i++){
            if(arr[i]>ans){
                ans2+=arr[i]-ans;
            }
        }
        printf("Case #%d: %d %d\n",t,ans,ans2);
//        printf("Case #%d: %d %d\n",t,ans,ans2);
    }
}
