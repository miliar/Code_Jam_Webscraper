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
#define maxN 105
#define oo 1000000000000000007LL

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

int nTest, n, q, e[maxN], s[maxN], a[maxN][maxN];
ll dist[maxN][maxN];
double d[maxN];
bool avail[maxN];

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &nTest);
    fto(iTest, 1, nTest) {
        scanf("%d%d", &n, &q);
        fto(i, 1, n) scanf("%d%d", &e[i], &s[i]);
        fto(i, 1, n) {
            fto(j, 1, n) {
                scanf("%d", &a[i][j]);
                dist[i][j] = (a[i][j] == -1) ? oo : a[i][j];
            }
        }

        fto(k, 1, n)
            fto(i, 1, n)
                fto(j, 1, n) dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]);

        printf("Case #%d:", iTest);
        fto(i, 1, q) {
            int st, en;
            scanf("%d%d", &st, &en);

            fto(i, 1, n) d[i] = oo, avail[i] = true;
            d[st] = 0;

            while (true) {
                int u = 0;
                double minD = oo;
                fto(v, 1, n) {
                    if (avail[v] && d[v] < minD) {
                        minD = d[v];
                        u = v;
                    }
                }
                if (u == 0) break;

                avail[u] = false;
                fto(v, 1, n) {
                    if (avail[v] && dist[u][v] <= e[u]) {
                        d[v] = min(d[v], d[u]+1.0*dist[u][v]/s[u]);
                    }
                }
            }

            printf(" %.9g", d[en]);
        }
        puts("");
    }

    return 0;
}
