#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <random>
#include <functional>

using namespace std;

#define F first
#define S second
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define db3(x, y, z) cerr << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", " << z << ")\n"
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)a.size()
#define pw(n) (1ll << (n))

#define equal equalll
#define less lesss
const int N = -1;
const long long INF = 1e9 + 19;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef double dbl;


struct State {
    ll l, r;
    bool operator < (State o) const {
        if (min(l, r) != min(o.l, o.r)) return min(l, r) > min(o.l, o.r);
        return max(l, r) > max(o.l, o.r);
    }
};

State makeState(ll l, ll r) {
    ll len = r - l;
    ll pos = l + len / 2;
    return {pos - l, r - pos};
}

State build(ll len) {
    return {(len - 1) / 2, len - 1 - (len - 1) / 2};
}

int main(){
#ifdef HOME 
    assert(freopen("in", "r", stdin));
    //freopen("C.out", "w", stdout);
    freopen("C.out1", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++) {
        //db(tt);
        ll n, k;
        printf("Case #%d: ", tt + 1);
        cin >> n >> k;
        map<State,ll> q;        
        q[build(n)] = 1;
        for (; k >= 0; ) {
            //db(q.size());
            ll l = q.begin()->F.l;
            ll r = q.begin()->F.r;
            ll cnt = q.begin()->S;
            q.erase(q.begin());
            if (cnt >= k) {
                cout << r << " " << l << endl; 
                break;
            }
            k -= cnt;
            q[build(l)] += cnt;
            q[build(r)] += cnt;
        }
        //cout << q.begin()->r - 1 << " " << q.begin()->l - 1 << endl;
    }


    
    
#ifdef HOME 
    epr("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
#endif
    return 0;
}

