#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

typedef int _loop_int;
#define REP(i,n) for(_loop_int i=0;i<(_loop_int)(n);++i)
#define FOR(i,a,b) for(_loop_int i=(_loop_int)(a);i<(_loop_int)(b);++i)
#define FORR(i,a,b) for(_loop_int i=(_loop_int)(b)-1;i>=(_loop_int)(a);--i)

#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define DEBUG_VEC(v) cout<<#v<<":";REP(i,v.size())cout<<" "<<v[i];cout<<endl
#define ALL(a) (a).begin(),(a).end()

#define CHMIN(a,b) a=min((a),(b))
#define CHMAX(a,b) a=max((a),(b))

// mod
const ll MOD = 1000000007ll;
#define FIX(a) ((a)%MOD+MOD)%MOD

// floating
typedef double Real;
const Real EPS = 1e-11;
#define EQ0(x) (abs(x)<EPS)
#define EQ(a,b) (abs(a-b)<EPS)
typedef complex<Real> P;

int n;
void dfs(int p,int v,vi &used, vector<vector<bool>> &g){
  used[p] = v;
  int from = 2*p+v;
  REP(to,2*n){
    if(!g[from][to])continue;
    if(used[to/2]!=-1)continue;
    dfs(to/2,to%2,used,g);
  }
}

int r,c;
char mp[52][52];
int dir[52][52];
bool covered[52][52];
vi lst[52][52];

const int TATE = 1, YOKO = 2;

int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};
void solve(){
  scanf("%d%d",&r,&c);
  REP(i,r)scanf("%s",mp[i]);
  REP(i,r)REP(j,c)covered[i][j] = false;
  REP(i,r)REP(j,c)lst[i][j].clear();
  REP(i,r)REP(j,c){
    dir[i][j] = -1;
    if(mp[i][j]=='|')mp[i][j] = '-';
    if(mp[i][j]!='-')continue;
    dir[i][j] = TATE | YOKO;
    REP(d,4){
      int dd = d;
      int ci=i, cj=j;
      while(true){
        ci += dy[dd];
        cj += dx[dd];
        if(ci<0 || cj<0 || ci>=r || cj>=c)break;
        if(mp[ci][cj]=='#')break;
        if(mp[ci][cj]=='-' || mp[ci][cj]=='|'){
          if(d%2==0){
            // yoko is forbidden
            dir[i][j] &= TATE;
          }else{
            // tate is forbidden
            dir[i][j] &= YOKO;
          }
          break;
        }
        if(mp[ci][cj]=='/'){
          dd = 3-dd;
        }else if(mp[ci][cj]=='\\'){
          dd ^= 1;
        }
      }
    }
    if(dir[i][j]==0){
      puts("IMPOSSIBLE");
      return;
    }
    if(dir[i][j]!=(TATE|YOKO)){
      REP(d,4){
        if(dir[i][j]==YOKO && d%2==1)continue;
        if(dir[i][j]==TATE && d%2==0)continue;
        int dd = d;
        int ci=i, cj=j;
        while(true){
          covered[ci][cj] = true;
          ci += dy[dd];
          cj += dx[dd];
          if(ci<0 || cj<0 || ci>=r || cj>=c)break;
          if(mp[ci][cj]=='#')break;
          if(mp[ci][cj]=='/'){
            dd = 3-dd;
          }else if(mp[ci][cj]=='\\'){
            dd ^= 1;
          }
        }
      }
      if(dir[i][j]==YOKO)mp[i][j]='-';
      else mp[i][j]='|';
    }else{
      int id = i*50+j;
      REP(d,4){
        int dd = d;
        int ci=i, cj=j;
        while(true){
          ci += dy[dd];
          cj += dx[dd];
          if(ci<0 || cj<0 || ci>=r || cj>=c)break;
          if(mp[ci][cj]=='#')break;
          if(mp[ci][cj]=='/'){
            dd = 3-dd;
          }else if(mp[ci][cj]=='\\'){
            dd ^= 1;
          }
          if(mp[ci][cj]=='.'){
            lst[ci][cj].push_back(id*2 + (d%2));
          }
        }
      }
    }
  }
  // construct 2-sat
  // yoko(0)->false, tate(1)->true
  // ray map
  map<int,int> ray;
  REP(i,r)REP(j,c)if(mp[i][j]=='-' && dir[i][j]==(TATE|YOKO)){
    int id = ray.size();
    ray[2*(50*i+j)+0]=id;
    ray[2*(50*i+j)+1]=id+1;
  }
  // vector<vi> g(ray.size());
  vector<vector<bool>> g(ray.size(),vector<bool>(ray.size(),false));
  REP(i,r)REP(j,c)if(mp[i][j]=='.' && !covered[i][j]){
    if(lst[i][j].size()==0){
      puts("IMPOSSIBLE");
      return;
    }
    if(lst[i][j].size()==1)lst[i][j].push_back(lst[i][j][0]);
    int a = ray[lst[i][j][0]];
    int b = ray[lst[i][j][1]];
    if(a==b){
      // g[a^1].push_back(b);
      g[a^1][b]=true;
    }else{
      // g[a^1].push_back(b);
      // g[b^1].push_back(a);
      g[a^1][b]=true;
      g[b^1][a]=true;
    }
  }
  REP(k,ray.size())REP(i,ray.size())REP(j,ray.size())g[i][j] = g[i][j] || (g[i][k]&&g[k][j]);
  REP(i,ray.size()/2)if(g[2*i][2*i+1] && g[2*i+1][2*i]){
    puts("IMPOSSIBLE");
    return;
  }
  n = ray.size()/2;
  puts("POSSIBLE");
  vi ans(ray.size()/2, -1);
  REP(i,r)REP(j,c)if(mp[i][j]=='-' && dir[i][j]==(TATE|YOKO)){
    int id = ray[2*(50*i+j)]/2;
    if(ans[id]!=-1){
      if(ans[id])mp[i][j]='|';
      continue;
    }
    int v = 1;
    if(!g[2*id][2*id+1])v=0;
    ans[id] = v;
    if(v)mp[i][j] = '|';
    dfs(id,v,ans,g);
  }
  REP(i,r)puts(mp[i]);
}

int main(){
  int t;
  scanf("%d",&t);
  REP(i,t){
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}
