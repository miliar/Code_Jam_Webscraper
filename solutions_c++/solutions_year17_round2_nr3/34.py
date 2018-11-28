#include <bits/stdc++.h>
#define int long long
#define P(x) cout << x << endl
#define D(x) P(#x << ": " << x)
#define F(i,n) for (int i=0; i<(int)(n); i++)
#define DEC(i,n) for (int i=(int)(n); --i>=0;)
#define $(s) (int)((s).size())
#define ALL(v) v.begin(), v.end()
#define V vector
#define pb push_back
using namespace std;
void MI(int &a, int v) {a = min(a,v);}
void MA(int &a, int v) {a = max(a,v);}
const int MAXT=1e13, INF=1e17, N=100;

struct vd {int i; double d;};
bool operator<(vd a, vd b) {
    return a.d > b.d;
}

signed main() {
    int nt; cin>>nt;
    F(tt,nt) {
        int n,q; cin>>n>>q;
        int e[n], sp[n];
        F(i,n) cin>>e[i]>>sp[i];
        int d[n][n];
        F(i,n) F(j,n) {
            cin>>d[i][j];
            if (d[i][j] == -1)
                d[i][j] = INF;
        }
        F(k,n) F(i,n) F(j,n)
            d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        printf("Case #%lld:", tt+1);
        F(qq,q) {
            int s,t; cin>>s>>t;
            s--, t--;
            double curd[n];
            F(i,n) curd[i] = INF;
            curd[s] = 0;
            bitset<N> vis;
            F(ii,n) {
                double mi=INF; int u=-1;
                F(i,n) if (!vis[i] && curd[i] < mi)
                    mi = curd[i], u = i;
                if (u != -1) {
                    vis[u] = true;
                    F(v,n) if (d[u][v] <= e[u]) {
                        curd[v] = min(curd[v], curd[u] + (double)d[u][v] / sp[u]);
                    }
                }
            }
            printf(" %.8f", curd[t]);
        }
        printf("\n");
    }
}
