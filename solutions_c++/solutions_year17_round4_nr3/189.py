#include<bits/stdc++.h>
using namespace std;
class TwoSAT{
    public:
    int n;
    vector < vector<int> > g, gt;
    vector<bool> used;
    vector<int> order, comp;
    void dfs1 (int v) {
        used[v] = true;
        for (size_t i=0; i<g[v].size(); ++i) {
            int to = g[v][i];
            if (!used[to])
                dfs1 (to);
        }
        order.push_back (v);
    }
    void dfs2 (int v, int cl) {
        comp[v] = cl;
        for (size_t i=0; i<gt[v].size(); ++i) {
            int to = gt[v][i];
            if (comp[to] == -1)
                dfs2 (to, cl);
        }
    }
    bool Satisfable(vector < int > &sol){
        sol.resize(n/2);
        sol.clear();
        for(int i = 0 ; i < n ; i++)
           if (!used[i])
                dfs1 (i);
        for (int i=0, j=0; i<n; ++i) {
            int v = order[n-i-1];
            if (comp[v] == -1) dfs2 (v, j++);
        }
        for(int i = 0 ; i < n ; i++)
            if (comp[i] == comp[i^1])
                return 0;
        for(int i = 0 ; i < n ; i+=2){
            int ans = comp[i] > comp[i^1] ? i : i^1;
            sol.push_back(ans%2);
        }
        return 1;
    }
    void init(int N){
        n = N * 2;
        used.clear(); order.clear(); comp.clear();
        g.resize(n);
        gt.resize(n);
        used.assign (n, false);
        comp.assign (n, -1);
    }

    void imply(int a , int na ,int b , int nb){
        // na :: 0 variable is false , 1 variable is true
	// pass variables 1 indexed
        a--; b--;
        a*=2 , b*=2;
        a += na , b +=nb;
        g[a].push_back(b);
        gt[b].push_back(a);
        g[b^1].push_back(a^1);
        gt[a^1].push_back(b^1);
    }
    void orr(int a , int na , int b , int nb){
        imply(a , 1 - na, b , nb);
    }
    void xorr(int a , int na , int b , int nb){
        imply(a , na , b , 1 - nb);
        imply(a , 1 - na , b , nb);
        imply(b , nb , a , 1 - na);
        imply(b , 1 - nb , a , na);
    }
};
const int MX = 70;
string grid[MX];
int onrow[MX][MX] , oncol[MX][MX];
int hor[MX][MX] , ver[MX][MX];
int elrow[MX] , elcol[MX];
int baddour[MX*MX*5];
int whorow[MX][MX] , whocol[MX][MX];
int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int R , C , T , Tn = 0;
    cin>>T;
    while(T--){
        TwoSAT G;
        printf("Case #%d: ",++Tn);
        cin>>R>>C;
        memset(baddour , 0 , sizeof(baddour));
        memset(hor , 0 , sizeof(hor));
        memset(ver , 0 , sizeof(ver));
        memset(elrow , 0 , sizeof(elrow));
        memset(elcol , 0 , sizeof(elcol));
        memset(whorow , 0 , sizeof(whorow));
        memset(whocol , 0 , sizeof(whocol));
        int timer = 0;
        for(int j = 1 ; j <= R ; j++){
            cin>>grid[j];
            grid[j] = "#" + grid[j];
        }
        for(int x = 1 ; x <= R ; x++){
            for(int y = 1 ; y <= C ; y++){
                if(grid[x][y] == '#'){
                    onrow[x][y] = -1;
                    continue;
                }
                if(y == 1 || grid[x][y-1] == '#') onrow[x][y] = ++timer;
                else onrow[x][y] = onrow[x][y-1];
                //cout<<onrow[x][y]<<' ';
            }
        }

        for(int y = 1 ; y <= C ; y++){
            for(int x = 1 ; x <= R ; x++){
                if(grid[x][y] == '#'){
                    oncol[x][y] = -1;
                    continue;
                }
                if(x == 1 || grid[x-1][y] == '#') oncol[x][y] = ++timer;
                else oncol[x][y] = oncol[x-1][y];

            }
        }
        bool fakss = 0;
        int jd3 = 0;
        for(int x = 1 ; x <= R ; x++){
            for(int y = 1 ; y <= C ; y++){
                for(int j = 1 ; j <= C ; j++){
                    if(grid[x][y] == '|' || grid[x][y] == '-')
                        if(grid[x][j] == '|' || grid[x][j] == '-')
                            if(y != j)
                                if(onrow[x][j] == onrow[x][y]){
                                    ver[x][j] = ver[x][y] = 1;
                                 //   cout<<x<<' '<<y<<' '<<j<<endl;
                                }
                }
                for(int j = 1 ; j <= R ; j++){
                    if(grid[x][y] == '|' || grid[x][y] == '-')
                        if(grid[j][y] == '|' || grid[j][y] == '-')
                            if(oncol[j][y] == oncol[x][y] && x != j){
                                hor[x][y] = hor[j][y] = 1;
                         //       cout<<x<<' '<<y<<' '<<j<<' '<<y<<endl;
                            }
                }
                if(grid[x][y] != '|' && grid[x][y] != '-') continue;
                if(hor[x][y] && ver[x][y]){
                    fakss = 1;
                }
                if(hor[x][y] && !ver[x][y]){
                    elrow[x] = 1;
                }
                if(!hor[x][y] && ver[x][y]){
                    elcol[y] = 1;
                }
                if(!hor[x][y] && !ver[x][y]){
                    baddour[onrow[x][y]] = 1;
                    baddour[oncol[x][y]] = 1;
                }

            }
        }
        if(fakss) {
            puts("IMPOSSIBLE");
     //       puts("a4333");
            continue;
        }
        G.init(10000);
        for(int x = 1 ; x <= R ; x++){
            for(int y = 1 ; y <= C ; y++){
                if(grid[x][y] == '|' || grid[x][y] == '-'){
                    if(!hor[x][y] && !ver[x][y])
                        G.xorr(onrow[x][y] , 1 , oncol[x][y] , 1);
                    continue;
                }
                if(grid[x][y] != '.') continue;
                if(elcol[y] || elrow[x]) continue;
                //cout<<x<<' '<<y<<' '<<whorow[x]<<' '<<whocol[y]<<endl;
                int a = onrow[x][y] , b = oncol[x][y];
                if(baddour[a] == 0 && baddour[b] == 0){ fakss = 1;}
                else if(baddour[a] == 0) G.orr(oncol[x][y] , 1 , oncol[x][y] , 1);
                else if(baddour[b] == 0) G.orr(onrow[x][y] , 1 , onrow[x][y] , 1);
                else G.orr(onrow[x][y] , 1 , oncol[x][y] , 1);
            }
        }
        //cout<<timer<<endl;
        vector < int > aa;
        bool feh = 0;
        if(!fakss && G.Satisfable(aa)) feh = 1 , puts("POSSIBLE");
        else puts("IMPOSSIBLE");
        if(feh)
        for(int x = 1 ; x <= R ; x++){
            for(int y = 1 ; y <= C ; y++){
                if(grid[x][y] == '.' || grid[x][y] == '#'){
                    cout<<grid[x][y];
                    continue;
                }
               // cout<<onrow[x][y]<<' ';
                if(hor[x][y]) cout<<'-';
                else if(ver[x][y]) cout<<'|';
                else if(aa[onrow[x][y]-1]) cout<<'-';
                else cout<<'|';
            }
            puts("");

        }
    }
}

