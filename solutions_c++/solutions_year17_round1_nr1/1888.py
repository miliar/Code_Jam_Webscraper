#include <bits/stdc++.h>
using namespace std;






int main() {
    freopen("inputA","r",stdin);
    freopen("outputA","w",stdout);
    int tests;
    cin>>tests;
    for (int T = 1; T <= tests; ++T) {
        int R,C;
        cin>>R>>C;
        char grid[R][C];
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                cin>>grid[i][j];
            }
        }

        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if(grid[i][j]!='?'){
                    char t=grid[i][j];
                    int k=j-1;
                    while(k>=0&&grid[i][k]=='?') {grid[i][k]=t;k--;};
                    k=j+1;
                    while(k<C&&grid[i][k]=='?'){grid[i][k]=t;k++;};
                    j=k-1;
                }
            }
        }
        for (int i = 0; i < R; ++i) {
            if(grid[i][0]!='?'){
                int k=i-1;
                while(k>=0&&grid[k][0]=='?'){
                    for (int j = 0; j < C; ++j) {
                        grid[k][j]=grid[i][j];
                    }
                    k--;
                }
                k=i+1;
                while(k<R&&grid[k][0]=='?'){
                    for (int j = 0; j < C; ++j) {
                        grid[k][j]=grid[i][j];
                    }
                    k++;
                }
            }
        }












        cout<<"Case #"<<T<<": "<<endl;
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                cout<<grid[i][j];
            }
            cout<<endl;
        }

    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
