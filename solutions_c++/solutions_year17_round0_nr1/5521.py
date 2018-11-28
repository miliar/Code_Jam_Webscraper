#include "bits/stdc++.h"
using namespace std;
const int N = 2e6 + 6;
int n , k;
int arr[N];
string s;
int main() {
    int tt;
    freopen("codejam1.txt" , "r" , stdin);
    freopen("codejamout1.txt" , "w" , stdout);
    cin >> tt;
    for(int qq = 1; qq <= tt; ++qq) {
        cin >> s >> k;
        cout << "Case #" << qq << ": ";
        n = (int) s.size();
        int cnt = 0;
        for(int i = 0; i + k - 1 < n; ++i) {
            if(s[i] == '-') {
                for(int j = i; j <= i + k - 1; ++j) {
                    s[j] = s[j] ^ '+' ^ '-';
                }
                ++cnt;
            }
        }
        bool can = true ;
        for(int i = 0; i < n; ++i) {
            can &= (s[i] == '+');
        }
        if(!can) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << cnt << endl;
        }
    }
    return 0;
}
