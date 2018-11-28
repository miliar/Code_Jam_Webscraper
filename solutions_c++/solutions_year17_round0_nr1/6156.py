#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main () {
    freopen("/Users/bowbowbow/Downloads/A-large.in", "r", stdin);
    freopen("/Users/bowbowbow/Desktop/A.out", "w", stdout);
    int T, K;
    cin >> T;
    for(int t=1;t<=T;t++) {
        string str;
        cin >> str >> K;
        
        int ans = 0;
        for(int i=0;i <= str.size()-K;i++) {
            if(str[i] == '-') {
                ans++;
                for(int j=i;j<= i+K-1;j++) {
                    if(str[j]=='-') {
                        str[j] = '+';
                    } else {
                        str[j] = '-';
                    }
                }
            }
        }
        
        bool flag = true;
        for(int i=0; i<str.size(); i++) {
            if(str[i] == '-') {
                flag = false;
                break;
            }
        }
        cout << "Case #" << t << ": ";
        
        if(flag) {
            cout << ans << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
