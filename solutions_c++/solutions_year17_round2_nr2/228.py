#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define forab(i,a,b) for( int i = (a); i < (b); i++ )
#define forn(i,n) forab(i,0,n)
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>
#define pcc pair<char,char>

const int MXN = 110;
const double dinf = 1e18;


vector<vector<vector<pcc > > > dp [3];
int c [3];
int d [3];

int n;

int G, O, V;

string colors = "RYB";

void out(int cur, int a, int b, int c) {
    if (a + b + c == n) {
        return;
    }
    printf("%c", colors[cur]);
    if (colors[cur] == 'R' && G > 0) {
        forn(i,G) {
            printf("GR");
        }
        G = 0;
    }
    if (colors[cur] == 'B' && O > 0) {
        forn(i,O) {
            printf("OB");
        }
        O = 0;
    }
    if (colors[cur] == 'Y' && V > 0) {
        forn(i,V) {
            printf("VY");
        }
        V = 0;
    }
    int pp = dp[cur][a][b][c].se;
    if (cur == 0) {
        a++;
    }
    if (cur == 1) {
        b++;
    }
    if (cur == 2) {
        c++;
    }
    out(pp, a, b, c);
}

int sign(int a) {
    if (a > 0) return 1;
    else return 0;
}

void solve() {
    scanf("%d", &n);
    scanf("%d%d%d%d%d%d", &c[0], &O, &c[1], &G, &c[2], &V);
    c[0] -= G;
    c[1] -= V;
    c[2] -= O;
    n = c[0] + c[1] + c[2];
    if (c[0] < 0 || c[1] < 0 || c[2] < 0) {
        printf("IMPOSSIBLE");
        return;
    }
    if (n == 0 && sign(G) + sign(V) + sign(O) == 1) {
        if (G != 0) {
            forn(i,G) {
                printf("GR");
            }
        }
        if (O != 0) {
            forn(i,O) {
                printf("OB");
            }
        }
        if (V != 0) {
            forn(i,V) {
                printf("VY");
            }
        }
        return;
    }
    if ( (G != 0 && c[0] == 0) || (V != 0 && c[1] == 0) || (O != 0 && c[2] == 0) ) {
        printf("IMPOSSIBLE");
        return;        
    }
    forn(color,3) {
        if (c[color] == 0) continue;
        forn(cc,3) {
            dp[cc] = vector<vector<vector<pcc > > >(c[0] + 1);
            forn(i,c[0] + 1) {
                dp[cc][i] = vector<vector<pcc > >(c[1] + 1);
                forn(j,c[1] + 1) {
                    dp[cc][i][j] = vector<pcc>(c[2] + 1);
                }
            }
        }
        c[color]--;
        dp[color][c[0]][c[1]][c[2]].fi = 1;
        for (d[0] = c[0]; d[0] >= 0; d[0]--) {
            for (d[1] = c[1]; d[1] >= 0; d[1]--) {
                int mn = d[0] + d[1] == 0 ? 1 : 0;
                for (d[2] = c[2]; d[2] >= mn; d[2]--) {
                    forn(cc,3) {
                        if (!dp[cc][d[0]][d[1]][d[2]].fi) {
                            continue;
                        }
                        forn(cur,3) {
                            if (cur == cc || d[cur] == 0) {
                                continue;
                            }
                            d[cur]--;
                            dp[cur][d[0]][d[1]][d[2]].fi = 1;
                            dp[cur][d[0]][d[1]][d[2]].se = cc;
                            d[cur]++;
                        }
                    }
                }
            }
        }
        c[color]++;
        bool ok = false;
        forn(cur,3) {
            if (cur == color) {
                continue;
            }
            if (dp[cur][0][0][0].fi) {
                ok = true;


                out(cur, 0, 0, 0);
                break;
            }
        }
        if (ok) {
            return;
        }
    }
    printf("IMPOSSIBLE");
}


int main(){
    freopen("input.txt", "r", stdin);    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    forn(i,T){
        cerr << i << endl;
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }
}
