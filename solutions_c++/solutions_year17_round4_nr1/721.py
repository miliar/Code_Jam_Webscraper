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
int n, p;

int cant[100];

ll solve(){
    cin >> n >> p;
    zero(cant);    
    forn(i, n){
        int v; cin >> v;
        cant[v%p]++;
    }
    if(p==2){
        return cant[0]+(cant[1]+1)/2;
    }
    else if(p==3){
        int ans=cant[0];
        int pa=min(cant[1], cant[2]);
        ans+=pa;
        cant[1]-=pa;
        cant[2]-=pa;
        ans+=cant[1]/3;
        ans+=cant[2]/3;
        if(cant[1]%3 || cant[2]%3) ans++;
        return ans;
    }
    return -1;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("A-small-attempt0.in", "r", stdin);
    ios::sync_with_stdio(0);
    int TC; cin >> TC;
    forr(TCC, 1, TC+1){
        cout << "Case #" << TCC << ": ";
        cout << solve();
        cout << endl;
    }
    return 0;
}
