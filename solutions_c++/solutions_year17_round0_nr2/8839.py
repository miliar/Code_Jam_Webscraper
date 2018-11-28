#include <bits/stdc++.h>

using namespace std;

void solve(string &n){
    int t=n.size();
    for(int i=n.size()-1; i>0; i--){
        if(n[i-1] > n[i]){
            n[i-1]--;
            t = i;
        }
    }

    for(int i=n[0]=='0'?1:0; i<t; i++) putchar(n[i]);
    for(int i=t; i<n.size(); i++) putchar('9');
    putchar('\n');
}

int main(){
    int t;
    string s;
    cin >> t;
    for(int i=1; i<=t; i++){
        cin >> s;
        cout << "Case #"<<i<<": ";
        solve(s);
    }

    return 0;
}

