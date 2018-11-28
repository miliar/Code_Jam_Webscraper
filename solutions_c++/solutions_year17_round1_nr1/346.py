#include <bits/stdc++.h>
using namespace std;

char grid[100][100];
int R, C;

int first_non_empty_line(){
    for (int i=0; i<R; i++){
        for (int j=0; j<C; j++){
            if (grid[i][j] != '?')
                return i;
        }
    }
    return -1;
}

void fill_line(int line){
    char last = '?';
    for (int i=0; i<C; i++){
        if (grid[line][i] == '?' && last != '?') {
            grid[line][i] = last;
        } else if (grid[line][i] != '?') {
            last = grid[line][i];
        }
    }
    last = '?';
    for (int i=C-1; i>=0; i--){
        if (grid[line][i] == '?' && last != '?') {
            grid[line][i] = last;
        } else if (grid[line][i] != '?') {
            last = grid[line][i];
        }
    }
}

bool empty(int line){
    for (int j=0; j<C; j++){
        if (grid[line][j] != '?')
            return false;
    }
    return true;
}

// row b takes values of row a
void move_to(int a, int b){
    for (int j=0; j<C; j++){
        grid[b][j] = grid[a][j];
    }
}

void solve(){
    cin >> R >> C;
    for (int i=0; i<R; i++){
        for (int j=0; j<C; j++){
            cin >> grid[i][j];
        }
    }
    
    int first = first_non_empty_line();
    fill_line(first);
    for (int i=0; i<first; i++){
        move_to(first, i);
    }
    for (int i=first+1; i<R; i++){
        if (empty(i)) {
            move_to(i-1, i);
        } else {
            fill_line(i);
        }
    }
    for (int i=0; i<R; i++){
        for (int j=0; j<C; j++){
            cout << grid[i][j];
        }
        cout << endl;
    }
}

int main(){
    int T;
    cin >> T;
    for (int i=1; i<=T; i++){
        cout << "Case #" << i << ":" << endl;
        solve();
    }
}
