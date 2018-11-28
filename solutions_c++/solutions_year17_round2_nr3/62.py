#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for (int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for (int i = (int)(n) - 1; i >= (int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define db(x) cout << #x << " = " << x << endl

using namespace std;
            
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
typedef double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-9;
const int INF = (int)1e9;
const int MAXN = 111;
const ll LINF = 1e18;

int T, n, q;
int len[MAXN], s[MAXN];
ll g[MAXN][MAXN];
int used[MAXN];
ld dist[MAXN];

void dijkstra(int f) {
    forn(i, n) {
        used[i] = 0;
        dist[i] = LINF;
    }
    
    dist[f] = 0;    
    forn(i, n) {
        int v = -1;
        forn(j, n) {
            if (!used[j] && (v == -1 || dist[j] < dist[v])) {
                v = j;
            }
        }
        used[v] = 1;
        
        //where?
        forn(w, n) {
            ll L = g[w][v];
            if (!used[w] && L <= len[w]) {
                ld t = ((ld)L) / s[w];
                dist[w] = min(dist[w], dist[v] + t);                   
            }
        }
    }
}

int main() {

    cout.precision(30);
    
    cin >> T;
    forn(ttt, T) {
        printf("Case #%d:", ttt + 1);
        scanf("%d%d", &n, &q);
        forn(i, n) {
            scanf("%d%d", &len[i], &s[i]);    
        }
        forn(i, n) {
            forn(j, n) {
                int x;
                scanf("%d", &x);
                g[i][j] = x;
                if (x == -1) {
                    g[i][j] = LINF;   
                }
            }
        }
        
        forn(k, n) {
            forn(i, n) {
                forn(j, n) {
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
                }
            }
        }
        
        forn(i, q) {
            int s, f;
            scanf("%d%d", &s, &f);
            s--, f--;

            dijkstra(f);
            cout << ' ' << dist[s];   
        }
        
        cout << '\n';
    }
    
    return 0;
}