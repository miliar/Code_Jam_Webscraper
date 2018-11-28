#include <bits/stdc++.h>

using namespace std;

int T, l;

string s;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    cin >> T;
    for(int TT = 1; TT <= T; ++TT){
        cin >> s;
        cout << "Case #" << TT << ": ";
        if(s.size() == 1){
            cout << s << "\n";
        } else {
            for(int i = 1; i < s.size(); ++i){
                if(s[i] > s[i - 1]){
                    l = i;
                } else if(s[i] < s[i - 1]){
                    if(s[l] != '1'){
                    for(int j = 0; j < l; ++j) {
                        cout << s[j];
                    }
                        cout << (char)(s[l] - 1);
                    for(int j = l + 1; j < s.size(); ++j)
                        cout << '9';
                    }
                    else {
                        for(int j = 0; j < s.size() - 1; ++j)
                            cout << '9';
                    }
                    l = -1;
                    break;
                }
            }
            if(l != -1) cout << s;
            cout << "\n";
            l = 0;
        }

    }
    return 0;
}