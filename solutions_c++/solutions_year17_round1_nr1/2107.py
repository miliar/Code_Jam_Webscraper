#include<bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int testcase;
    cin >> testcase;
    for(int tt = 0;tt < testcase;tt++){
        int r,c;
        cin >> r >> c;
        char grid[50][50];
        for(int i = 0;i < r;i++){
            for(int j = 0;j < c;j++){
                cin >> grid[i][j];
            }
        }
        char first[50];
        vi gg;
        gg.assign(50,-1);
        for(int i = 0;i < r;i++){
            for(int j = 0;j < c && gg[i] == -1;j++){
                if(grid[i][j] != '?'){
                    first[i] = grid[i][j];
                    gg[i] = 1;
                }
            }
        }
        for(int i = 0;i < r;i++){
            for(int j = 0;j < c;j++){
                if(gg[i] == -1){
                    if(i != 0){
                        grid[i][j] = grid[i-1][j];
                        continue;
                    }
                    int k = i+1;
                    while(gg[k] == -1 && k < r){
                        k++;
                    }
                    for(int ll = k - 1;ll >= i;ll--){
                        for(int pp = 0;pp < c;pp++){
                            grid[ll][pp] = grid[ll+1][pp];
                        }
                        first[ll] = first[ll+1];
                        gg[ll] = 1;
                    }
                }
                if(grid[i][j] == '?') grid[i][j] = first[i];
                else first[i] = grid[i][j];
            }
        }
        printf("Case #%d:\n",tt+1);
        for(int i = 0;i < r;i++){
            for(int j = 0;j < c;j++){
                cout << grid[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
