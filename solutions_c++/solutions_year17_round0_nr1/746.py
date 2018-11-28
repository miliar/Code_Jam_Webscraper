#include <bits/stdc++.h>
using namespace std;
char ss[10010];
void solve() {
    int n;
    int k;
    scanf("%s %d",ss,&k);
    string s = ss;
    n = s.size();
    int ans = 0;
    for(int i = 0;i < n-k+1;i++) {
        if(s[i] == '-') {
            // flip
            ans++;
            for(int j = 0;j < k;j++) {
                s[i+j] = s[i+j]=='-'?'+':'-';
            }
        }
    }
    for(int i = 0;i < n;i++) {
        if(s[i] == '-') {
            printf("IMPOSSIBLE\n");
            return;
        }
    }
    printf("%d\n",ans);
}
int main() {
    int t;
    scanf("%d",&t);
    for(int i = 0;i < t;i++) {
        printf("Case #%d: ",i+1);
        solve();
    }
}
