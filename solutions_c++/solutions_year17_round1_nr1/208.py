#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(void) {
    int T; cin >> T;
    for(int ts=1; ts<=T; ts++) {
        int R,C; cin >> R >> C;
        vector<string> grid(R);
        for(int r=0; r<R; r++) cin >> grid[r];
        string prev="";
        for(int r=0; r<R; r++) {
            if(grid[r]==string(C,'?')) {
                grid[r]=prev;
            } else {
                int i;
                for(i=0; i<C; i++) if(grid[r][i]!='?') break;
                char c=grid[r][i];
                for(int i=0; i<C; i++) {
                    if(grid[r][i]!='?') c=grid[r][i];
                    grid[r][i]=c;
                }
                prev=grid[r];
            }
        }
        for(int r=R-1; r>=0; r--)
            if(grid[r]=="") grid[r]=grid[r+1];
        cout << "Case #" << ts << ":" << endl;
        for(int r=0; r<R; r++) cout << grid[r] << endl;
    }
}
