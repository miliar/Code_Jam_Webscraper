#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        string s;
        int k;
        cin >> s >> k;
        int negcnt = 0;
        for (int i = 0; i < s.size(); ++i) {
            negcnt += s[i]=='-';
        }
        int ans = 0;
        for (int j = 0; j < s.size() - (k-1) && negcnt > 0; ++j) {
            if(s[j]=='-'){
                ++ans;
                for (int i = j; i < j+k; ++i) {
                    if(s[i] == '-'){
                        --negcnt;
                        s[i] = '+';
                    }
                    else{
                        ++negcnt;
                        s[i] = '-';
                    }
                }
            }
        }
        if (negcnt > 0) {
            cout << "Case #" << test << ": IMPOSSIBLE\n";
        } else {
            cout << "Case #" << test << ": " << ans << '\n';
        }
        cerr << "Solved case " << test << '\n';
    }
    return 0;
}