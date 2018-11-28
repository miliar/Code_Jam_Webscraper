#include <bits/stdc++.h>
using namespace std;

char s[1010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1; t<=T; t++) {
        int k,ans=0;
        scanf("%s%d",s,&k);
        int n=strlen(s);
        for (int i=0; i<n; i++) {
            if (i+k>n) break;
            if (s[i]=='+') continue;
            for (int j=0; j<k; j++) {
                if (s[i+j]=='-') s[i+j]='+';
                else s[i+j]='-';
            }
            ans++;
        }
        for (int i=0; i<n; i++) {
            if (s[i]=='-') {
                ans=-1;
                break;
            }
        }
        printf("Case #%d: ",t);
        if (ans==-1) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n",ans);
        }
    }
    return 0;
}
