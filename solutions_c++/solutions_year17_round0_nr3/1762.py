#include <bits/stdc++.h>

#define rep(i,n) for(i=0; i<n; i++)
#define repl(i,n) for(i=1; i<=n; i++)

#define sz(x) (int) x.size()
#define pb push_back
#define all(x) x.begin(),x.end()
#define uu first
#define vv second
#define mem(x, y) memset(x, y, sizeof(x))
#define un(x) x.erase(unique(all(x)), x.end())

#define sdi(x) scanf("%d", &x)
#define sdii(x, y) scanf("%d %d", &x, &y)
#define sdiii(x, y, z) scanf("%d %d %d", &x, &y, &z)
#define sdl(x) scanf("%lld", &x)
#define sdll(x, y) scanf("%lld %lld", &x, &y)
#define sdlll(x, y, z) scanf("%lld %lld %lld", &x, &y, &z)
#define sds(x) scanf("%s", x)
#define pfi(x) printf("%d\n", x)
#define pfii(x, y) printf("%d %d\n", x, y)
#define pfiii(x, y, z) printf("%d %d %d\n", x, y, z)
#define pfl(x) printf("%lld\n", x)
#define pfll(x, y) printf("%lld %lld\n", x, y)
#define pflll(x, y, z) printf("%lld %lld %lld\n", x, y, z)

#define eps 1e-9
#define OK cerr << "ok\n"
#define DB(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair <int, int> pii;

inline int setBit(int N, int pos) { return N=N | (1<<pos); }
inline int resetBit(int N, int pos) { return N= N & ~(1<<pos); }
inline bool checkBit(int N, int pos) { return (bool)(N & (1<<pos)); }

//int kx[] = {+2, +1, -1, -2, -2, -1, +1, +2};
//int ky[] = {+1, +2, +2, +1, -1, -2, -2, -1}; //Knight Direction
//int fx[] = {+0, +0, +1, -1, -1, +1, -1, +1};
//int fy[] = {-1, +1, +0, +0, +1, +1, -1, -1}; //Four & Eight Direction

inline pair <LL, LL> solve(LL n, LL k) {
    priority_queue <LL> q;
    unordered_map <LL, LL> mapp;
    LL cur=1;
    q.push(n);
    mapp[n] = 1;
    while(true) {
        LL now = q.top();
        q.pop();
        LL freq = mapp[now];
        mapp[now] = 0;
        if(freq == 0) continue;
        now--;
        LL b = now/2;
        LL a = now/2 + (bool)(now%2);
        if(k <= cur+freq-1) return { a, b };
        q.push(a);
        q.push(b);
        if(mapp.find(a) == mapp.end()) mapp[a] = freq;
        else mapp[a] += freq;
        if(mapp.find(b) == mapp.end()) mapp[b] = freq;
        else mapp[b] += freq;
        cur += freq;
    }
}

inline pair <LL, LL> brute(LL n, LL k) {
    priority_queue <LL> q;
    q.push(n);
    while(k--) {
        LL now = q.top()-1;
        q.pop();
        LL b = now/2;
        LL a = now/2 + (bool)(now%2);
        if(k == 0) return { a, b };
        q.push(a);
        q.push(b);
    }
}

int main() {
//    assert(freopen("in.txt","r",stdin));
//    assert(freopen("out.txt","w",stdout));
    assert(freopen("C-large.in","r",stdin));
    assert(freopen("C-large.out","w",stdout));

    int test, kase=1;
    LL n, k;

    sdi(test);
    while(test--) {
        cerr << kase << endl;
        sdll(n, k);
        printf("Case #%d: ", kase++);
        auto x = solve(n, k);
        pfll(x.uu, x.vv);
//        auto y = brute(n, k);
//        assert(x == y);
    }

    return 0;
}
