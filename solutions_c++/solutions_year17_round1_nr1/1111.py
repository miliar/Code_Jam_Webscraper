#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;
char grid[30][30];
int main () {
    freopen("/Users/bowbowbow/Downloads/A-large.in", "r", stdin);
    freopen("/Users/bowbowbow/Downloads/A-large.out", "w", stdout);
    
    int T;
    cin >> T;
    for(int t=1;t<=T;t++) {
        int R, C;
        cin >> R >> C;
        for(int i=1;i<=R;i++) {
            scanf("%s", grid[i]+1);
        }
        
        for(int i=1;i<=R;i++){
            for(int j=1;j<=C;j++) {
                if(grid[i][j] == '?') continue;
                
                int ny = i-1, nx = j;
                while(ny>=1) {
                    if(grid[ny][nx] != '?') break;
                    grid[ny][nx] = grid[i][j];
                    ny--;
                }
                ny = i+1, nx = j;
                while(ny<=R) {
                    if(grid[ny][nx] != '?') break;
                    grid[ny][nx] = grid[i][j];
                    ny++;
                }
            }
        }
        
        for(int i=1;i<=R;i++){
            for(int j=1;j<=C;j++) {
                if(grid[i][j] == '?') continue;
                int ny = i, nx = j+1;
                while(nx <= C) {
                    if(grid[ny][nx] != '?') break;
                    grid[ny][nx] = grid[i][j];
                    nx++;
                }
                ny = i, nx = j-1;
                while(nx >=1) {
                    if(grid[ny][nx] != '?') break;
                    grid[ny][nx] = grid[i][j];
                    nx--;
                }
            }
        }
        
        cout << "Case #"<< t << ":" << endl;
        for(int i=1;i<=R;i++){
            for(int j=1;j<=C;j++){
                cout << grid[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
