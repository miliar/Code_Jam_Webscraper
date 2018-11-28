#include <bits/stdc++.h>
using namespace std;

int height, width;
string grid[30];

bool done(){
    for(int i=0; i<height; i++){
        for(int j=0; j<width; j++){
            return false;
        }
    }
    return true;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t = 0;
    cin >> t;
    for(int i=1; i<=t; i++){
        cin >> height >> width;
        for(int j=0; j<height; j++) cin >> grid[j];
        for(int j=0; j<height; j++){
            for(int k=0; k<width; k++){
                if(grid[j][k]!='?'){
                    for(int l=j+1; l<height; l++){
                        if(grid[l][k]!='?') break;
                        grid[l][k] = grid[j][k];
                    }
                }
            }
        }
        for(int j=0; j<height; j++){
            for(int k=0; k<width; k++){
                if(grid[j][k]!='?'){
                    for(int l=j-1; l>=0; l--){
                        if(grid[l][k]!='?') break;
                        grid[l][k] = grid[j][k];
                    }
                }
            }
        }
        for(int j=0; j<height; j++){
            for(int k=1; k<width; k++){
                if(grid[j][k]=='?') grid[j][k] = grid[j][k-1];
            }
        }
        for(int j=0; j<height; j++){
            for(int k=width-2; k>=0; k--){
                if(grid[j][k]=='?') grid[j][k] = grid[j][k+1];
            }
        }
        cout << "Case #" << i << ":" << endl;
        for(int j=0; j<height; j++) cout << grid[j] << endl;
    }
    return 0;
}
