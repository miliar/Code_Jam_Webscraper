#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
typedef long long ll;

int T;

int n, p, g[123];

map<vector<int>,int> ch[5][5];
int dp(int p, int sum, vector<int> cnt) {
    int brk = 1;
    for (int x : cnt) if (x) brk = 0;
    if (brk) return 0;
    if (ch[p][sum].find(cnt) != ch[p][sum].end()) return ch[p][sum][cnt];

    int res = 99999;
    fo(i,0,p) if (cnt[i]) {
        vector<int> adv(cnt);
        adv[i]--;
        res = min(res, dp(p, (sum+i)%p, adv));
    }
    if (sum) res++;
    return ch[p][sum][cnt] = res;
}
int main() {
    scanf("%d", &T);
    fo(_,1,T+1) {
        printf("Case #%d: ", _);

        scanf("%d %d", &n, &p);
        fo(i,0,n) scanf("%d", g+i);

        vector<int> cnt;
        fo(i,0,p) cnt.pb(0);
        fo(i,0,n) cnt[g[i]%p]++;

        printf("%d\n", n - dp(p, 0, cnt));
    }

    return 0;
}
