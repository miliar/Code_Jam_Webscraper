#include <bits/stdc++.h>

using namespace std;

int bt (int i, string s, int fl, int k){
    if (i == s.size()){
        for (int j = 0; j < s.size(); j++){
            if (s[j] == '-'){
                return 2222;
            }
            return fl;
        }
    }
    int ret = 2222;
    if (s[i] == '+') {
        ret = min (ret,  bt(i + 1, s, fl, k));
    }
    if (ret < 2222) return ret;
    if (i < s.size () - k + 1){
        for (int j = i; j < i + k; j++){
            s[j] = s[j] == '+' ? '-' : '+';
        }

        if (s[i] == '+'){
            ret = min (ret, bt(i + 1, s, fl + 1, k));
        }
    }
    return ret;
}

int main(){
    freopen("a.inp", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        string s;
        cin >> s;
        int k;
        cin >> k;
        int ret = bt(0, s, 0, k);
        if (ret > 1111){
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        }
        else{
            cout << "Case #" << t << ": " << ret  << endl;
        }
    }
    return 0;
}
