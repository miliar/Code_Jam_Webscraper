//In the name of Allah
#include <bits/stdc++.h>
using namespace std; 

typedef long double ld; 

struct Cell { 
    int x, y, d;  
}; 

int dx[] = { 0 , -1 , 0 , 1 } , 
    dy[] = { 1 , 0 , -1 , 0 } ; 
const int maxN = 50 + 3;
const int maxK = maxN * maxN * 2; 
struct Problem { 
    string a[maxN]; 
    int id[maxN][maxN];
    int n, m; 

    int handle( char ch , int d ) { 
        if( ch == '/' ) 
            return d ^ 1; 
        return d ^ 3; 
    }

    bool gg( char ch ) { 
        return ch == '|';
    }
    char ff( Cell x ) { 
        return a[x.x][x.y]; 
    }
    bool valid( Cell x ) { 
        if( min(x.x,x.y) < 0 || x.x >= n || x.y >= m || a[x.x][x.y] == '#' )
            return false;
        return true;
    }

    Cell move( Cell curr ) { 
        while( valid( curr ) && ff(curr) != '-' && ff(curr) != '|' ) { 
            if( ff(curr) != '.' ) { 
                curr.d = handle( ff( curr ) , curr.d );
            }
            curr.x += dx[curr.d]; 
            curr.y += dy[curr.d]; 
        }
        return curr;
    }

    int cnt;
    int ans[maxK]; 
    int scc[maxK],scount;
    int mark[maxK]; 
    int lo[maxK]; 
    int st[maxK], ind; 
    vector<int> c[maxK]; 

    void add_edge( int a , int b , int c , int d ) { 
        int u = a * 2 + b , 
            v = c * 2 + d; 
        this->c[u^1].push_back(v);
        this->c[v^1].push_back(u); 
    }

    stack<int> que; 
    int dfs( int s ) {
        que.push(s);
        mark[s] = 1; 
        st[s] = lo[s] = ind++; 
        for( auto x : c[s] ) 
            if( !mark[x] ) 
                lo[s] = min( lo[s] , dfs( x ) ); 
            else if( mark[x] == 1 ) 
                lo[s] = min( lo[s] , st[x] ); 
        if( lo[s] == st[s] ) { 
            int x = -1; 
            do { 
                x = que.top();
                que.pop();
                scc[x] = scount; 
                mark[x] = 2;
            } while( x != s );
            scount++;
        }
        return lo[s];
    }

    bool solve2sat() { 
        ind = 0;
        scount=0;
        fill( mark , mark + 2 * cnt , 0 );
        for( int i = 0 ; i < 2*cnt ; i++ ) 
            if( !mark[i] ) 
                dfs( i ); 
        for( int i = 0 ; i < cnt ; i++ ) { 
            if( scc[i*2] == scc[i*2+1] ) 
                return false;
            ans[i] = ( scc[i*2] > scc[i*2+1] );
        }
        return true;
    }

    void solve() { 
        cin >> n >> m; 
        cnt = 0;
        for( int i = 0 ; i < n ; i++ ) { 
            cin >> a[i];
            for( int j = 0 ; j < m ; j++ ) 
                if( a[i][j] == '-' || a[i][j] == '|' ) 
                    id[i][j] = cnt++;
                else
                    id[i][j] = -1; 
        }

        for( int i = 0 ; i < n ; i++ ) 
            for( int j = 0 ; j < m ; j++ ) 
                if( a[i][j] != '#' ) { 
                    vector<Cell> tot; 
                    for( int d = 0 ; d < 2 ; d++ ) { 
                        Cell p1 = move( {i + dx[d] , j + dy[d] , d} );  
                        Cell p2 = move( {i + dx[d^2] , j + dy[d^2], d^2} );  

                        bool has = false;
                        if( valid(p1) && id[p1.x][p1.y] != -1 ) {
                            tot.push_back(p1);
                            has = true;
                        } else if( valid(p2) && id[p2.x][p2.y] != -1 ) { 
                            tot.push_back(p2);
                            has =true;
                        }

                        if( id[i][j] != -1 ) { 
                            if( has ) { 
                                add_edge( id[i][j] , d ^ 1 , id[i][j] , d ^ 1 );
                            }
                        } 
                    }
                    if( a[i][j] != '.' ) continue;
                    if( tot.empty() ) { 
                        cout << "IMPOSSIBLE" << endl;
                        return;
                    } else if( tot.size() == 1 ) { 
                        auto x = tot[0]; 
                        add_edge( id[x.x][x.y] , x.d % 2 , id[x.x][x.y] , x.d % 2 ); 
                    } else { 
                        auto x = tot[0], 
                             y = tot[1]; 
                        add_edge( id[x.x][x.y] , x.d % 2 , id[y.x][y.y] , y.d % 2 ); 
                    }
                }
        if( solve2sat() ) { 
            cout << "POSSIBLE" << endl;
            for( int i = 0 ; i < n ; i++ ) { 
                for( int j = 0 ; j < m ; j++ ) 
                    if( a[i][j] != '-' && a[i][j] != '|' ) 
                        cout << a[i][j]; 
                    else
                        cout << (ans[id[i][j]] ? "|" : "-" );
                cout << endl;
            }
        } else
            cout << "IMPOSSIBLE" << endl;
    }
};

int main() { 
    cout << fixed << setprecision(15); 

    int t; cin >> t; 
    for( int i = 1 ; i <= t ; i++ ) { 
        cout << "Case #" << i << ": "; 
        Problem x; 
        x.solve(); 
    }
}
