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

const int MAX = 20;
int n, TC, visit[MAX][MAX][2];
char str[MAX];
bool dp[MAX][MAX][2];
struct data {
    int last, flag;
} path[MAX][MAX][2];

bool DP(int idx, int last, int flag) {
    if(idx >= n) return true;

    if(visit[idx][last][flag] == TC) return dp[idx][last][flag];
    visit[idx][last][flag] = TC;

    bool ret = false;
    int i;
    if(!flag) {
        for(i=9; i>=last; i--) {
            if(DP(idx+1, i, 0)) {
                ret = true;
                path[idx][last][flag] = { i, 0 };
                break;
            }
        }
    }
    else {
        int val = str[idx]-'0';
        if(val >= last && DP(idx+1, val, 1)) {
            ret = true;
            path[idx][last][flag] = { val, 1 };
        }
        else {
            for(i=val-1; i>=last; i--) {
                if(DP(idx+1, i, 0)) {
                    ret = true;
                    path[idx][last][flag] = { i, 0 };
                    break;
                }
            }
        }
    }
    return dp[idx][last][flag] = ret;
}

inline void printPath(int idx, int last, int flag) {
    while(idx < n) {
        if(path[idx][last][flag].last != 0) {
            printf("%d", path[idx][last][flag].last);
        }
        int a = path[idx][last][flag].last;
        int b = path[idx][last][flag].flag;
        last = a;
        flag = b;
        idx++;
    }
    puts("");
}

int main() {
//    assert(freopen("in.txt","r",stdin));
//    assert(freopen("out.txt","w",stdout));
//    assert(freopen("B-large.in","r",stdin));
//    assert(freopen("B-large.out","w",stdout));

    int test, kase=1;

    sdi(test);
    while(test--) {
        TC++;
        sds(str);
        n = strlen(str);
        printf("Case #%d: ", kase++);
        bool ret = DP(0, 0, 1);
        assert(ret);
        printPath(0, 0, 1);
    }

    return 0;
}
