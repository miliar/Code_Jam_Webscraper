#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <deque>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <complex>
#include <cstring>
#include <cassert>
#include <bitset>

using namespace std;
#define rep(i, a, b) for(int i = (a); i < (b); i++)
#define repd(i, a, b) for(int i = (a); i > (b); i--)
#define forIt(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define forRev(it, a) for(__typeof((a).rbegin()) it = (a).rbegin(); it != (a).rend(); it++)
#define ft(a) __typeof((a).begin())
#define ll long long
#define ld long double
#define fi first
#define se second
#define mk make_pair
#define pb push_back
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define Rep(i,n) for(int i = 0; i < (n); ++i)
#define bitcount(n) __builtin_popcountll(n)


typedef complex<ld> cplex;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef vector<iii> viii;

const int N = 50 + 7;
const int M = 20;
const int inf = 1e9 + 7;
const long long linf = 1e18 + 7;
const double pi = acos(-1);
const double eps = 1e-7;
const bool multipleTest = 1;

int n, p;

vii list[N];

int r[N];
int pj[N];
int oldj[N];

int dp[2][1 << 8];

bool giao(ii a, ii b) {
    if (a.first > b.first) swap(a, b);
    if (b.first > a.second) return false;
    return true;
}

void solve() {
    cin >> n >> p;
    for(int i = 0; i < n; ++i) {
        scanf("%d", r + i);
        list[i].clear();
        pj[i] = 0;
    }
    
    set<int> st;
    
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < p; ++j) {
            int u; scanf("%d", &u);
            
            int k2 = u * 10 / 9 / r[i];
            while (k2 * r[i] * 9 > u * 10) -- k2;
            while ((k2 + 1) * r[i] * 9 <= u * 10) ++k2;
            
            
            int k = u * 10 / 11 / r[i];
            while (k * r[i] * 11 < u * 10) ++k;
            while ((k - 1) * r[i] * 11 >= u * 10) --k;
            
            if (k <= k2) {
                list[i].push_back(mk(k, k2));
                st.insert(k);
                st.insert(k2);
            }
        }
        sort(list[i].begin(), list[i].end());
//        for(ii x : list[i]) {
//            cout << x.first << ' ' << x.second << " : ";
//        }
//        puts("");
    }
    
    
    if (st.count(0)) st.erase(0);
    int ans = 0;
    
    for(int x : st) {
        bool ok = true;
//        if (x == 9) {
//            cout << pj[0] << ' ' << pj[1] << '\n';
//        }
        while (ok) {
            rep(t, 0, n) oldj[t] = pj[t];
            for(int i = 0; i < n; ++i) {
                int &j = pj[i];
                while (j < list[i].size() && list[i][j].second < x) ++j;
                if (j < list[i].size() && list[i][j].first <= x && x <= list[i][j].second) {
                    ++j;
                } else {
                    ok = false;
                    break;
                }
            }
            if (ok) ++ans;
            else {
                rep(i, 0, n) pj[i] = oldj[i];
            }
        }
    }
    cout << ans << '\n';
    
//    if (n > 1) {
//        
//        rep(mask, 0, 1 << p) dp[2][mask] = 0;
//        int cur = 0;
//        int mx = 0;
//        
//        for(int j = 0; j < list[1].size(); ++j) {
//            int pre = cur;
//            cur ^= 1;
//            rep(mask, 1, 1 << list[0].size()) {
//                dp[cur][mask] = 0;
//                rep(t, 0, list[0].size()) if (mask & (1 << t)) {
//                    if (giao(list[0][t], list[1][j])) {
//                        dp[cur][mask] = max(dp[cur][mask], dp[pre][mask ^ (1 << t)] + 1);
//                    }
//                }
//                mx = max(mx, dp[cur][mask]);
//            }
//        }
//        
//        cout << mx << '\n';
//        
//    } else cout << ans << '\n';
    
    
}


int main() {
#ifdef _LOCAL_
    freopen("in.txt", "r", stdin);
#endif
    
    freopen("out.txt", "w", stdout);

    
    int Test = 1;
    if (multipleTest) {
        cin >> Test;
    }
    for(int i = 0; i < Test; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
    }
    
#ifdef _LOCAL_
//    cout<<"\n" << 1.0 * clock() / CLOCKS_PER_SEC <<endl;
#endif
}
