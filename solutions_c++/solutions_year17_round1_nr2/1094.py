#include <bits/stdc++.h>

#define ll long long
using namespace std;
ifstream f("d.in");
ofstream g("d.out");

struct statuss{
    ll nr, ind;
};

const ll NMax = 55;

ll t,n,m,tmax,tmin,servingsmin,servingsmax,ans;
ll ingr[NMax],st[NMax],fol[NMax];
ll q[NMax][NMax];

void verificare(ll k){
    ll nr = 0;
    for(ll j = 1; j <= m; ++j){
        ll tmax = q[1][j] * 100 / 90;
        ll tmin = q[1][j] * 100 / 110;

        ll servingsmin = tmin / ingr[1];
        ll servingsmax = tmax / ingr[1];

        for(ll k = max(servingsmin - 1,1LL); k <= servingsmax + 1; ++k){
            ll nec = k * ingr[2];
            ll nec2 = k * ingr[1];

            if(1.0 * nec * 90 / 100 <= 1.0 * q[2][st[j]] && 1.0 * q[2][st[j]] <= 1.0 * nec * 110 / 100 &&
               1.0 * nec2 * 90 / 100 <= 1.0 * q[1][j] && 1.0 *q[1][j] <= 1.0 *nec2 * 110 / 100){
                nr++;
                break;
            }
        }
    }
    ans = max(nr,ans);
}
void back(ll k){
    for(ll i = 1; i <= m; ++i){
        if(fol[i] == 0){
            fol[i] = 1;
            st[k] = i;

            if(k == m){
                verificare(k);
            }else
                back(k + 1);

            fol[i] = 0;
        }
    }
}

int main()
{
    f >> t;
    for(ll testcase = 1; testcase <= t; ++ testcase){
        f >> n >> m;
        for(ll i = 1; i <= n; ++i){
            f >> ingr[i];
        }
        for(ll i = 1; i <= n; ++i){
            for(ll j = 1; j <= m; ++j){
                f >> q[i][j];
            }
        }
        ans = 0;
        if(n == 2)
            back(1);
        else{
            for(ll j = 1; j <= m; ++j){
                ll tmax = q[1][j] * 100 / 90;
                ll tmin = q[1][j] * 100 / 110;

                ll servingsmin = tmin / ingr[1];
                ll servingsmax = tmax / ingr[1];

                for(ll k = max(servingsmin - 1,1LL); k <= servingsmax + 1; ++k){
                    ll nec = k * ingr[1];

                    if(1.0 *nec * 90 / 100 <= 1.0 *q[1][j] && 1.0 *q[1][j] <= 1.0 *nec * 110 / 100){
                        ans++;
                        break;
                    }
                }
            }

        }
        g << "Case #" << testcase << ": "<< ans << '\n';
    }
    return 0;
}


/*

            tmax = q[1][j] * 100 / 90;
            tmin = q[1][j] * 100 / 110;

            servingsmin = tmin / ingr[1];
            servingsmax = tmax / ingr[1];
*/
