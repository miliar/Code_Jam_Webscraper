#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
const int MAXN = 105;
const ll INF = 10000000000000000ll;
inline ll up(ll a, ll b) { return (a+b-1)/b; }
ll attempt(ll Hc, ll Hd, ll Ad, ll Hk, ll Ak) {
    ll cnt = 0;
    bool heal = 0;
    //printf("%lld %lld %lld %lld %lld: ", Hc, Hd, Ad, Hk, Ak);
    while (Hk > 0) {
        if (Hc <= 0) return INF;
        if (Ad >= Hk) {
            Hk -= Ad;
            ++cnt;
            heal = 0;
        }
        else if (Ak >= Hc) {
            if (heal) return INF;
            Hc = Hd - Ak;
            ++cnt;
            heal = 1;
        }
        else {
            Hk -= Ad;
            Hc -= Ak;
            ++cnt;
            heal = 0;
        }
    }
    //printf("%lld\n", cnt);
    return cnt;
}
ll attempt2(ll Hc, ll Hd, ll Ad, ll Hk, ll Ak) {
    if (Ak == 0) return (Hk+Ad-1)/Ad;
    ll ret = 0;
    if (Hc > 0) {
        ll Tc = (Hc-1)/(Ak);
        if (Tc*Ad >= Hk) return up(Hk, Ad);
        else {
            Hk -= Tc*Ad;
            ret += Tc + 1;
        }
    }
    //restored to full health
    ll T = (Hd-1)/(Ak);
    if (T <= 1) return INF;
    
    ll dc = (T-1)*Ad;
    printf("dc = %lld\n", dc);
    ret += (Hk/dc) * T;
    printf("ret = %lld\n", ret);
    Hk %= dc;
    Hk += Ad - 1;
    ret += Hk % Ad;
    return ret;
}

int TC, Hd, Ad, Hk, Ak, B, D;
int main() {
    scanf("%d", &TC);
    for (int Txn = 1; Txn <= TC; ++Txn) {
        scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
        ll ans = attempt(Hd, Hd, Ad, Hk, Ak);
        ll h = Hd, con = 0;
        for (int debuff = 0; (debuff-1)*D < Ak; ++debuff) {
            //printf("debuff = %d\n", debuff);
            ll ak = max(0, Ak - D*debuff);
            ans = min(ans, attempt(h, Hd, Ad, Hk, ak) + con);
            ll Hc = h, con2 = con;
            if (B > 0) {
                for (int buff = 1; (buff-1)*B+Ad < Hk; ++buff) {
                    //printf("buff = %d\n", buff);
                    ll ad = Ad + buff*B;
                    if (Hc <= ak) {
                        Hc = Hd - ak;
                        ++con2;
                    }
                    if (Hc <= ak) break;
                    Hc -= ak;
                    ++con2;
                    ans = min(ans, attempt(Hc, Hd, ad, Hk, ak) + con2);
                }
            }
            if (D == 0) break;
            /* attempt to debuff ? */
            if (h > max(0, Ak - D*(debuff+1))) {
                h -= max(0, Ak - D*(debuff+1));
                ++con;
                continue;
            }
            else {
                //cure
                h = Hd;
                ++con;
                h -= max(0, Ak-D*debuff);
                
                //buff?
                if (h <= max(0, Ak-D*(debuff+1))) break;
                h -= Ak-D*(debuff+1);
                ++con;
            }
        }
        
        printf("Case #%d: ", Txn);
        if (ans >= INF) puts("IMPOSSIBLE");
        else printf("%lld\n", ans);
    }
}