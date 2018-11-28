#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define first fi
#define second se
#define sz(x) (int)x.size()
#define mp(a,b) make_pair(a,b)
#define pb push_back
const int inf = 0x3f3f3f3f;
const int mod = 1e9+7;

const int N = 105;
int Ha, Aa, Hb, Ab, B, D;
int vis[N][N][N][N][2];
int T;
int cas;

struct ST {
    int Ha, Aa, Hb, Ab, f, w;
    ST() {}
    ST(int Ha, int Aa, int Hb, int Ab, int f, int w) : Ha(Ha), Aa(Aa), Hb(Hb), Ab(Ab), f(f), w(w) {}
};
queue<ST> Q;

void gao(ST v) {
    if (vis[v.Ha][v.Aa][v.Hb][v.Ab][v.f] != cas) {
        vis[v.Ha][v.Aa][v.Hb][v.Ab][v.f] = cas;
        Q.push(v);
    }
}

int bfs() {
  //  printf("%d\n", cas);
    while (!Q.empty()) Q.pop();
    Q.push(ST(Ha, Aa, Hb, Ab, 0, 0));
    vis[Ha][Aa][Hb][Ab][0] = cas;
    while (!Q.empty()) {
        ST u = Q.front(); Q.pop();
        if (u.Ha == 0) continue;
        if (u.Hb == 0) return ((u.w + 1) / 2);
     //   printf("%d %d %d %d %d %d\n", u.Ha, u.Aa, u.Hb, u.Ab, u.f, u.w);
        if (u.f) {
            ST v = u;
            v.f = 0;
            v.Ha = max(0, v.Ha - v.Ab);
            v.w++;
            gao(v);
        } else {
            ST v = u;
            v.Ha = Ha;
            v.w++;
            v.f = 1;
            gao(v);

            v = u;
            v.Hb = max(0, v.Hb - v.Aa);
            v.w++;
            v.f = 1;
            gao(v);

            v = u;
            v.Aa = min(100, v.Aa + B);
            v.w++;
            v.f = 1;
            gao(v);

            v = u;
            v.Ab = max(0, v.Ab - D);
            v.w++;
            v.f = 1;
            gao(v);
        }
    }
    return -1;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    cas = 0;
    while (T--){
        scanf("%d%d%d%d%d%d", &Ha, &Aa, &Hb, &Ab, &B, &D);
        ++cas;
        printf("Case #%d: ", cas);
        int ans = bfs();
        if (ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
