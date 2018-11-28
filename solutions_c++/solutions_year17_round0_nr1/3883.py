#include <bits/stdc++.h>

using namespace std;

int T, k, ans;

string s;

void rev(int ss){
    for(int i = 0; i < k; ++i){
        if(s[ss + i] == '+') s[ss + i] = '-';
        else s[ss + i] = '+';
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    cin >> T;
    for(int TT = 1; TT <= T; ++TT){
        cout << "Case #" << TT << ": ";
        cin >> s >> k;
        for(int i = 0; i < s.size(); ++i){
            if(s[i] == '-'){
                ans += 1;
                if(i + k > s.size()){
                    ans = -1;
                    cout << "IMPOSSIBLE\n";
                    break;
                } else {
                    rev(i);
                }
            }

        }
        if(ans != -1) cout << ans << "\n";
        ans = 0;
    }
    return 0;
}