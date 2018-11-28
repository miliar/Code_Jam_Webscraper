#include <bits/stdc++.h>
#define LL long long
#define ULL unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define debug cout << "YES" << endl

using namespace std;

typedef pair<double,int>II;
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return __builtin_popcount(s);}
template<class T> T gcd(T a, T b){ T r; while (b != 0) { r = a % b; a = b; b = r; } return a;}

const double PI = 2*acos(0.0);
const double eps = 1e-9;
const int infi = 1e9;
const LL Linfi = 1e18;
const LL MOD = 1000000007;
const int c1 = 31;
const int c2 = 37;
#define maxn 1005

int n, q, ST[maxn], EN[maxn];

LL D[maxn][maxn], c[maxn][maxn]; //F[i]: number of shortest from start to i
double dp[maxn];
LL E[maxn], S[maxn];
priority_queue<II, vector<II> > Q;

void solve(){
    cout << fixed << setprecision(9);
    FOR(k,1,n) FOR(u,1,n) FOR(v,1,n){
        if (c[u][v] > c[u][k]+c[k][v])
            c[u][v] = c[u][k]+c[k][v];
    }


    FOR(i,1,q){
        FOR(i,1,n)  dp[i] = Linfi;
        int st = ST[i], en = EN[i];
        dp[st] = 0;
        while(!Q.empty()) Q.pop();
        Q.push(make_pair(0,st));

        while(!Q.empty()){
            double du = Q.top().fi;
            int u = Q.top().se; Q.pop(); //cout << u << endl;
            //if(u == en) break;
            if(abs(du - dp[u]) < eps)
            FOR(v,1,n) if(u != v && c[u][v] != Linfi){
                if(E[u] >= c[u][v]){
                    double t = 1.0*c[u][v] / S[u];
                    //cout << v << " : " << t << endl;
                    if(dp[v] > dp[u] + t){
                        dp[v] = dp[u] + t;
                        Q.push(mp(dp[v], v));
                    }

                }
            }
        }
        cout << dp[en] << " ";
    }
    cout << endl;

}

int main(){
    ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int sotest;
    cin >> sotest;
    FOR(test,1,sotest){
        cin >> n >> q;
        FOR(i,1,n) cin >> E[i] >>  S[i];
        FOR(i,1,n) FOR(j,1,n) cin >> D[i][j];
        FOR(i,1,n) FOR(j,1,n) {
            if(i == j) c[i][j] = 0;
            else if(D[i][j] == -1) c[i][j] = Linfi;
            else c[i][j] = D[i][j];
        }

        FOR(i,1,q) cin >> ST[i] >> EN[i];
        cout << "Case #" << test << ": ";
        solve();
    }



    return 0;
}
