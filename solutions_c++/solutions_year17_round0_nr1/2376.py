#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

char s[1005];
int test, ans, k, slen;

void solve() {
    ans = 0;
    slen = strlen(s);
    int i;
    for (i = 0; (i+k) <= slen; ++i) {
        if (s[i] == '-') {
            for(int j = 0; j < k; ++j)
                s[i+j] = (s[i+j] == '+' ? '-' : '+');
            ++ans;
        }
    }
    for (; i < slen; ++i) {
        if (s[i] == '-')
            ans = -1;
    }
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&test);
    for (int t = 1; t <= test; ++t) {
        scanf("%s %d",s,&k);
        solve();
        if (ans != -1)
            printf("Case #%d: %d\n",t,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",t);
    }
    return 0;
}
