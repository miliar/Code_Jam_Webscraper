#include <bits/stdc++.h>
using namespace std;

#define fi          "input.txt"
#define fo          "output.txt"
#define fileopen    freopen(fi,"r",stdin);freopen(fo,"w",stdout)
#define FOR(i,l,r)  for(int i=(int)(l);i<=(int)(r);i++)
#define FORD(i,l,r) for(int i=(int)(l);i>=(int)(r);i--)
#define xy          pair<int64,int>
#define int64       long long
#define ld          long double
#define X           first
#define Y           second
#define pb          push_back
#define init(a,v)   memset(a,v,sizeof(a))
#define Sz(s)       (int)(s.size())
#define EL          cout<<endl
#define digit(x)    ('0'<=x&&x<='9')
#define forever     while (true)
#define ran(l,r)    ((1LL*rand()*rand())%((int)(r)-(int)(l)+1)+(int)(l))

const double OO = 1e18+5;
const int MOD = (int) 1e9+7;
const long double Pi = 3.141592653589793238;
const int N = (int) 1e2+5;

int a[N][N],e[N],s[N],n,q;
double dis[N][N], t[N][N];

void solve(int test) {
    cin>>n>>q;
    FOR(i,1,n) {
        cin>>e[i];
        cin>>s[i];
    }
    FOR(i,1,n) FOR(j,1,n)
        cin>>a[i][j];
    FOR(i,1,n) FOR(j,1,n) {
        dis[i][j]=a[i][j];
        if (dis[i][j]<0) {
            dis[i][j]=OO;
        }
        t[i][j]=OO;
        if (i==j) {
            t[i][j]=dis[i][j]=0;
        }
    }
    FOR(k,1,n)
        FOR(i,1,n)
            FOR(j,1,n)
                dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j]);

    FOR(k,1,n) {
        FOR(i,1,n) {
            FOR(j,1,n) {
                if (dis[i][j]>OO-100) continue;
                if (dis[i][k]>OO-100) continue;
                if (dis[k][j]>OO-100) continue;
                double ta=t[i][k],tb=t[k][j];
                if (dis[i][k]<=e[i]) {
                    ta = min(ta,dis[i][k]/s[i]);
                }
                if (dis[k][j]<=e[k]) {
                    tb = min(tb,dis[k][j]/s[k]);
                }
                t[i][j] = min(t[i][j], ta+tb);
            }
        }
    }
    while (q--) {
        int u,v;
        cin>>u>>v;
        printf("%.8f ",t[u][v]);
    }
}

int main() {
    fileopen;
    int T;cin>>T;
    FOR(i,1,T) {
        printf("Case #%i: ",i);
        solve(i);
        EL;
    }
}
