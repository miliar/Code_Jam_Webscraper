// Author: Wang, Yen-Jen
#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 1000 + 7;

int tag[MAX_N];

int main() {
    int T;
    cin >> T;
    for(int kcase = 1; kcase <= T; kcase++) {
        int k;
        string s;
        cin >> s >> k;
        int n = (int)s.size();
        for(int i = 0; i <= n; i++) tag[i] = 0;
        int t = 0 , ans = 0;
        for(int i = 0; i < n; i++) {
            t ^= tag[i];
            if(s[i] == '+') {
                if(t == 1) {
                    if(i + k - 1 >= n) {
                        ans = -1;
                        break;
                    }
                    t ^= 1;
                    tag[i + k] = 1;
                    ans++;
                }
            }
            else {
                if(t == 0) {
                    if(i + k - 1 >= n) {
                        ans = -1;
                        break;
                    }
                    t ^= 1;
                    tag[i + k] = 1;
                    ans++;
                }
            }
        }
        printf("Case #%d: ",kcase);
        if(ans == -1) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
