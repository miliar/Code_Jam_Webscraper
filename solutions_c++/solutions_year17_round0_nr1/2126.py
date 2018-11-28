#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)

int solve() {
    char s[5000];
    int k;
    scanf("%s %d\n",s,&k);
    int l = strlen(s);
    FOR(i,l) s[i] = s[i]=='+'? 1 : 0;
    
    int result = 0;
    for(int i=l-1; i>=(k-1);--i) {
     if (s[i]==0) {
         ++result;
         for(int j=0;j<k;++j) {
             s[i-j]^=1;
         }
     }
     
    }
    for(int i=0; i<k;++i) {
        if (s[i]!=1) return -1;
    }
    return result;
    
}


int main(void) {
    int t;
    scanf("%d\n",&t);
    FOR(i,t) {
        printf("Case #%d: ", i+1);
        int ans = solve();
        if (ans==-1) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    
}
