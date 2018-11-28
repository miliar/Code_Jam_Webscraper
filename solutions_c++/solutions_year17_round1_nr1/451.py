#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int R, C;
        cin >> R >> C;

        vector<string> gridstr(R);
        for(int i=0;i<R;i++){
            cin >> gridstr[i];
        }
        vector<char> gridrow(C);
        vector<vector<char> > grid(R, gridrow);
        for(int r=0;r<R;r++){
            for(int c=0;c<C;c++){
                grid[r][c] = gridstr[r][c];
            }
        }
/*
        for(int r=0;r<R;r++){
            for(int c=0;c<C;c++){
                if(grid[r][c]!='?'){
                    for(int a=0;a<=r;a++){
                        for(int b=0;b<=c;b++){
                            if(grid[a][b]=='?') grid[a][b]= grid[r][c];
                        }
                    }
                }
            }
        }*/

        // prop right
        for(int r=0;r<R;r++){
            for(int c=1;c<C;c++){
                if(grid[r][c]=='?') grid[r][c] = grid[r][c-1];
            }
        }

        // prop left
        for(int r=0;r<R;r++){
            for(int c=C-2;c>=0;c--){
                if(grid[r][c]=='?') grid[r][c] = grid[r][c+1];
            }
        }

        // prop down
        for(int r=1;r<R;r++){
            for(int c=0;c<C;c++){
                if(grid[r][c]=='?') grid[r][c] = grid[r-1][c];
            }
        }

        // prop up
        for(int r=R-2;r>=0;r--){
            for(int c=0;c<C;c++){
                if(grid[r][c]=='?') grid[r][c] = grid[r+1][c];
            }
        }


        
        cout << "Case #" << t << ": " << endl;
        for(int r=0;r<R;r++){
            for(int c=0;c<C;c++){
                cout << grid[r][c];
            }
            cout << endl;
        }
    }

    return 0;
}