#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl "\n"
#define cv(c) (int)(c-'a')
#define db(x) cerr << #x << ": " << x << " "
#define db2(x, y) cerr << #x << ": " << x << " " << #y << ": " << y << " "
#define bn() cerr << endl
#define sep() cerr << "-------" << endl
#define inf 1000000002
#define linf 1000000000000000002
#define pi acos(-1)

using namespace std;
typedef long long ll;
typedef long double ld;

ld stot = 0;
pair<ll, ll> v[1003];

ld areaLateral(pair<ll, ll> a){
    return (ld)a.fi * 2 * pi * (ld)a.se;
}
ld area(pair<ll, ll> a){
    return areaLateral(a) + pi * (ld)a.se * (ld)a.se;
}
bool cmp(pair<ll, ll> a, pair<ll, ll> b){
    return areaLateral(a) > areaLateral(b);
}
int main(){
    ios::sync_with_stdio(false);
    freopen("A-Large.in", "r", stdin);
    freopen("ou", "w", stdout);

    int te;
    cin >> te;
    int caso = 1;
    while(te--){
        stot = 0;
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < n; i++){
            cin >> v[i].se >> v[i].fi;
        }

        sort(v, v + n, cmp);
        int indmx = -1;
        int rmx = 0;
        int ind = -1;
        ld mx = 0;
        if (k == 1){
            for (int i = 0; i < n; i++){
                mx = max(mx, area(v[i]));
            }
            cout << setprecision(12) << fixed;
            cout << "Case #" << caso << ": " << mx << endl;
            caso++;
            continue;
        }
        for (int i = 0; i < k - 1; i++){
            stot += areaLateral(v[i]);
            if (v[i].se > rmx){
                rmx = v[i].se;
                indmx = i;
            }
        }
        stot -= areaLateral(v[indmx]);
        stot += area(v[indmx]);
        //cout << indmx << endl;
        //cout << stot << endl;
        ld res = stot;
        for (int i = k - 1; i < n; i++){
            if (rmx <= v[i].se){
                //cout << 123123 << " " << stot - area(v[indmx]) + area(v[i]) + areaLateral(v[indmx]) << endl;
                res = max(res, stot - area(v[indmx]) + area(v[i]) + areaLateral(v[indmx]));
            }
            else{
                //cout << 234234 << endl;
                res = max(res, stot + areaLateral(v[i]));
            }
        }
        cout << setprecision(12) << fixed;
        cout << "Case #" << caso << ": " << res << endl;
        caso++;
    }
    return 0;
}

