#include <iostream>
#include <cstdio>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long ll;

int main() {
    int T;
    scanf("%d", &T);
    for (int c = 1; c <= T; c++) {
        ll n, k, odd, eve, cnt = 0, po = 0;
        map<ll, ll> mp;
        scanf("%lld %lld", &n, &k);
        if (n % 2 == 0) { odd = n / 2 - 1; eve = n / 2; }
        else { odd = (n - 1) / 2; eve = (n - 1) / 2; }
        if (odd > eve) swap(odd, eve);
        mp[odd] = 0; mp[eve] = 0;
        mp[odd] += 1; mp[eve] += 1;
        cnt += pow(2, po);
        while (cnt < k) {
            ll a, b, c, d, cnt_a = 0, cnt_b = 0, cnt_c = 0, cnt_d = 0;
            if (odd % 2 == 0 && odd != 0) { a = odd / 2 - 1; b = odd / 2; }
            else { a = odd / 2; b = odd / 2; }
            cnt_a += mp[odd];
            cnt_b += mp[odd];
            //cout << mp[a] << " " << mp[b] << endl;
            if (eve % 2 == 0 && eve != 0) { c = eve / 2 - 1; d = eve / 2; }
            else { c = eve / 2; d = eve / 2; }
            if (odd != eve) { cnt_c += mp[eve]; cnt_d += mp[eve]; }
            ll tmp1 = min(a, b), tmp2 = min(c, d);
            mp[odd] = 0; mp[eve] = 0;
            odd = min(tmp1, tmp2);
            tmp1 = max(a, b), tmp2 = max(c, d);
            eve = max(tmp1, tmp2);
            mp[a] += cnt_a; mp[b] += cnt_b;
            mp[c] += cnt_c; mp[d] += cnt_d;
            po++;
            cnt += pow(2, po);
            //cout << mp[odd] << " " << mp[eve] << endl;
            //cout << odd << " " << eve << endl;
            //cout << mp[odd] << " " << mp[eve] << endl;
            //cout << endl;
        }
        ll count = cnt - k;
        ll cur = pow(2, po);
        //cout << cnt  << " " << cur  << " " << count << endl;
        //eve > odd
        
        printf("Case #%d: ", c);
        if (mp[eve] > cur) {
            int res = mp[eve] - cur;
            //cout << res  << " " << count << endl;
            if (res >= cur - count) cout << eve << " " << eve << endl;
            else cout << eve << " " << odd << endl;
        }
        else if (mp[eve] >= cur - count) cout << eve << " " << odd << endl;
        else cout << odd << " " << odd << endl;
        
    }
}