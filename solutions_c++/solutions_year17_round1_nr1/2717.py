
#include <list>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <iostream>
using namespace std;


int main() {
    int nTest;
    cin >> nTest;
    for(int iTest = 1; iTest <= nTest; iTest++) {
        int R,C;
        cin >> R >> C;
        vector<string> grid;
        vector<bool> ColIsOk;
        for (int iRow = 0; iRow < R ; iRow++) {
            string aRow;
            cin >> aRow;
            grid.push_back(aRow);
            ColIsOk.push_back(false);
        }
        for(int j=0; j<C ; j++) {
            int i=0;
            while(i < R && grid[i][j]=='?'){
                i++;
            }
            if(i==R) {
                continue;
            }
            ColIsOk[j] = true;
            for(int ii=0; ii < i; ii++) {
                grid[ii][j] = grid[i][j];
            }
            for(int ii=i+1; ii < R; ++ii) {
                if(grid[ii][j]=='?') {
                   grid[ii][j] = grid[ii-1][j];
                }
            }
        }
        
        /*for(int i = 0; i < R; ++i) {
            for(int j =0; j < C; ++j) {
                if(grid[i][j]>='A' && grid[i][j]<='Z') {
                    ColIsOk[j]= true;
                    int ku =1;
                    while(i+ku < R && grid[i+ku][j]=='?') {
                        grid[i+ku][j]==grid[i][j];
                        ku++;
                    }
                    int kd =1;
                    while(i-ku > 0 && grid[i-ku][j]=='?') {
                        grid[i+ku][j]==grid[i][j];
                        ku++;
                    }
                }
            }
        }*/
        int jj;
        for(jj=0; jj <C; ++jj) {
            if(ColIsOk[jj]) {
                break;
            }
        }
        for(int j=0; j<jj;++j) {
               
                    for(int i=0; i < R; ++i) {
                        grid[i][j] = grid[i][jj];
                    }
                
        }
        
        for(int j=jj+1; j<C;++j) {
                if(!ColIsOk[j]) {
                    for(int i=0; i < R; ++i) {
                        grid[i][j] = grid[i][j-1];
                    }
                }
        }

        cout << "Case #" << iTest << ":\n";
        for(int i =0; i<R; ++i) {
            cout << grid[i] << endl;

        }
    }
    return 0;
}
