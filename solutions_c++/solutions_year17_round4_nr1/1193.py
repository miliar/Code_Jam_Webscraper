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


const int MAX = 105;
int n, p, arr[MAX], freq[5];

inline int two() {
    int ret = freq[0] + freq[1]/2;
    if(freq[1]%2 != 0) ret++;
    return ret;
}

inline int three() {
    int ret = freq[0];
    int mn = min(freq[1], freq[2]);
    int mx = max(freq[1], freq[2]);
    ret += mn;
    ret += (mx-mn)/3;
    if((mx-mn)%3 != 0) ret++;
    return ret;
}

inline int four() {
    int ret = freq[0];
    int mn13 = min(freq[1], freq[3]);
    int mx13 = max(freq[1], freq[3]);
    ret += mn13;
    int leftover = mx13-mn13;
    ret += freq[2]/2;
    bool twoLeft = false;
    if(freq[2]%2 != 0) twoLeft = true;
    if(twoLeft) {
        if(leftover>=2) {
            ret++;
            leftover -= 2;
            ret += leftover/4;
            if(leftover%4 != 0) ret++;
        }
        else ret++;
    }
    else {
        ret += leftover/4;
        if(leftover%4 != 0) ret++;
    }
    return ret;
}

int main() {
//    assert(freopen("in.txt","r",stdin));
//    assert(freopen("out.txt","w",stdout));
    assert(freopen("A-large.in","r",stdin));
    assert(freopen("A-large.out","w",stdout));

    int test, kase=1, i;

    sdi(test);
    while(test--) {
        cerr << kase << endl;
        mem(freq, 0);
        sdii(n, p);
        rep(i, n) {
            sdi(arr[i]);
            freq[ arr[i]%p ]++;
        }
        printf("Case #%d: ", kase++);
        if(p == 2) pfi(two());
        else if(p == 3) pfi(three());
        else if(p == 4) pfi(four());
    }

    return 0;
}
