#include <bits/stdc++.h>

using namespace std;

#define foi(i,k,n)  for(int i = (int)k; i < (int)n; ++i)
int R,C,area;
char mat[40][40];
char curr;
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};
bool done[500];

inline bool in(int x, int y) {
    return x >= 0 && x < R && y >= 0 && y < C;
}

void dfs(int x, int y) {
    mat[x][y] = curr;
    int xto, yto;
    foi(i,0,4) {
        xto = x + dx[i];
        yto = y + dy[i];
        if(in(xto, yto) && mat[xto][yto] == '?')
            dfs(xto, yto);
    }
}

void undfs(int x, int y, bool flag) {
    if(flag)
        mat[x][y] = '?';
    int xto, yto;
    foi(i,0,4) {
        xto = x + dx[i];
        yto = y + dy[i];
        if(in(xto, yto) && mat[xto][yto] == curr)
            undfs(xto, yto,true);
    }
}

bool works(int i, int j, int p, int q) {
    area = 0;
    foi(x,i,1 + p)
        foi(y,j,1 + q) {
            if(mat[x][y] != curr)   return false;
            ++area;
        }
    return true;
}

bool works2(int x, int y, int i, int j, int p, int q) {
    return x >= i && x <= p && y >= j && y <= q;
}

void color(int i, int j, int p, int q) {
    //cout << "Coloreando con la letra " << curr << " de [" << i << "," << j << "] a [" << p << "," << q << "]" << endl;
    foi(x,i,1 + p)
        foi(y,j,1 + q)  mat[x][y] = curr;
    //cout << "After" << endl;
    /*foi(f,0,R) {
        foi(g,0,C)
            cout << mat[f][g];
        cout << endl;
    }*/
}

void solve2(int x, int y) {
    //cout << "Buscando colorear desde la posicion " << x << "," << y << endl;
    curr = mat[x][y];
    done[curr] = true;
    //cout << "Which is also " << curr << endl;
    dfs(x,y);
    int ii = -1,jj,pp,qq;
    int m = -1;
    foi(i,0,R)
        foi(j,0,C)
            foi(p,i,R)
                foi(q,j,C)
                    if(works2(x,y,i,j,p,q) && works(i,j,p,q))
                        if(area > m) {
                            ii = i;
                            jj = j;
                            pp = p;
                            qq = q;
                            m = area;
                        }
    undfs(x,y,false);
    if(~ii)color(ii,jj,pp,qq);
}

void solve() {
    foi(i,0,R)
        foi(j,0,C)
            if(mat[i][j] != '?' && !done[mat[i][j]])
                solve2(i,j);
}

int main() {
    int c = 0;
    cin >> c;
    foi(k,0,c) {
        cin >> R >> C;
        foi(i,0,R)  foi(j,0,C)  cin >> mat[i][j];
        /*cout << "Solve" << endl;
        foi(i,0,R) {
            foi(j,0,C)
                cout << mat[i][j];
                cout << endl;
        }*/
        memset(done, false, sizeof done);
        //cout << "----------\n";
        solve();
        cout << "Case #" << 1 + k << ":\n";
        foi(i,0,R) {
            foi(j,0,C){
                if(mat[i][j] == '?')    cout << "WTF!!" << endl;
                cout << mat[i][j];
            }
            cout << endl;
        }
        //cout << "*************************\n";
    }
    return 0;
}
