#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t, k, sz, ans;
    bool f;
    string s;

    scanf("%d", &t);
    getchar();

    for(int C=1; C<=t; C++) {
        f = true;
        ans = 0;
        cin >> s;
        sz = s.size();
        scanf("%d", &k); k--;
        getchar();
        for(int i=0; i < sz; i++) {
            if(s[i] == '+') continue;
            if(i+k >= sz) {
                f = false;
                break;
            }
            for(int j=i; j<= i+k; j++) {
                if(s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
            ans++;
        }
        printf("Case #%d: ", C);
        if(!f) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
}
