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

const int MAXN=100100;
int N, C, M;
map<int, int> tickets[2020];
int qtickets[2020];
int cant[2020];



int f(int t){
    int acum=0;
    forn(i, N){
        for(auto it:tickets[i])
            acum+=it.snd;
        if(acum>t*(i+1)) return -1;
    }
    int mx=0;
    forn(i, C) mx=max(mx, cant[i]);
    if(mx>t) return -1;
    int prom=0;
    forn(i, N){
        if(t<qtickets[i])
            prom+=qtickets[i]-t;
    }
    return prom;
}

void solve(){
    cin >> N >> C >> M;
    forn(i, N) tickets[i].clear();
    zero(cant);
    zero(qtickets);
    forn(i, M){
        int p,b; cin >> p >> b; p--, b--;
        tickets[p][b]++;
        cant[b]++;
        qtickets[p]++;
    }
    int a=0,b=M;
    while(b-a>1){
        int c=(a+b)/2;
        if(f(c)>=0) b=c;
        else a=c; 
    }
    cout << b << ' ' << f(b) << endl;
}

int main() {
    freopen("b.in", "r", stdin);
    //~ freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    ios::sync_with_stdio(0);
    int TC; cin >> TC;
    forr(TCC, 1, TC+1){
        cout << "Case #" << TCC << ": ";
        solve();
    }
    return 0;
}
