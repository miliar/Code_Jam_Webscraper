#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9+10;
int T;
int k;
string s;

int solve(int idx) {
    int ret = 0;
    if(idx == k-1) {
        bool possible = true;
        for(int i=0;i<idx;i++) {
            if(s[i] != s[i+1]) possible = false;
        }
        if(!possible) return -INF;
        else {
            if(s[idx] == '-') return 1;
            else return 0;
        }
    }


    if(s[idx] == '-') {
        for(int i=idx-k+1;i<idx;i++) {
            if(s[i] == '-') s[i] = '+';
            else s[i] = '-';
        }         
        return solve(idx-1) + 1;
    } else {
        return solve(idx-1);
    }
}

int main() {
    cin >> T;
    for(int i=1;i<=T;i++) {
        cin >> s >> k;
        int ans = solve(s.size()-1);
        if(ans >= 0) cout << "Case #" << i << ": " << ans << endl;
        else cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    }
}
