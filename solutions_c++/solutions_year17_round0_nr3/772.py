#include <bits/stdc++.h>
using namespace std;

#define REPU(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a); i > (b); --i)
#define FOREACH(it, a) for (auto it = a.begin(); it != a.end(); ++it)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())

typedef long long ll;
const int MOD = 1000000007;

template<class T, class U> inline T tmin(T a, U b) { return (a < b) ? a : b; }
template<class T, class U> inline T tmax(T a, U b) { return (a > b) ? a : b; }
template<class T, class U> inline void amax(T &a, U b) { if (b > a) a = b; }
template<class T, class U> inline void amin(T &a, U b) { if (b < a) a = b; }
template<class T> inline T tabs(T a) { return (a > 0) ? a : -a; }
template<class T> T gcd(T a, T b) { while (b != 0) { T c = a; a = b; b = c % b; } return a; }

int main(int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);
    
    int ntest; cin >> ntest;
    REPU(it, 1, ntest + 1) {
        ll n, k; cin >> n >> k;
        set<ll> st; map<ll, ll> mp;
        st.insert(-n - 1); mp[-n - 1] = 1;
        ll ans = 2;
        while (k > 0) {
            ll mx = *st.begin();
            ll cnt = mp[mx];
            st.erase(mx); mp.erase(mx);
            k -= cnt; mx = -mx;
            ll nmx = -((mx + 1) / 2);
            if (nmx <= -2) {
                st.insert(nmx); mp[nmx] += cnt;
            }
            nmx = -(mx / 2);
            if (nmx <= -2) {
                st.insert(nmx); mp[nmx] += cnt;
            }
            if (k <= 0) {
                ans = mx;
            }
        }
        printf("Case #%d: %lld %lld\n", it, (ans - 1) / 2, (ans - 2) / 2);
    }
	
	return 0;
}
