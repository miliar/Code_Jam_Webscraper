#include<bits/stdc++.h>
using namespace std;
int main() {
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
    int t;
    cin >> t;
    for(int cnt = 1; cnt <= t; cnt++) {
        string s;
        int k;
        cin >> s >> k;
        int num[1010];
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '-')
                num[i] = 0;
            else
                num[i] = 1;
        }
        int flag = 0;
        int ans = 0;
        for(int i = 0; i < s.size(); i++) {
            if(num[i] == 0) {
                ans++;
                if(i + k > s.size()) {
                    flag = -1;
                    break;
                }
                for(int j = i; j < i + k; j++)
                    num[j] ^= 1;
            }
        }
        cout << "Case #" << cnt << ": ";
        if(flag == -1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ans << endl;
    }

    return 0;
}
