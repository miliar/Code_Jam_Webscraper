#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    int num = 1;
    while(t--) {
        string s;
        int k;
        cin >> s >> k;
        int tot = 0;
        for(int i = 0; i + k -1 < s.size(); i++) {
            if(s[i] == '-') {
                tot ++;
                for(int j = 0 ;j < k; j ++) {
                    s[i + j] = (s[i+j]=='+')?'-':'+';
                }
            }
        }
        int good = 1;
        for(auto it: s) {
            good &= it == '+';
        }
        cout << "Case #" << num << ": ";
        if(good) {
            cout << tot << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
        num ++;
    }
    return 0;
}
