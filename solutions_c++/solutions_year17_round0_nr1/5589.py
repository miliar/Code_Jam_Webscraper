#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t <<": ";
        int k;
        string str;
        cin >> str;
        cin >> k;
        int len = str.size();
        int pan = 0;
        int turn = (1<<k)-1;
        for(int i = 0; i < len; ++i) {
            pan <<= 1;
            if(str[i] == '-') pan |= 1;
        }
        int ans = 0;
        for(int i = 0; i < len-k+1; ++i) {
            if(pan & 1) {
                pan ^= turn;
                ans++;
            }
            pan >>= 1;
            if(!pan) break;
        }
        if(pan) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
    return 0;
}
