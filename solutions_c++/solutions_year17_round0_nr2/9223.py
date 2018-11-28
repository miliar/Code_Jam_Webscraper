#include <cstdio>
#include <cstring>
using namespace std;
typedef unsigned long long ULL;
int len;
char str[25];
inline bool judge(ULL n) {
    sprintf(str,"%llu",n);
    len=strlen(str);
    for (int i=1; i<len; i++)
        if (str[i]<str[i-1]) return false;
    return true;
}
inline void solve() {
    ULL n;
    scanf("%llu",&n);
    while (!judge(n))
        n--;
    printf("%llu\n",n);
}
int main() {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int tcas=1; tcas<=T; tcas++) {
        printf("Case #%d: ",tcas);
        solve();
    }
    return 0;
}