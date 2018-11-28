#include <iostream>

using namespace std;

int solve() {
    int k,n,ans;
    string S;
    ans=0;
    cin>>S>>k;
    n=S.size();
    for(int i=0;i<=n-k;i++){
        if(S[i]=='-'){
            for(int j=0;j<k;j++){
                if(S[i+j]=='-')S[i+j]='+';
                else S[i+j]='-';
            }
            ans++;
        }
    }
    for(int i=0;i<n;i++)
        if(S[i]=='-')return -1;
    return ans;
}

int main () {
    // freopen("A-large.bin","r",stdin);
    // freopen("out_large.txt","w",stdout);

    int tc,ans;
    cin>>tc;
    for(int c=1;c<=tc;c++){
        ans=solve();      
        cout<<"Case #"<<c<<": ";
        if(ans==-1)cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;
    }
    return 0;
}