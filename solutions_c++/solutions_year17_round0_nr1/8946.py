#include <cstdio>
#include <cstring>
using namespace std;
char str[1010];
bool s[1010];
int k,len;
inline void solve() {
    int ans=0;
    scanf("%s%d",str,&k);
    len=strlen(str);
    for (int i=0; i<len; i++)
        s[i]=(str[i]=='-');
    for (int i=0; i+k-1<len; i++) {
        if (s[i]) {
            for (int j=i; j<i+k; j++)
                s[j]=(!s[j]);
            ans++;
        }
    }
    bool flag=true;
    for (int i=0; i<len; i++)
        if (s[i]) {
            flag=false;
            break;
        }
    if (flag) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
}
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int tcas=1; tcas<=T; tcas++) {
        printf("Case #%d: ",tcas);
        solve();
    }
    return 0;
}