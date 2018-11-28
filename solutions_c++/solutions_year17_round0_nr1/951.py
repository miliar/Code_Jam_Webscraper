#include <bits/stdc++.h>

using namespace std;

int t,tes,ans,n,i,j,k;
bool yes;
char s[1007];

int main() {
    scanf("%d",&t);
    for (tes=1 ; tes<=t ; tes++) {
        scanf("%s %d",&s,&k);
        printf("Case #%d: ",tes);
        
        n = strlen(s);
        ans = 0;
        
        for (i=0 ; i+k <= n ; i++) if (s[i] == '-') {
            ans++;
            for (j=0 ; j<k ; j++) {
                if (s[i+j] == '-') s[i+j] = '+'; else s[i+j] = '-';
            }
        }
        
        yes = true;
        for (i=0 ; i<n ; i++) if (s[i] == '-') yes = false;
        if (yes) printf("%d\n",ans); else printf("IMPOSSIBLE\n");
    }
}
