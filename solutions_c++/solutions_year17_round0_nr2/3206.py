#include <bits/stdc++.h>
using namespace std;
#define prt(k) cout<<#k" = "<<k<<"   ";
#define pln(k) cout<<#k" = "<<k<<endl;
typedef long long LL;
const int MAXN = 1701000 ;
LL p10[234];
LL dp[325][23];
LL A[342];

int bit[234], len;
LL n;
void fj(LL n) {
    len = 0;
    while (n > 0) {
        bit[len++] = n % 10;
        n /= 10;
    }
}
bool check(LL n) {
    int bit[234], len;
    len = 0;
    while (n > 0) {
        bit[len++] = n % 10;
        n /= 10;
    }
    for (int i=len-1;i>0;i--)
    if (bit[i] > bit[i-1]) {
        return false;
    }
    return true;
}
LL dfs(int last, LL now, int pos, bool lim) {
    if (pos == -1) {
        return now;
    }
    if (pos!=-1 && ~dp[last][pos]) return dp[last][pos];
    int ed = lim ? bit[pos] : 9;
    for (int i=last;i<=ed;i++) {

    }
}

int main()
{
    p10[0] = 1;
    for (int i=1;i<=18;i++) p10[i] = p10[i-1]*10;
    int re, ca = 1; cin>>re;
    while (re--) {
        cin >> n;
        fj(n);
        LL tot = 0;
        A[0] = n;
        tot = check(n) ? n : 0;
        for (int first=len-1;first>0;first--) {
            int i;
            LL ans = 0;
            for (i=len-1;i>first;i--) ans = ans * 10 + bit[i] ;
            ans = ans * 10 + bit[i--] - 1;
            for (; i>=0; i--) ans = ans * 10 + 9;
            if (check(ans)) tot = max(tot , ans);

        }
        printf("Case #%d: %lld\n", ca++, tot);
    }
}
