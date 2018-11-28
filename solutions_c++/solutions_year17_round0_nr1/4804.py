#define A
#ifdef A
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    string s;
    int k;int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> s >> k;
        int count  = 0;
        for (int j = 0; j < s.size()-k+1 ; j++) {
            if(s[j]=='-'){
                count++;
                for (int l = j; l < k+j && l<s.size(); ++l) {
                    if(s[l] == '-')
                        s[l] = '+';
                    else s[l] = '-';
                }
            }
        }
        bool ok = true;
        for (int m = 0; m < s.size(); ++m) {
            if(s[m] == '-') ok = false;
        }
        cout << "Case #" << i << ": ";
        if(ok) cout << count << endl;
        else cout << "IMPOSSIBLE\n";
    }
    return 0;
}
#endif