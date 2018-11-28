#include <bits/stdc++.h>
using namespace std;

/*
 *  2-sat algorithm in O(N^2 + M) time,
 *   O(N+M) average case time???
 *
 */
#include <bits/stdc++.h>
using namespace std;

struct Sat{
    int N;
    vector<vector<int> > G;
    vector<int> val, tmp;
    mt19937 RNG;
    Sat(int _N):N(_N), G(2*N), val(2*N){}
    int index(int x){
        return (2*abs(x)-2)+(x<0);
    }
    /// a->b
    void add_implication(int x1, int x2){
        G[index(x1)].push_back(index(x2));
    }
    /// a v b
    void add_or(int x1, int x2){
        add_implication(-x1, x2);
        add_implication(-x2, x1);
    }
    void add_true(int x1){
        add_implication(-x1, x1);
    }
    bool rec(int x){
        if(val[x]!=-1) return val[x];
        val[x]=1; val[x^1]=0;
        for(int const&e:G[x]){
            if(!rec(e)) return false;
        }
        return true;
    }
    int getRand(){
        return uniform_int_distribution<int>(0, 1)(RNG);
    }
    bool solve(){
        fill(val.begin(), val.end(), -1);
        vector<int> tmp(2*N);
        for(int i=0;i<2*N;i+=2){
            if(val[i]==-1){
                int off = getRand();
                copy(val.begin(), val.end(), tmp.begin());
                if(!rec(i^off)){
                    copy(tmp.begin(), tmp.end(), val.begin());
                    if(!rec(i^off^1)) return false;
                }
            }
        }
        return true;
    }


};


struct Pos{
    int x, y;
    int dir;
};
// 0: UP
// 1: RIGHT
// 2: DOWN
// 3: LEFT
vector<string>b;
void step(Pos &pos){
    switch(b[pos.x][pos.y]){
        case '.':
            break;
        case '/':
            pos.dir^=1;
            break;
        case '\\':
            pos.dir^=3;
            break;
        case '#':
            cerr << "in Wall\n";
            break;
    }
    switch(pos.dir){
        case 0:
            --pos.x;
            break;
        case 1:
            ++pos.y;
            break;
        case 2:
            ++pos.x;
            break;
        case 3:
            --pos.y;
            break;
        default:
            cerr << "invalid dir: " << pos.dir << "\n";
            assert(0);
    }
}

int main()
{
    freopen("inC.txt", "r", stdin);
    freopen("outC.txt", "w", stdout);
    cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
    int Tests; cin >> Tests;
    for(int cas=1;cas<=Tests;++cas){
        cout << "Case #" << cas << ": ";
        cerr << "Case #" << cas << "\n";
        int X, Y;
        cin >> X >> Y;
        b.clear();
        b.resize(X+2);
        b[0] = b.back() = string(Y+2, '#');
        for(int i=0;i<X;++i){
            cin >> b[i+1];
            b[i+1].insert(b[i+1].begin(), '#');
            b[i+1].push_back('#');
        }

        X+=2, Y+=2;
        Sat sat(X*Y+2);
        auto deco = [&](int const&x, int const&y){return 1+x+X*y;};
        auto enco = [&](int pos){--pos; return make_pair(pos%X, pos/X);};
        vector<vector<int> >  shoots(X*Y+2);
        bool fail = false;
        for(int i=1;i+1<X;++i){
            for(int j=1;j+1<Y;++j){
                vector<int> dirs;
                if(b[i][j]=='|'){
                    dirs = {0, 1, 2, 3};
                } else if(b[i][j]=='-'){
                    dirs = {0, 1, 2, 3};
                }
                array<bool, 2> can = {true, true};
                array<vector<pair<int, int> >, 2> hits;
                for(int k=0;k<dirs.size();++k){
                    //cerr << "at: " << i << "/" << j << "/" << k << "\n";
                    int e = dirs[k];
                    Pos p = {i, j, e};
                    vector<pair<int, int> > hit;
                    bool f = false;
                    for(;;){
                        step(p);
                        //cerr << p.x << "/" << p.y << "\n";
                        if(b[p.x][p.y] == '#') break;
                        if(b[p.x][p.y] == '-'){
                            f=true;
                            break;
                        }
                        if(b[p.x][p.y] == '|'){
                            f=true;
                            break;
                        }
                        if(b[p.x][p.y] == '.'){
                            hit.emplace_back(p.x, p.y);
                        }
                    }
                    if(f){
                        can[k%2]=0;
                    } else {
                        for(auto e:hit)
                            hits[k%2].push_back(e);
                    }
                }
                if(!can[0] && !can[1]){
                    fail = true;
                } else {
                    for(int k=0;k<2;++k){
                        if(can[k]){
                            for(auto e:hits[k]){
                                shoots[deco(e.first, e.second)].push_back((k==0?1:-1)*deco(i, j));
                            }
                        } else {
                            sat.add_true(-(k==0?1:-1)*deco(i, j));
                        }
                    }
                }
            }
        }

        if(!fail){
            for(int x=0;x<X;++x){
                //cerr << b[x] << '\n';
                for(int y=0;y<Y;++y){
                    int i = deco(x, y);
                    if(b[x][y]!='.') continue;
                    sort(shoots[i].begin(), shoots[i].end());
                    shoots[i].erase(unique(shoots[i].begin(), shoots[i].end()), shoots[i].end());
                    assert(shoots[i].size()<=2);
                    if(shoots[i].size()){
                        sat.add_or(shoots[i].front(), shoots[i].back());
                    } else {
                        fail = true;
                    }
                }
            }
            if(!sat.solve()){
                fail = true;
            }
        }
        if(fail){
            cout << "IMPOSSIBLE";
            cout << "\n";
        } else {
            cout << "POSSIBLE";
            cout << "\n";
            for(int i=1;i+1<X;++i){
                for(int j=1;j+1<Y;++j){
                    if(b[i][j] == '|' || b[i][j] == '-'){
                        b[i][j] = (sat.val[sat.index(deco(i, j))]?'|':'-');
                    }
                }
                cout << b[i].substr(1, Y-2);
                cout << "\n";
            }
        }

    }

    return 0;
}
