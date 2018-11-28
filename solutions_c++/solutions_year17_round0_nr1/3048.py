#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s;
    int k;
    cin >> s >> k;
    int slen = s.length();
    int flips = 0;
    for(int i=0; i<=slen-k; ++i){
        if(s[i] == '-'){
            ++flips;
            for(int j=0; j<k; ++j){
                if(s[i+j] == '+')
                    s[i+j] = '-';
                else
                    s[i+j] = '+';
            }
        }
    }
    for(int i=slen-k+1; i<slen; ++i){
        if(s[i] == '-'){
            cout << "IMPOSSIBLE";
            return;
        }
    }
    cout << flips;
}

int main(){
    int tc;
    cin >> tc;
    for(int t=1; t<=tc; ++t){
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }
}
