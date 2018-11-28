#include <bits/stdc++.h>
using namespace std;

void solve(){
    string n;
    cin >> n;
    int slen = n.length();
    for(int i=0; i<slen-1; ++i){
        if(n[i] > n[i+1]){
            --n[i];
            int j;
            for(j=i; j>=0; --j){
                if(j > 0 && n[j-1] > n[j]){
                    --n[j-1];
                }
                else
                    break;
            }
            for(int k=j+1; k<slen; ++k)
                n[k] = '9';
            break;
        }
    }
    for(int i=0; i<slen; ++i){
        if(n[i] != '0'){
            cout << n.data()+i;//n.substr(i);
            return;
        }
        assert(i<slen-1);
    }
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
