#include <iostream>
#include <string>
#include <algorithm>


using namespace std;

#define ll long long

ll solve () {
    ll n,p;
    cin>>n;
    string s = to_string(n);
    reverse(s.begin(),s.end());
    int i=0;
    p=10;
    while(p<=n){
        if(s[i]<s[i+1]){
            n-=n%p+1;
            s=to_string(n);
            reverse(s.begin(),s.end());
        }
        p*=10;
        i++;
    }
    return n;
}

int main () {
    freopen("B-large.bin","r",stdin);
    freopen("B_large_out.txt","w",stdout);
    ll ans;
    int tc;
    cin>>tc;
    for(int c=1;c<=tc;c++){
        ans=solve();
        cout<<"Case #"<<c<<": "<<ans<<endl;
    }
    return 0;
}