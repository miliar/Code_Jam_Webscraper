#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
#define TASK "B-large"
    freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
    int t;
    cin >> t;
    for(int cs = 1; cs <= t; ++cs){
        string ans;
        cin >> ans;
        for(int l = 1; l < ans.size(); ++l){
            if(ans[l - 1] > ans[l]) {
                for(l = l - 1; l >= 0 && ans[l] > ans[l + 1]; --l) ans[l] -= 1;
                if(ans[0] == '0') {
                    ans.pop_back();
                    for(char &c : ans) c = '9';
                } else {
                    for(int i = l + 2; i < ans.size(); ++i) ans[i] = '9';
                }
                break;
            }
        }
        cout << "Case #" << cs << ": " << ans << "\n";
    }
    return 0;
}
