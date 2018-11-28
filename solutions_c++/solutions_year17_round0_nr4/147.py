//84104971101048411497 - Can you guess what does this mean?
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef complex<double> point;
#define mapii map<int, int>
#define debug(a) cout << #a << ": " << a << endl
#define debuga1(a, l, r) fto(i, l, r) cout << a[i] << " "; cout << endl
#define fdto(i,  r, l) for(int i = (r); i >= (l); --i)
#define fto(i, l, r) for(int i = (l); i <= (r); ++i)
#define forit(it, var) for(__typeof(var.begin()) it = var.begin(); it != var.end(); it++)
#define forrit(rit, var) for(__typeof(var.rbegin()) rit = var.rbegin(); rit != var.rend(); rit++)
#define ii pair<int, int>
#define iii pair<int, ii>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define X real()
#define Y imag()
#define maxN 205
#define oo 2000000007
#define EPS 1e-9
#define sz(a) (int)a.size()

const double PI = acos(-1.0);

double fRand(double fMin, double fMax)
{
    double f = (double)rand() / RAND_MAX;
    return fMin + f * (fMax - fMin);
}

template <class T>
T min(T a, T b, T c) {
    return min(a, min(b, c));
}

template <class T>
T max(T a, T b, T c) {
    return max(a, max(b, c));
}

int nTest, n, m, p[2*maxN];
bool r[maxN], c[maxN], cc[2*maxN], cp[2*maxN], _plus[maxN][maxN], cross[maxN][maxN], visited[2*maxN], g[2*maxN][2*maxN];
char st[maxN][maxN], ansSt[maxN][maxN];

bool DFS(int u) {
    if (visited[u]) return false;
    visited[u] = true;
    fto(v, 1, 2*n-1) {
        if (g[u][v] && (!p[v] || DFS(p[v]))) {
            p[v] = u;
            return true;
        }
    }
    return false;
}

int main () {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    scanf("%d", &nTest);
    fto(iTest, 1, nTest) {
        scanf("%d%d", &n, &m);

        fto(i, 0, n) fto(j, 0, n) st[i][j] = ansSt[i][j] = '.';
        memset(r, false, sizeof r);
        memset(c, false, sizeof c);
        memset(cc, false, sizeof cc);
        memset(cp, false, sizeof cp);
        memset(_plus, false, sizeof _plus);
        memset(cross, false, sizeof cross);
        memset(g, false, sizeof g);
        memset(p, 0, sizeof p);

        fto(i, 1, m) {
            char s[2];
            int x, y;
            scanf("%s%d%d", s, &x, &y);
            if (s[0] == 'o' || s[0] == '+') {
                cc[x-y+n] = true;
                cp[x+y-1] = true;
                _plus[x][y] = true;
            }
            if (s[0] == 'o' || s[0] == 'x') {
                r[x] = true;
                c[y] = true;
                cross[x][y] = true;
            }
            st[x][y] = s[0];
        }

        fto(x, 1, n) {
            fto(y, 1, n) {
                if (!r[x] && !c[y]) {
                    r[x] = true;
                    c[y] = true;
                    cross[x][y] = true;
                }
            }
        }

        fto(x, 1, n) {
            fto(y, 1, n) {
                if (!cc[x-y+n] && !cp[x+y-1]) {
                    //printf("%d %d %d %d\n", x, y, x-y+n, x+y-1);
                    g[x-y+n][x+y-1] = true;
                }
            }
        }

        fto(u, 1, 2*n-1) {
            memset(visited, false, sizeof visited);
            DFS(u);
        }

        fto(u, 1, 2*n-1) {
            if (p[u] != 0) {
                int x = (p[u]+u-n+1)/2, y = u+1-x;
                _plus[x][y] = true;
            }
        }

        vector<pair<char, ii> > ans;
        int sum = 0;
        fto(x, 1, n) {
            fto(y, 1, n) {
                if (cross[x][y] && _plus[x][y]) ansSt[x][y] = 'o';
                else if (cross[x][y]) ansSt[x][y] = 'x';
                else if (_plus[x][y]) ansSt[x][y] = '+';
                else ansSt[x][y] = '.';

                if (ansSt[x][y] == 'o') sum += 2;
                if (ansSt[x][y] == '+' || ansSt[x][y] == 'x') sum += 1;
                if (ansSt[x][y] != st[x][y]) ans.pb(mp(ansSt[x][y], mp(x, y)));
            }
        }

//        fto(x, 1, n) printf("%s\n", st[x]);
//        fto(x, 1, n) printf("%s\n", ansSt[x]);

        printf("Case #%d: %d %d\n", iTest, sum, sz(ans));
        forit(it, ans) printf("%c %d %d\n", it->ff, it->ss.ff, it->ss.ss);
    }



    return 0;
}
