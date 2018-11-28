#define A
#ifdef A
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    string str;
    int k;int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> str >> k;
        int count  = 0;
        for (int j = 0; j < str.size()-k+1 ; j++) {
            if(str[j]=='-'){
                ++count;
                for (int l = j; l < k+j && l<str.size(); ++l) {
                    if(str[l] == '-')
                        str[l] = '+';
                    else str[l] = '-';
                }
            }
        }
        bool ok = true;
        for (int m = 0; m < str.size(); ++m) {
            if(str[m] == '-') ok = false;
        }
        cout << "Case #" << i << ": ";
        if(ok) cout << count << endl;
        else cout << "IMPOSSIBLE\n";
    }
    return 0;
}
#endif