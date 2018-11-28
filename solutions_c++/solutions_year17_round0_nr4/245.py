#include <bits/stdc++.h>
using namespace std;
#define rep(it,st,en) for(int it=(st);it<(int)(en);++it)
#define allof(c) (c).begin(), (c).end()
#define mt make_tuple
#define mp make_pair
#define pb push_back
#define X first
#define Y second
typedef long long int ll; 
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
const int INF=(int)1e9; 
const double EPS=(ld)1e-7;

vector<int> match;
vector<bool> seen;
template<class G>
bool find(int j, G &g) {
    if (match[j] == -1) return 1;
    seen[j] = 1; int di = match[j];
    for(auto &e: g[di])
        if (!seen[e] && find(e, g)) {
            match[e] = di;
            match[j] = -1;
            return 1;
        }
    return 0;
}
template<class G>
int dfs_matching(G &g, int n, int m) {
    match.assign(m, -1);
    rep(i,0,n) {
        seen.assign(m, false);
        for(auto &j: g[i])
            if (find(j, g)) {
                match[j] = i;
                break;
            }
    }
    return m - count(allof(match), -1);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    map<char,int> CI; map<int,char> IC;
    CI['+'] = 1; CI['x'] = 2; CI['o'] = 3;
    IC[1] = '+'; IC[2] = 'x'; IC[3] = 'o'; 

    int T;
    cin>>T;
    rep(t,1,T+1){
        int n,m;
        cin>>n>>m;
        set<int> cx,rx;
        set<int> d1,d2;
        map<pii,int> M;
        set<pii> added;
        rep(i,0,n) cx.insert(i), rx.insert(i);
        int ans = 0;
        rep(i,0,m){
            char c;
            int a,b;
            cin>>c>>a>>b;
            --a,--b;
            int k = CI[c];
            M[pii(a,b)] = k;
            if(k&1){
                ans++;
                d1.insert(a+b);
                d2.insert(a-b);
            }
            if(k&2){
                ans++;
                rx.erase(a);
                cx.erase(b);
            }
        }
        // place 'x'
        while(!rx.empty()){
            int a = *rx.begin();
            int b = *cx.begin();
            rx.erase(rx.begin()); 
            cx.erase(cx.begin());
            M[pii(a,b)] |= 2;
            ans++;
            added.insert(pii(a,b));
        }

        // place '+'
        vvi g(2*n-1);
        rep(i,0,n) rep(j,0,n){
            if(d1.count(i+j) || d2.count(i-j)) continue;
            g[i+j].pb(i-j+n-1);
        }
        dfs_matching(g, 2*n-1, 2*n-1);
        rep(k,0,2*n-1){
            int a = match[k];
            int b = k-n+1;
            if(a != -1) {
                assert((a+b)%2 == 0);
                int i = (a+b)/2;
                int j = (a-b)/2;
                M[pii(i,j)] |= 1;
                ans++;
                added.insert(pii(i,j));
            }
        }

        cout<<"Case #"<<t<<": "<<ans<<" "<<added.size()<<endl;
        for(pii p: added)
            cout<<IC[M[p]]<<" "<<(p.X+1)<<" "<<(p.Y+1)<<"\n";
    }
    return 0;
}
