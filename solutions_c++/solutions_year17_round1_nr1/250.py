#include<bits/stdc++.h>
using namespace std;
const int MX = 50;
string grid[MX];
int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int T , Tn;
    cin>>T;
    while(T--){
        int R , C;
        cin>>R>>C;
        for(int j = 1 ; j <= R ; j++){
            cin>>grid[j];
            grid[j] = "#" + grid[j];
        }
        for(int row = 1 ; row <= R ; row++){
            for(int col = 2 ; col <= C ; col++)
                if(grid[row][col] == '?')
                 grid[row][col] = grid[row][col-1];
            for(int col = C - 1 ; col ; col--)
                if(grid[row][col] == '?')
                    grid[row][col] = grid[row][col + 1];
        }
        for(int col = 1 ; col <= C ; col++){
            for(int row = 2 ; row <= R ; row++)
                if(grid[row][col] == '?')
                    grid[row][col] = grid[row-1][col];
            for(int row = R - 1 ; row ; row--)
                if(grid[row][col] == '?')
                    grid[row][col] = grid[row+1][col];
        }
        printf("Case #%d:\n",++Tn);
        for(int row = 1 ; row <= R ; row++){
            cout<<grid[row].substr(1 , C)<<endl;
        }
    }
}

