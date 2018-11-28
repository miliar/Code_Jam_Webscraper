#include <bits/stdc++.h>

using namespace std;


string a[30];

void solve() {
    int n,m; cin>>n>>m;
    for(int i = 0;i < n;i++) {
        cin>>a[i];
        for(int j = 1;j < m;j++) {
            if(a[i][j] != '?') continue;
            a[i][j] = a[i][j - 1];
        }
        for(int j = m - 2;j >= 0;j--) {
            if(a[i][j] != '?') continue;
            a[i][j] = a[i][j + 1];
        }
    }
    for(int i = 1;i < n;i++) {
        if(a[i][0] == '?')
            a[i] = a[i - 1];
    }
    for(int i = n - 2;i >= 0;i--) {
        if(a[i][0] == '?')
            a[i] = a[i + 1];
    }
    for(int i = 0;i < n;i++) 
        cout<<a[i]<<endl;
}

int main() {
    assert(freopen("input.txt","r",stdin));
    assert(freopen("output.txt","w",stdout));
    int t; cin>>t;
    for(int i = 1;i <= t;i++) {
        cerr<<"Executing Case #"<<i<<endl;
        cout<<"Case #"<<i<<": "<<endl;
        solve();
    }

}
