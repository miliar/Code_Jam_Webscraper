#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;
double s[10005],k[10005];
double d;
int n;
void read(){
    cin>>d>>n;
    int i;
    for(i=1;i<=n;i++){
        cin>>k[i]>>s[i];
    }
}
void solve(){
    double mx=0;
    for(int i=1;i<=n;i++){
        mx=max(mx,(d-k[i])/s[i]);
    }
    printf("%.9llf\n",d/mx);
}
int main(){
    int t;
    freopen("Al.in","r",stdin);
    freopen("Al.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++){
        read();
        cout<<"Case #"<<i<<": ";
        solve();
    }
}
