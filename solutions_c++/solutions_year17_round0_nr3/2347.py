#include<bits/stdc++.h>
#define two(a) (1<<(a))
#define LINF (1ll<<61)
#define EPS (1e-14)
#define Lshift(a,b) (a<<b)
#define Rshift(a,b) (a>>b)
#define rep(a,b) for(a=0 ; a<b ; a++)
#define xrep(a,b,c) for(a=b ; a<c ; a++)
#define INF (1<<29)
#define swap(a,b) ( (a^=b) , (b^=a) , (a^=b) )
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;


void proc(int t) {
    int i, j;
    ll n, k;
    map<ll, ll> xmap;
    cin >> n >> k;
    xmap[n] = 1;
    ll minx(-1), maxn(-1);
    while(1) {
        auto rit = xmap.crbegin();
        ll value = rit->first;
        ll count = rit->second;
        // xmap.erase(rit);
        xmap.erase(rit->first);
        --value;
        minx = value / 2;
        maxn = minx + (value & 1);
        if (count >= k) { break; }
        k -= count;
        if (maxn) {
            if (maxn == minx) {
                xmap[maxn] = xmap[maxn] + (count << 1);
            }
            else {
                xmap[maxn] = xmap[maxn] + count;
                if (minx) {
                    xmap[minx] = xmap[minx] + count;
                }
            }
        }
    }
    

    cout << "Case #" << t << ": " << maxn << ' ' << minx << endl;
}

int main() {
    int t, T;
    cin >> T;
    xrep(t, 1, T+1) {
        proc(t);
    }
}
