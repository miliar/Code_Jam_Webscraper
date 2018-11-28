#include <bits/stdc++.h>
using namespace std;
int main() {
    int t;
    string s;
    cin >> t;
    int tc = 1;
    while (t--) {
        cin >> s;
        for (int i = s.size() - 2; i >= 0; i--) {
            if (s[i+1] < s[i]) {
                s[i] -= 1;
                for (int j = i+1; j < s.size(); j++) s[j] = '9';
            }
            
        }
        cout << "Case #" << tc++ << ": ";
        int i = 0;
        for (; i < s.size(); i++){
            if (s[i] != '0') break;
        }
        for (; i < s.size(); i++) cout << s[i];
        cout << endl;
    }
}