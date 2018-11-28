#include<bits/stdc++.h>
using namespace std;

int cas = 0;
bool check(int x){
    int la = 10;
    while(x){
        if(la<x%10)return false;
        la = x%10;
        x/=10;
    }
    return true;
}
void solve(){
    printf("Case #%d: ",++cas);
    int n;
    cin>>n;
    int ans = 0;
    for(int i=1;i<=n;i++){
        if(check(i))
            ans=max(ans,i);
    }
    cout<<ans<<endl;
}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("1.out","w",stdout);
    int t;
    scanf("%d",&t);
    while(t--){
        solve();
    }
}
