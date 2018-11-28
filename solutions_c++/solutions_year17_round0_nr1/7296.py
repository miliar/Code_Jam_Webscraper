#include <bits/stdc++.h>
using namespace std;

int main() {
    
    freopen("inp.txt", "r", stdin);
    freopen("opt.txt", "w", stdout);
    
    int t;
    cin >> t;
    for(int q = 0; q<t; ++q) {
        
        string s;
        int k;
        cin >> s;
        cin >> k;
        vector<char> str(s.c_str(), s.c_str() + s.length());
        
        int l = str.size(), count = 0;
        
        for(int i = 0; i<l-k+1; ++i) {
            if(str[i] == '-') {
                for(int j=i; j<i+k; ++j) {
                    if(str[j] == '-') {
                        str[j] = '+';
                    }
                    else {
                        str[j] = '-';
                    }
                }
                count++;
            }
        }
                
        int flag = 1;
        for(int i = 0; i<l; ++i) {
            if(str[i] == '-') {
                flag = 0;
                break;
            }
        }

        if(flag) {
            cout << "Case #" << q+1 << ": " << count << endl;
        }
        else {
            cout << "Case #" << q+1 << ": IMPOSSIBLE" << endl;
        }
    }

    return 0;
}
