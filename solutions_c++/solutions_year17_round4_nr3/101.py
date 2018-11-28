#include <bits/stdc++.h>
using namespace std;
#define rep(it,st,en) for(int it=(st);it<(int)(en);++it)
#define allof(c) (c).begin(), (c).end()
#define mt make_tuple
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define sz(v) (v).size()
typedef long long int ll; 
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
const int INF=(int)1e9; 
const double EPS=(ld)1e-7;

struct TwoSat {
    int N;
    vector<vi> gr;
    vi values; // 0 = false , 1 = true
    TwoSat(int n = 0) : N(n), gr(2*n) {}
    int add_var() { // ( optional )
        gr.emplace_back();
        gr.emplace_back();
        return N++;
    }
    void add_clause(int a_index, bool a_value, int b_index, bool
            b_value) {
        int a = 2*a_index + a_value, b = 2*b_index + b_value;
        gr[a^1].push_back(b);
        gr[b^1].push_back(a);
    }
    void set_value(int index, bool value) { // ( optional )
        add_clause(index, value, index, value);
    }
    void at_most_one(const vi& li, bool val=1) { // ( optional )
        if (sz(li) <= 1) return;
        int cur = li[0];
        rep(i,2,sz(li)) {
            int next = add_var();
            add_clause(cur, !val, li[i], !val);
            add_clause(cur, !val, next, val);
            add_clause(li[i], !val, next, val);
            cur = next;
        }
        add_clause(cur, !val, li[1], !val);
    }
    vi val, comp, z; int time = 0;
    int dfs(int i) {
        int low = val[i] = ++time, x; z.push_back(i);
        for(auto& e: gr[i]) if (!comp[e])
            low = min(low, val[e] ?: dfs(e));
        ++time;
        if (low == val[i]) do {
            x = z.back(); z.pop_back();
            comp[x] = time;
            if (values[x>>1] == -1)
                values[x>>1] = x&1;
        } while (x != i);
        return val[i] = low;
    }
    bool solve() {
        values.assign(N, -1);
        val.assign(2*N, 0); comp = val;
        rep(i,0,2*N) if (!comp[i]) dfs(i);
        rep(i,0,N) if (comp[2*i] == comp[2*i+1]) return 0;
        return 1;
    }
};

int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    rep(tt,1,T+1){
        int r,c;
        cin>>r>>c;
        vector<string> v(r);
        rep(i,0,r) cin>>v[i];
        vector<vvi> lr(r,vvi(c)), ud(r,vvi(c));
        typedef tuple<int,int,int,int> node;
        queue<node> q;
        int cnt = 1;
        map<pii, int> M;
        rep(i,0,r){
            rep(j,0,c){
                if(v[i][j] == '-' || v[i][j] == '|'){
                    M[pii(i,j)] = cnt;
                    rep(d,0,4){
                        int x = i + dx[d];
                        int y = j + dy[d];
                        if(x >= 0 && x < r && y >= 0 && y < c){
                            q.push(make_tuple(x,y,d,cnt * ((d%2) ? 1:-1)));
                        }
                    }
                    cnt++;
                }
            }
        }
        TwoSat ts(cnt-1);
        while(!q.empty()){
            int x,y,d,t;
            tie(x,y,d,t) = q.front();
            q.pop();
            if(v[x][y] == '#') continue;
            if(v[x][y] == '-' || v[x][y] == '|'){
                int k = abs(t)-1;
                bool b = !(t>0);
                ts.set_value(k,b);
            }
            else if(v[x][y] == '/'){
                int d2;
                if(d == 0) d2 = 3;
                if(d == 1) d2 = 2;
                if(d == 2) d2 = 1;
                if(d == 3) d2 = 0;
                x = x + dx[d2];
                y = y + dy[d2];
                if(x >= 0 && x < r && y >= 0 && y < c){
                    q.push(make_tuple(x,y,d2,t));
                }
            }
            else if(v[x][y] == '\\'){
                int d2;
                if(d == 0) d2 = 1;
                if(d == 1) d2 = 0;
                if(d == 2) d2 = 3;
                if(d == 3) d2 = 2;
                x = x + dx[d2];
                y = y + dy[d2];
                if(x >= 0 && x < r && y >= 0 && y < c){
                    q.push(make_tuple(x,y,d2,t));
                }
            }
            else if(v[x][y] == '.'){
                if(d%2) lr[x][y].push_back(t);
                else ud[x][y].push_back(t);
                x = x + dx[d];
                y = y + dy[d];
                if(x >= 0 && x < r && y >= 0 && y < c){
                    q.push(make_tuple(x,y,d,t));
                }
            }
        }
        rep(i,0,r){
            rep(j,0,c){
                int x = i, y = j;
                if(v[x][y] == '.'){
                    if(lr[x][y].size()>1) lr[x][y].clear();
                    if(ud[x][y].size()>1) ud[x][y].clear();
                    if(lr[x][y].empty() && ud[x][y].empty()){
                        ts.set_value(0,true);
                        ts.set_value(0,false);
                    }
                    if(!lr[x][y].empty() && ud[x][y].empty()){
                        int t = lr[x][y][0];
                        int k = abs(t)-1;
                        bool b = (t>0);
                        ts.set_value(k,b);
                    }
                    if(lr[x][y].empty() && !ud[x][y].empty()){
                        int t = ud[x][y][0];
                        int k = abs(t)-1;
                        bool b = (t>0);
                        ts.set_value(k,b);
                    }
                    if(!lr[x][y].empty() && !ud[x][y].empty()){
                        int t1 = lr[x][y][0];
                        int k1 = abs(t1)-1;
                        bool b1 = (t1>0);
                        int t2 = ud[x][y][0];
                        int k2 = abs(t2)-1;
                        bool b2 = (t2>0);
                        ts.add_clause(k1,b1,k2,b2);
                    }
                }
            }
        }
        cout<<"Case #"<<tt<<": ";
        if(!ts.solve()){
            cout<<"IMPOSSIBLE\n";
        }
        else{
            cout<<"POSSIBLE\n";
            auto& q = ts.values;
            rep(i,0,r){
                rep(j,0,c){
                    if(v[i][j] == '-' || v[i][j] == '|'){
                        cout<<((q[M[pii(i,j)]-1])?'-':'|');
                    }
                    else{
                        cout<<v[i][j];
                    }
                }
                cout<<"\n";
            }
        }
    }
    return 0;
}
