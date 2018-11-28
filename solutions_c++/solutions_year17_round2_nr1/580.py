//touch {a..m}.in; tee {a..m}.cpp < template.cpp
#include <bits/stdc++.h>
using namespace std;
#define forr(i,a,b) for(int i=(a); i<(b); i++)
#define forn(i,n) forr(i,0,n)
#define sz(c) ((int)c.size())
#define zero(v) memset(v, 0, sizeof(v))
#define forall(it,v) for(auto it=v.begin();it!=v.end();++it)
#define pb push_back
#define RND(a, b) (rand()%((b)-(a)+1)+(a))
#define fst first
#define snd second
typedef long long ll;
typedef pair<int,int> ii;
#define dforn(i,n) for(int i=n-1; i>=0; i--)
#define dprint(v) cout << #v"=" << v << endl //;)

const int MAXN=10100;
ll D,N;
ll K[MAXN], S[MAXN];

void solve(){
    cin >> D >> N;
    double mt=-1;
    forn(i, N){
        cin >> K[i] >> S[i];
        double t = (D-K[i])/(double)S[i];
        mt=max(mt, t);
    }
    double V=D/mt;
    cout << V;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ios::sync_with_stdio(0);
    int TC; cin >> TC;
    cout << setprecision(9) << fixed;
    forr(TCC, 1, TC+1){
        cout << "Case #" << TCC << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
