#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 1000000007;

vector<string> field;

int R, C;

bool used[50][50];
int shooted[50][50];

int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};

int get_dir(int dir, char mirror){
    if(mirror == '\\'){
        if(dir == 0) return 1;
        if(dir == 1) return 0;
        if(dir == 2) return 3;
        if(dir == 3) return 2;
    }else if(mirror == '/'){
        if(dir == 0) return 3;
        if(dir == 3) return 0;
        if(dir == 1) return 2;
        if(dir == 2) return 1;
    }
    assert(0);
    return 0;
}

pair<int, int> find_shooter(int y, int x, int dir){
    if(y < 0 || R <= y || x < 0 || C <= x || field[y][x] == '#'|| used[y][x]) return make_pair(-1, -1);
    if(field[y][x] == '|' || field[y][x] == '-'){
        if(dir == 0 || dir == 2){
            field[y][x] = '-';
        }else{
            field[y][x] = '|';
        }
        return make_pair(y, x);
    }

    if(field[y][x] == '\\' || field[y][x] == '/'){
        dir = get_dir(dir, field[y][x]);
    }
    return find_shooter(y + dy[dir], x + dx[dir], dir);
}

bool shoot(int y, int x, int dir, int diff){
    if(y < 0 || R <= y || x < 0 || C <= x || field[y][x] == '#') return true;
    if(field[y][x] == '|' || field[y][x] == '-') return false;

    if(field[y][x] == '\\' || field[y][x] == '/'){
        dir = get_dir(dir, field[y][x]);
    }
    shooted[y][x] += diff;
    return shoot(y + dy[dir], x + dx[dir], dir, diff);
}

bool dfs(int y, int x){
    // cout << y << " " << x << endl;
    // for(int i=0;i<R;i++){
    //     cout << field[i] << endl;
    // }
    // for(int i=0;i<R;i++){
    //     for(int j=0;j<C;j++){
    //         cout << shooted[i][j];
    //     }
    //     cout << endl;
    // }
    if(x >= C) return dfs(y+1, 0);
    if(y == R) return true;
    if(field[y][x] == '.' && shooted[y][x] == 0){
        for(int dir=0;dir<2;dir++){
            auto p = find_shooter(y, x, dir);
            if(p.first != -1){
                int sy = p.first, sx = p.second;
                used[sy][sx] = true;

                int offset = field[sy][sx] == '-' ? 0 : 1;
                bool ok = shoot(sy + dy[offset], sx + dx[offset], offset, 1) && shoot(sy + dy[offset + 2], sx + dx[offset + 2], offset + 2, 1);
                // cout << "ok " << ok << " " << dir << " " << field[sy][sx] << endl;
                if(ok && dfs(y, x+1)){
                    return true;
                }
                shoot(sy + dy[offset], sx + dx[offset], offset, -1) && shoot(sy + dy[offset + 2], sx + dx[offset + 2], offset + 2, -1);

                used[sy][sx] = false;
            }
        }
        return false;
    }else if((field[y][x] == '|' || field[y][x] == '-') && !used[y][x]){
        for(int offset=0;offset<2;offset++){
            field[y][x] = offset == 0 ? '-' : '|';
            used[y][x] = true;
            bool ok = shoot(y + dy[offset], x + dx[offset], offset, 1) && shoot(y + dy[offset + 2], x + dx[offset + 2], offset + 2, 1);
            if(ok && dfs(y, x+1)){
                return true;
            }
            shoot(y + dy[offset], x + dx[offset], offset, -1) && shoot(y + dy[offset + 2], x + dx[offset + 2], offset + 2, -1);
            used[y][x] = false;
        }
        return false;
    }else{
        return dfs(y, x+1);
    }
}

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        cin >> R >> C;

        field.resize(R);
        for(int i=0;i<R;i++){
            cin >> field[i];
        }
        memset(shooted, 0, sizeof(shooted));
        memset(used, 0, sizeof(used));

        printf("Case #%d: ", t);
        if(dfs(0, 0)){
            cout << "POSSIBLE" << endl;
            for(int i=0;i<R;i++){
                cout << field[i] << endl;
            }
        }else{
            cout << "IMPOSSIBLE" << endl;
        }

    }

    return 0;
}