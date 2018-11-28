#include <bits/stdc++.h>

#define st first
#define nd second
#define pb push_back
#define mp make_pair

#define cl(x,y) memset(x, y, sizeof(x))
#define dbs(x) cerr << x << endl;
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;

const int INF = 0x3f3f3f3f, MOD = 1e9+7;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const double PI=acos(-1), EPS = 1e-9;
const int N = 1e5+9;

int main () {
    int T;
    scanf("%d", &T);
    for(int t = 1; t<=T; t++) {
        ll n, k;
        scanf("%lld %lld", &n, &k);
        //priority_queue<pll> q;
        //q.push(mp(n,1));
        map<ll,ll> m;
        m[n] = 1;
        while(k) {
            auto p = *(m.rbegin());
            ll x = p.st, y = p.nd;
            m.erase(x);
            //printf("x: %lld y: %lld\n", x,y);
            k -= min(k,y);
            m[(x-1)/2]+=y, m[x/2]+=y;
            if(!k)
                printf("Case #%d: %lld %lld\n", t, x/2, (x-1)/2);
        }
    }

    return 0;
}
