#include <bits/stdc++.h>
using namespace std;



int main(){
    ios_base::sync_with_stdio(false);
    freopen("in", "r", stdin); freopen("out", "w", stdout);
    int t; cin >> t;
    for(int tt = 0 ; tt < t; ++tt){
        string s;
        getline(cin, s, ' ');
        int k; cin >> k;
        int ans = 0;
        for(uint i = 1 ; i < s.size(); ++i){
            if(s[i] == '-'){
                if(i + k > s.size()){
                    ans = -1;
                    break;
                }
                ans++;
                for(int j = 0 ; j < k; ++j){
                    if(s[i + j] == '-') s[i + j] = '+';
                    else s[i + j] = '-';
                }
            }
        }
        if(ans == -1) cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << tt + 1 << ": " << ans << endl;
    }
    return 0;
}


