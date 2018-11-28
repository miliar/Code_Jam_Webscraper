#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)

void solve() {
    char s[100];
    scanf("%s\n",s);
    int l = strlen(s);
    if (l==1) {
        // tidy
        printf("%s\n",s);
        return;
    }
    
    int i = 0;
    while (i < l-1 && s[i] <= s[i+1]) {
        ++i;
    }
    if (i == l-1) {
        // tidy
        printf("%s\n",s);
        return;
    }
    
    while(i>=0) {
        --s[i];
        if(i==0) break;
        if (s[i] < s[i-1]) --i;
        else break;
    }
    for(int j=i+1;j<l;++j) s[j]='9';
    int k = 0;
    while(s[k]=='0') ++k;
    printf("%s\n",s+k);
}


int main(void) {
    int t;
    scanf("%d\n",&t);
    FOR(i,t) {
        printf("Case #%d: ", i+1);
        solve();
    }
    
}
