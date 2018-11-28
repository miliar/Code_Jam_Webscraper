#include <cstdio>
#include <cstring>
using namespace std;
const int L = 10000;
char str[L+10];
int main(){
    freopen("A-large.in", "r", stdin);
//    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int cas=1; cas<=test; cas++){
        scanf("%s", str+1);
        int k;
        scanf("%d", &k);
        int len = strlen(str+1);
        int ans = 0;
        for (int i=1; i<=len-k+1; i++) if (str[i] == '-'){
            for (int j=0; j<k; j++)
                str[i+j] = str[i+j] == '+' ? '-' : '+';
            ans ++;
        }
        for (int i=1; i<=len; i++) if (str[i] == '-'){
            ans = -1;
        }
        if (ans == -1) printf("Case #%d: IMPOSSIBLE\n", cas);
        else printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
