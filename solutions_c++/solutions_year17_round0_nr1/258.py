#include <bits/stdc++.h>

using namespace std;

const int N=1e3+10;
string s;
int k,a[N];


void solve(){
    int n=s.length();
    for(int i=0;i<n;i++) a[i]=s[i]=='-';

    int ans=0;
    for(int i=0;i<n;i++) if (a[i]){
        if (i>n-k){
            printf("IMPOSSIBLE\n");
            return;
        }
        for(int j=0;j<k;j++) a[i+j]^=1;
        ans++;
    }
    cout<<ans<<'\n';
}
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int test;
    cin>>test;
    for(int te=1;te<=test;te++){
        cin>>s>>k;
        cout<<"Case #"<<te<<": ";
        solve();
    }
}
