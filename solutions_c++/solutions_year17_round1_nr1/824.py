#include <iostream>
#define MAX_R 27
using namespace std;
char grid[MAX_R][MAX_R];
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin >> T;
    for(int z = 1; z <= T; z++) {
        int R, C;
        cin >> R >> C;
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                cin >> grid[i][j];
            }
        }
        for(int i = 0; i < R; i++) {
            char seen = '?';
            for(int j = 0; j < C; j++) {
                if(grid[i][j] == '?' && seen != '?') {
                    grid[i][j] = seen;
                } else {
                    seen = grid[i][j];
                }
            }
            seen = '?';
            for(int j = C-1; j >= 0; j--) {
                if(grid[i][j] == '?' && seen != '?') {
                    grid[i][j] = seen;
                } else {
                    seen = grid[i][j];
                }
            }
        }
        int li = -1;
        for(int i = 0; i < R; i++) {
            if(grid[i][0] == '?' && li != -1) {
                for(int j = 0; j < C; j++) {
                    grid[i][j] = grid[li][j];
                }
            } else if(grid[i][0] != '?') {
                li = i;
            }
        }
        li = -1;
        for(int i = R - 1; i >= 0; i--) {
            if(grid[i][0] == '?' && li != -1) {
                for(int j = 0; j < C; j++) {
                    grid[i][j] = grid[li][j];
                }
            } else if(grid[i][0] != '?') {
                li = i;
            }
        }

        cout << "Case #" << z <<":\n";
        for(int i=  0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                cout << grid[i][j];
            }
            cout <<"\n";
        }
    }


}
