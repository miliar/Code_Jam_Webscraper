#include <iostream>
#include <string>
#include <vector>
#include <map>

#define ll long long

using namespace std;

int main() {
    int t, test = 0;
    cin >> t;
    while(t--){
        test++;
        int n,out = 0;
        string s;
        cin >> s >> n;
        for (int i = 0; i <= s.size()-n; ++i) {
            if(s[i] == '-'){
                out++;
                for (int j = i; j < i+n; ++j) {
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        bool je = true;
        for (int i = 0; i < s.size(); ++i) {
            if(s[i] == '-'){
                je = false;
                break;
            }
        }
        cout << "Case #" << test << ": ";
        if(!je) cout << "IMPOSSIBLE";
        else cout << out;
        cout << endl;
    }
    return 0;
}