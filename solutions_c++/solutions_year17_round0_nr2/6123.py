#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
#define ll long long
int main () {
    freopen("/Users/bowbowbow/Downloads/B-large.in", "r", stdin);
    freopen("/Users/bowbowbow/Desktop/B.out", "w", stdout);
    int T;
    cin >> T;
    for(int t=1;t<=T;t++) {
        ll N;
        cin >> N;
        
        cout << "Case #" << t << ": ";
        
        string ans = "";
        while(1) {
            bool flag = true;
            string str = to_string(N);
            for(int i=0;i<str.size()-1;i++) {
                if(str[i] > str[i+1]) {
                    flag = false;
                    break;
                }
            }
            if(flag) break;
            
            N /= 10;
            N--;
            
            ans += "9";
        }
        if(N) cout << N;
        reverse(ans.begin(), ans.end());
        cout << ans << endl;
    }
    return 0;
}
