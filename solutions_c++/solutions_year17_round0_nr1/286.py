#include <bits/stdc++.h>
using namespace std;

char flip(char c){
    if(c == '-'){
        return '+';
    }
    else{
        return '-';
    }
}

void solve(){
    string s;
    int n,k,ans=0;
    cin >> s >> k;
    n = s.size();
    s = '^' + s;
    for(int i=1; i<=n-k+1; i++){
        if(s[i] == '-'){
            ans++;
            for(int j=i; j<i+k; j++){
                s[j] = flip(s[j]);
            }
        }
    }
    bool possible = true;
    for(int i=n-k+2; i<=n; i++){
        if(s[i] == '-'){
            possible = false;
        }
    }
    if(possible){
        cout << ans;
    }
    else{
        cout << "IMPOSSIBLE";
    }
}

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin >> t;
    for(int c=1; c<=t; c++){
        cout << "Case #" << c << ": ";
        solve();
        cout << endl;
    }
}
