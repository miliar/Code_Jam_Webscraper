#include <bits/stdc++.h>

using namespace std;
ifstream f("d.in");
ofstream g("d.out");

const int NMax = 100;

int t,n,m;
char x[NMax][NMax];

int main()
{
    f >> t;
    for(int count = 1; count <= t; ++ count){
        f >> n >> m;
        f.get();
        memset(x,0,sizeof(x));
        for(int i = 0; i < n; ++i){
            f.getline(x[i],NMax);
        }

        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){

                if(x[i][j] != '?'){
                    for(int k = j - 1; k >= 0 && x[i][k] == '?'; --k){
                        x[i][k] = x[i][j];
                    }
                }

            }
        }
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                if(x[i][j] != '?'){
                    for(int k = j + 1; k < m && x[i][k] == '?'; ++k){
                        x[i][k] = x[i][j];
                    }
                }
            }
        }
        for(int j = 0; j < m; ++j){
            for(int i = 0; i < n; ++i){
                if(x[i][j] != '?'){
                    for(int k = i - 1; k >= 0 && x[k][j] == '?'; --k){
                        x[k][j] = x[i][j];
                    }
                }
            }
        }
        for(int j = 0; j < m; ++j){
            for(int i = 0; i < n; ++i){
                if(x[i][j] != '?'){
                    for(int k = i + 1; k < n && x[k][j] == '?'; ++k){
                        x[k][j] = x[i][j];
                    }
                }
            }
        }
        g << "Case #" << count << ":" << '\n';
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                g << x[i][j];
            }
            g << '\n';
        }
    }
    return 0;
}
