#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
using namespace std;
typedef long long ll;
const int inf = 1e9;
const ll infLL = 1e18;

int i, j, k, t, len, T;
char a[1005];
int main() {
    freopen("asmall.in","r",stdin);
    freopen("asmall.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    scanf ("%d",&T);
    for (int z = 1; z <= T; z++) {
        int cnt = 0;
        int ch = 0;
        scanf (" %s",&a[1]);
        scanf ("%d",&k);
        len = strlen (&a[1]);
        for (i = 1; i <= len-k+1; i++) {
            int j = i+k-1;
            if (a[i] == '-') {
                for (t = i; t <= j; t++) {
                    a[t] = (a[t]=='-') ? '+' : '-';
                }
                cnt++;
            }
        }
        for (i = 1; i <= len; i++) {
            if (a[i] == '-') {
                ch = 1; break;
            }
        }
        if (ch) printf("Case #%d: IMPOSSIBLE\n",z);
        else printf("Case #%d: %d\n",z,cnt);
    }
    return 0;
}
