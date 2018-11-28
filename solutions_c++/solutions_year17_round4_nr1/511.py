#include<bits/stdc++.h>
#define two(a) (1<<(a))
#define LINF (1ll<<61)
#define EPS (1e-14)
#define Lshift(a,b) (a<<b)
#define Rshift(a,b) (a>>b)
#define rep(a,b) for(a=0 ; a<b ; a++)
#define xrep(a,b,c) for(a=b ; a<c ; a++)
#define INF (1<<29)
#define swap(a,b) ( (a^=b) , (b^=a) , (a^=b) )
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;
int val[10];

void proc(int t) {
    memset(val, 0, sizeof(val));
    int i, j, n, p;
    cin >> n >> p;
    int sum(0);
    rep(i, n) {
        int tmp;
        cin >> tmp;
        sum += tmp;
        val[tmp % p] += 1;
    }
    int ans(val[0]+1);
    if (p == 2) {
        ans += val[1] / 2;
    }
    else if (p == 3) {
        int tmp(min(val[1], val[2]));
        ans += tmp;
        val[1] -= tmp;
        val[2] -= tmp;
        ans += val[1] / 3;
        ans += val[2] / 3;
    }
    else if (p == 4) {
        int tmp(min(val[1], val[3]));
        ans += tmp;
        val[1] -= tmp;
        val[3] -= tmp;
        ans += val[2] / 2;
        val[2] %= 2;
        ans += val[1] / 4;
        ans += val[3] / 4;
        val[1] %= 4;
        val[3] %= 4;
        tmp = min(val[1]/2, val[2]);
        ans += tmp;
        val[1] -= tmp*2;
        val[2] -= tmp;
        tmp = min(val[3]/2, val[2]);
        val[3] -= tmp*2;
        val[2] -= tmp;
        ans += tmp;
    }
    if (sum % p == 0) {
        ans--;
    }

    ans = min(ans, n);
    cout << "Case #" << t << ": " << ans << endl;
}

int main() {
    int t, tt;
    cin >> t;
    xrep(tt, 1, t+1) {
        proc(tt);
    }
}
