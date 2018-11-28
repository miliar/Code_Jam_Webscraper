#include <bits/stdc++.h>

using namespace std;

void solve() {
    string s; cin>>s;
    int k; cin>>k;
    int n = (int)s.length();
    int ans = 0;
    for(int i = 0;i + k <= n;i++) {
        if(s[i] == '-') {
            ans++;
            for(int j = i;j < i + k;j++) {
                s[j] = (s[j] == '+') ? '-' : '+';
            }
        }
    }
    int flag = 0;
    for(int i = 0;i < n;i++) {
        if(s[i] != '+') {
            flag = 1;
            break;
        }
    }
    if(!flag)
        cout<<ans<<endl;
    else
        cout<<"IMPOSSIBLE"<<endl;
}

int main() {
    assert(freopen("input.txt","r",stdin));
    assert(freopen("output.txt","w",stdout));
    int t; cin>>t;
    for(int i = 1;i <= t;i++) {
        cerr<<"Executing Case #"<<i<<endl;
        cout<<"Case #"<<i<<": ";
        solve();
    }

}
