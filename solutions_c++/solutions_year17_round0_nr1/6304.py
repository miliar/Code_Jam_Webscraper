#include <bits/stdc++.h>
using namespace std;
inline void solve();
int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);
    int t,i=0;
    cin >> t;

    while (i<t) {
        cout<<"Case #"<<i+1<<": ";
        solve();
        cout<<endl;
        i++;
    }
    return 0;
}




#define int int

const int ost =1e9+7;

inline void solve() {
    string s;
    cin>>s;int k;cin>>k;
    int ans=0;
    for(int i=0;i<=s.size()-k;i++){
        if(s[i]=='-'){
            for(int j=0;j<k;j++)
                s[i+j]=s[i+j]=='-'?'+':'-';
            ans++;
        }
    }
    for(auto i:s){
        if(i!='+'){
            cout<<"IMPOSSIBLE";
            return;
        }
    }
    cout<<ans;
}





















