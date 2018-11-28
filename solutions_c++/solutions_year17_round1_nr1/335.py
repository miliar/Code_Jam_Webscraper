#include <bits/stdc++.h>
using namespace std;

char mp[30][30];
int whole[30];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++) {
        int n,m;
        scanf("%d%d",&n,&m);
        memset(whole,0,sizeof(whole));
        for (int i=0;i<n;i++) {
            scanf("%s",mp[i]);
            int j=0;
            while (j<m&&mp[i][j]=='?') j++;
            if (j<m) {
                for (int k=0;k<j;k++) {
                    mp[i][k]=mp[i][j];
                }
                for (int k=j+1;k<m;k++) {
                    if (mp[i][k]=='?') mp[i][k]=mp[i][k-1];
                }
            } else {
                whole[i]=1;
            }
        }
        int i=0;
        while (whole[i]) i++;
        for (int j=0;j<i;j++) {
            strcpy(mp[j],mp[i]);
        }
        for (int j=i+1;j<n;j++) {
            if (whole[j]) {
                strcpy(mp[j],mp[j-1]);
            }
        }
        printf("Case #%d: \n",cas);
        for (int i=0;i<n;i++) {
            puts(mp[i]);
        }
    }
    return 0;
}
