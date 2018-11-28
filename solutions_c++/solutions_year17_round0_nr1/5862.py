#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int tc, count = 1;
    cin>>tc;
    while (tc--) {
        int k, ans = 0;
        bool imp = false;
        string s;
        cin>>s>>k;
        for (int i=0;i<s.length();i++) {
            if (s[i] == '-') {
                ans++;
                for (int j=i;j<i+k;j++) {
                    if (j == s.length()) {
                        imp = true;
                        break;
                    }
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
            if (imp == true) {
                break;
            }
        }

        cout<<"Case #"<<count++<<": ";
        if (imp) cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;
    }
    return 0;
}