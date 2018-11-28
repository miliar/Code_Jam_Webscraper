#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
//#pragma comment(linker, "/STACK:1024000000,1024000000")

using namespace std;

#define ll long long
#define SZ(x) ((int)(x).size()) 
#define ALL(v) (v).begin(), (v).end()
#define foreach(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++ i)
#define reveach(i, v) for (__typeof((v).rbegin()) i = (v).rbegin(); i != (v).rend(); ++ i) 
#define REP(i,a,n) for ( int i=a; i<int(n); i++ )
#define FOR(i,a,n) for ( int i=n-1; i>= int(a);i-- )
#define lson rt<<1, L, m
#define rson rt<<1|1, m, R
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define fi first
#define se second
#define CLR(a, b) memset(a, b, sizeof(a))
#define Max(a, b) a = max(a, b)
#define Min(a, b) a = min(a, b)
#define lowbit(x) (x) & (-(x))

ll n, k;

struct Node{
    ll l, r;
    ll m;
    ll mi, mx;
    int flag;
    Node(ll l, ll r): l(l), r(r){
        m = (l + r) / 2;
        flag = (l + r) & 1;
        mi = m - l;
        mx = r - m;
    }
    bool operator < (const Node& t) const{
        return (mi > t.mi) || (mi == t.mi && mx > t.mx) || (mi == t.mi && mx == t.mx && l < t.l);
    }
};
set<Node> st;
int main(){
#ifdef LOCAL_TEST
	freopen("in.txt","r",stdin);
#endif
	freopen("out.txt","w",stdout);
    int T, kase = 0;
    scanf("%d", &T);
    while(T --){
        scanf("%lld%lld", &n, &k);
        st.clear();
        st.insert(Node(1, n));
        REP(i, 1, k){
            auto it = st.begin();
            Node t = (*it);
            //printf("l = %lld, r = %lld\n", t.l, t.r);
            st.erase(it);
            //printf("l = %lld, r = %lld\n", t.l, t.r);
            if(t.m > t.l){
                st.insert(Node(t.l, t.m - 1));
            }
            if(t.m < t.r){
                st.insert(Node(t.m + 1, t.r));
            }
        }
        printf("Case #%d: ", ++ kase);
        auto it = st.begin();
        Node t = (*it);
        printf("%lld %lld\n", t.r - t.m, t.m - t.l);
    }
    return 0;
}
