#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
#define x first
#define y second
int main(){
    int t,C=0;
    scanf("%d",&t);
    while(t--){
        int add[5]={0};
        int n,m;
        scanf("%d%d",&n,&m);
        int ans=0;
        for(int i=0;i<n;i++){
            int x;
            scanf("%d",&x);
            if(x%m==0) ans++;
            else{
                add[x%m]++;
            }
        }
        if(m==2){
            ans+=(add[1]+1)/2;
        }
        else if (m==3){
            int mi = min(add[1], add[2]);
            ans += mi;
            add[1] -= mi;
            add[2] -= mi;
            ans += ( max(add[1], add[2]) + 2 ) / 3;
        }
        printf("Case #%d: %d\n",++C,ans);
    }
}
