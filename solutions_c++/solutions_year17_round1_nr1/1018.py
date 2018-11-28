#include <bits/stdc++.h>
using namespace std;
vector<string> grid;
int r, c;
vector<pair<int, int>> points;
void fill1(int x, int y){
    for(int i = y + 1;i < c;i++){
        if(grid[x][i] != '?')break;
        grid[x][i] = grid[x][y];
    }
    for(int i = y - 1;i >= 0;i--){
        if(grid[x][i] != '?')break;
        grid[x][i] = grid[x][y];
    }
}
void fill_above(int x){//cout << x << endl;
    for(int i = x - 1;i >= 0;i--){
        if(grid[i][0] != '?')break;
        for(int j = 0;j < c;j++){
            grid[i][j] = grid[i + 1][j];
        }
    }

}
void fill_below(int x){//cout << x << endl;
    for(int i = x + 1;i < r;i++){
        if(grid[i][0] != '?')break;
        for(int j = 0;j < c;j++){
            grid[i][j] = grid[i - 1][j];
        }
    }

}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    for(int cs = 0;cs < tc;cs++){
        points.clear();
        grid.clear();
        cin >> r >> c;
        string str;
        for(int i = 0;i < r;i++){
            cin >> str;
            grid.push_back(str);
            for(int j = 0;j < c;j++){
                if(str[j] != '?'){
                    fill1(i, j);

                }
            }
            fill_above(i);
        }
        int i = r - 1;
        for(;i >= 0;i--){
            if(grid[i][0] != '?')break;
        }
        fill_below(i);
        printf("Case #%d:\n", cs + 1);
        for(int i = 0;i < r;i++){
            cout << grid[i] << endl;
        }

    }
}
