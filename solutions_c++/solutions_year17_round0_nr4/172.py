#include <iostream>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <ctime>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <bitset>
#include <vector>
#include <complex>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef double db;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define de(x) cout << #x << "=" << x << endl
#define rep(i,a,b) for(int i=a;i<(b);++i)
#define per(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define fi first
#define se second

const int N = 205;
int T , n , m , has[4][N] , mask[N][N] , bmask[N][N];

int link[N],vis[N];
int dfs(int c,vi g[]){
    for(auto t : g[c])
        if(!vis[t]){
            vis[t] = true;
            if(link[t]==-1||dfs(link[t],g))
                return link[t]=c,1;
        }
    return 0;
}
int solve(int n,int m,vi g[]){
    fill_n(link,m,-1);
    int ret=0;
    rep(i,0,n){
        memset(vis,0,m*sizeof(int));
        ret += dfs(i,g);
    }
    return ret;
}
vi g[N];
char get(int mask){
    if(mask == 1) return 'x';
    if(mask == 2) return '+';
    if(mask == 3) return 'o';
    cerr << "???" << endl;
    return -1;
}

int main(){
    cin >> T;
    rep(i,0,T){
        cout << "Case #" << i + 1 << ": ";
        cin >> n >> m;
        memset(has,0,sizeof(has));
        memset(bmask,0,sizeof(bmask));
        memset(mask,0,sizeof(mask));
        int ans = 0;
        rep(i,0,m){
            char ch;int x , y;
            cin >> ch >> x >> y;
            --x;--y;
            if(ch == 'o') ans += 2;
            else ans ++;
            if(ch == 'o' || ch == 'x') has[0][x] = has[1][y] = 1 , bmask[x][y] |= 1;
            if(ch == 'o' || ch == '+') has[2][x - y + n - 1] = has[3][x + y] = 1 , bmask[x][y] |= 2;
        }
        rep(i,0,n) g[i].clear();
        rep(i,0,n) rep(j,0,n) if(!has[0][i] && !has[1][j])
            g[i].pb(j);
        ans += solve(n , n , g);
        rep(i,0,n) if(~link[i]) mask[link[i]][i] |= 1;
        int nn = n + n - 1;
        rep(i,0,nn) g[i].clear();
        rep(i,0,n) rep(j,0,n){
            int x = i - j + n - 1 , y = i + j;
            if(!has[2][x] && !has[3][y])
                g[x].pb(y);
        }
        ans += solve(nn , nn , g);
        rep(i,0,nn) if(~link[i]){
            int j = link[i];
            int a = (j + i - n + 1) / 2;
            int b = i - a;
            mask[a][b] |= 2;
        }
        vector<pii> v;
        rep(i,0,n) rep(j,0,n) if(mask[i][j]) v.pb(mp(i,j));
        cout << ans << " " << sz(v) << endl;
        for(auto e : v) cout << get(mask[e.fi][e.se] | bmask[e.fi][e.se]) << " " << e.fi + 1 << " " << e.se + 1 << endl;
    }
    return 0;
}

