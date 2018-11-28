#include<bits/stdc++.h>
using namespace std;
int T,k,a[10100];
char s[10100];
int main(){
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
        scanf("%s",&s);
        scanf("%d",&k);
        int ans=0;
        int n=strlen(s);
        for(int i=0;i<n;i++) if (s[i]=='-') a[i]=0;else a[i]=1;
        for (int i=0;i<=n-k;i++){
            if (a[i]==0){
                for (int j=i;j<=i+k-1;j++) a[j]^=1;
                ans++;
            }
        }
        for(int i=0;i<n;i++) if (a[i]==0) ans=-1;
        if (ans==-1)
            printf("Case #%d: IMPOSSIBLE\n",cas);
        else
            printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
