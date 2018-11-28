#include <bits/stdc++.h>
using namespace std;

int solve() {
    string pan;
    string target;
    int k;
    cin >> pan >> k;
    
    target = pan;
    for (int i=0;i<target.size();++i) target[i]='+';
    
    int bits = pan.size() - k + 1;
    int ans = 1000000000;
    for (int i=0; i<(1<<bits); ++i) {
        string tmp = pan;
        int totalBit = 0;
        for (int bit=0; bit<bits; ++bit) {
            if ((1<<bit) & i) {
                totalBit++;
                for (int j=bit; j<bit+k; ++j) {
                    if (tmp[j]=='+') 
                        tmp[j]='-';
                    else 
                        tmp[j]='+';
                }
            }
        }
        if (tmp==target) {
            ans = min(ans, totalBit);
        }
    }
    if (ans==1000000000) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
}

int main() {
    int ntest;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
