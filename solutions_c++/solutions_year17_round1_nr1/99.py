#include <bits/stdc++.h>

using namespace std;

int t,tes,i,n,m,j;
char s[107][107];

int main() {
    scanf("%d",&t);
    for (tes=1 ; tes<=t ; tes++) {
        scanf("%d%d",&n,&m);
        for (i=0 ; i<n ; i++) {
            scanf("%s",&s[i]);
        }
        
        for (i=0 ; i<n ; i++) {
            for (j=1 ; j<m ; j++) {
                if (s[i][j] == '?' && s[i][j-1] != '?') s[i][j] = s[i][j-1];
            }
        }
        for (i=0 ; i<n ; i++) {
            for (j=m-2 ; j>=0 ; j--) {
                if (s[i][j] == '?' && s[i][j+1] != '?') s[i][j] = s[i][j+1];
            }
        }
        for (j=0 ; j<m ; j++) {
            for (i=1 ; i<n ; i++) {
                if (s[i][j] == '?' && s[i-1][j] != '?') s[i][j] = s[i-1][j];
            }
        }
        for (j=0 ; j<m ; j++) {
            for (i=n-2 ; i>=0 ; i--) {
                if (s[i][j] == '?' && s[i+1][j] != '?') s[i][j] = s[i+1][j];
            }
        }
        
        printf("Case #%d:\n",tes);
        for (i=0 ; i<n ; i++) printf("%s\n",s[i]);
    }
}
