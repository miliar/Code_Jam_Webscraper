#include <iostream>
#include <cmath>
#include <cstdio>
#include <map>
using namespace std;
int r,c,t;

char grid[30][30];
char cakeused(int r1, int c1, int r2, int c2){
    int rmin = min(r1,r2);
    int rmax = max(r1,r2);
    int cmin = min(c1,c2);
    int cmax = max(c1,c2);
    int chars = 0;
    char ans;
    for(int y = rmin; y <= rmax; y++){
        for(int x = cmin; x <= cmax; ++x){
            if(grid[y][x] != '?'){
                ans = grid[y][x];
                chars++;
            }
        }    
    }
    if(chars == 1){
        return ans;
    }
    return '?';
}

int main(){
    cin >> t;
    for(int t_case = 0; t_case < t; t_case++){
        cin >> r >> c;
        //get input
        cin.get();
        for(int row = 0; row < r; row++){
            for(int col = 0; col < c; col++){
                cin.get(grid[row][col]);
            }
            cin.get();
        }
        
        map<char,int> used;
        for(int a = 0; a < r; ++a){
            for(int b = 0; b < c; ++b){
                for(int y = r-1; y >= a; --y){
                    for(int x = c-1; x >= b; --x){

                        char anser = cakeused(a,b,y,x);
                        if(anser != '?'){
                            if(used[anser] == 1){
                                continue;
                            }
                            used[anser] = 1;
                            for(int i = a; i <= y; ++i){
                                for(int j = b; j <= x; ++j){
                                    grid[i][j] = anser;
                                }
                            }

                            
                        }
                    }
                }
            }
        }

        

        // print ans
        cout << "Case #"<<t_case+1<<":"<<endl;
        for(int row = 0; row < r; row++){
            for(int col = 0; col < c; col++){
                cout << grid[row][col];
            }
            cout << endl;
        }
    }
}
