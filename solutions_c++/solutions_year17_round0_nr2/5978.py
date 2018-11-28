#include <bits/stdc++.h>

using namespace std;

int main(){

    int T; cin >> T;
    for(int t = 1; t <= T; t++) {
    string s; cin >> s;
    cout << "Case #" << t << ": ";
    int n = s.length();
    bool printed = false;
    for(int i = 0; i+1 < n; i++) {
        if (s[i] > s[i+1]) {
            int j = i;
            while(j > 0 && s[j-1] == s[j]) j--;
            if(j > 0 || s[j] > '1') {
                for(int u = 0; u < j; u++) cout << s[u];
                cout << (char) (s[j] - 1);
                for(int u = j + 1; u < n; u++) cout << '9';
            }
            else {
                for(int u = 1; u < n; u++) cout << '9';
            }
            cout << endl;
            printed = true;
            break;
        }
    }

    if(!printed) cout << s << endl;
    }
    return 0;
}
