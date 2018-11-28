
#include<algorithm>
#include<bitset>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define dprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", " << pair.Y << ")";}

int r, c;
int left(int i, int j) {
    return (2*i+1)*(c+1)+j;
}
int top(int i, int j) {
    return (2*i)*(c+1) + j;
}
int right(int i, int j) {
    return (2*i+1)*(c+1) + j+1;
}
int bot(int i, int j) {
    return (2*i+2)*(c+1) + j;
}

const int N=100000;
VI implies[2*N]; //wymuszenia, 2*x to zmienna 2*x+1 to jej zaprzeczenie
int sat_val[2*N],sat_vis[2*N],sat_sort[2*N],sat_ile;

inline void sat_or(int a,int b){
  //  debug(MP(a,b));
  implies[a^1].PB(b);
  implies[b^1].PB(a);
}

void sat_dfs_mark(int x){
  sat_vis[x]=1; sat_val[x]=sat_val[x^1]==-1;
  FORE(it,implies[x]) if (!sat_vis[*it]) sat_dfs_mark(*it);
}

void sat_dfs(int x){
  sat_vis[x]=1;
  FORE(it,implies[x^1]) if (!sat_vis[*it^1]) sat_dfs(*it^1);
  sat_sort[sat_ile++]=x;
}

/*przekazujemy liczbe zmiennych*/
int sat2(int n){
  sat_ile=0;
  REP(i,2*n) sat_vis[i]=0,sat_val[i]=-1;
  REP(i,2*n) if (!sat_vis[i]) sat_dfs(i);
  REP(i,2*n) sat_vis[i]=0;
  FORD(i,2*n-1,0) if (!sat_vis[sat_sort[i]]) sat_dfs_mark(sat_sort[i]);
  REP(i,2*n) if (sat_val[i]) FORE(it,implies[i]) if (!sat_val[*it]) return 0;
  return 1;
}


void solve(int tc) {
    cout << "Case #" << tc << ": ";
    cin >> r >> c;
    vector<string> T(r);
    int n = 2*(r+1)*(c+1);
    vector<VI> ng(2*(r+1)*(c+1));
    REP(i,r) cin >> T[i];
    REP(i,r) REP(j,c) {
        if (T[i][j] == '/') {
            ng[left(i,j)].PB(top(i,j));
            ng[top(i,j)].PB(left(i,j));
            ng[right(i,j)].PB(bot(i,j));
            ng[bot(i,j)].PB(right(i,j));
        } else if (T[i][j] == '\\') {
            ng[left(i,j)].PB(bot(i,j));
            ng[bot(i,j)].PB(left(i,j));
            ng[right(i,j)].PB(top(i,j));
            ng[top(i,j)].PB(right(i,j));
         } else if (T[i][j] != '#') {
            ng[left(i,j)].PB(right(i,j));
            ng[right(i,j)].PB(left(i,j));
            ng[bot(i,j)].PB(top(i,j));
            ng[top(i,j)].PB(bot(i,j));
         }
    }
    VI id(n, -1);
    int t = 0;
    REP(i,n) if (id[i] == -1 && !ng[i].empty()) {
        queue<int> Q;
        Q.push(i);
        id[i] = t;
        while(!Q.empty()) {
            int f = Q.front();
            Q.pop();
            for (int g : ng[f])  if (id[g] == -1) {
                id[g] = t;
                Q.push(g);
            }
        }
        ++t;
    }
    //debugv(id);
    VI cnt(t);
    REP(i,n) {
        if (id[i] == -1) continue;
        int col = id[i];
        cnt[col] += SZ(ng[i]) - 2;
    }
    VI who(t, -1);
    REP(i, 2*t+10) implies[i].clear();
    REP(i,r) REP(j,c) {
        if (T[i][j] == '|' || T[i][j] == '-') {
            T[i][j] = '|';
            int cl = id[left(i,j)], ct = id[top(i,j)];
            //debug(MP(cl,ct));
            if (who[cl] == -1) who[cl] = left(i,j);
            else who[cl] = -2;
            if (who[ct] == -1) who[ct] = top(i,j);
            else who[ct] = -2; 
            sat_or(2*cl+1, 2*ct+1);
        }
        if (T[i][j] != '#') {
            vector<int> S;
            S.PB(id[left(i,j)]);
            S.PB(id[right(i,j)]);
            S.PB(id[top(i,j)]);
            S.PB(id[bot(i,j)]);
            sort(ALL(S));
            sat_or(2*S[0], 2*S[3]);
        }
    }
   // debugv(who);
    REP(i,t) {
        if (who[i] < 0 || cnt[i] != -2) sat_or(2*i+1, 2*i+1);
    }
    int s = sat2(t);
    if (s == 0) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << "POSSIBLE" << endl;
        REP(i,r) REP(j,c) {
            if (T[i][j] == '|') {
                int cl = id[left(i,j)]; 
                if (sat_val[2*cl]) T[i][j] = '-';
            }
        }
        REP(i,r) cout << T[i] << endl;
    }
}


int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);
    int T;
    cin >> T;
    REP(i,T) solve(i+1);


    return 0;
}

