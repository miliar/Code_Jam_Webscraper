#include <bits/stdc++.h>

using namespace std;
#define int int64_t
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define endl '\n'

template<typename T>
void sci(T& t) {
    cin >> t;
}

template<typename T, typename... Ts>
void sci(T& t, Ts&... ts) {
    sci(t);
    sci(ts...);
}

#define scid(vars...) int vars; sci(vars)
#ifndef HOME
#define FASTIO cin.tie(nullptr); cout.tie(nullptr); ios_base::sync_with_stdio(false);
#define debug(...)
#define __DEBUG if (0) {
#define DEBUG__ }
#define cerr if (0) cerr
#else //HOME
#define FASTIO
#define debug(...) printf("$"); printf(__VA_ARGS__)
#define __DEBUG
#define DEBUG__
#endif // HOME

#define YN(ans) cout << ((ans) ? "YES" : "NO") << endl

#define forn(i,n)    for (int (i) = 0; (i)<(int)(n); ++(i))
#define forkn(i,k,n) for (int (i) = (int)(k); (i)<(int)(n); ++(i))
#define forit(i,container)    for (auto (i) : container)
#define itout(container)    cout << "\n$"; for (auto _it : container) cout << _it << ' ';

typedef long double ld;
typedef long long ll;

typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pld;

typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<ll> vll;
typedef vector<pll> vpll;
typedef vector<ld> vld;
typedef vector<pld> vpld;

typedef vector<vi> graph;
typedef vector<vpii> wgraph;

#define MAXN 500010
#define inf 2000000000
#define INFLL 2000000000000000000LL
#define MOD 1000000007
#define HASHMOD 793877113
#define SQRT 320
#define PI 3.141592653589

int32_t main(){
    //freopen("out.txt", "w", stdout);
    scid(T);
    forn(time, T){
        int n;
        cin >> n;
        int x = n, k = 0;
        while(x > 0){
            k++;
            x /= 10;
        }
        int ans = 0;
        forn(i, k){
            bool ok = 0;
            int num = 10;
            while(!ok){
                num--;
                int ansn = ans;
                for(int j = i; j < k; ++j){
                    ansn *= 10;
                    ansn += num;
                }
                ok = (ansn <= n);
            }
            ans *= 10;
            ans += num;
        }
        cout << "Case #" << time + 1 << ": ";
        cout << ans << endl;
    }
    return 0;
}
