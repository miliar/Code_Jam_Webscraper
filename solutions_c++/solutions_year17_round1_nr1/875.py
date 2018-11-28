#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int, int>;
const ll MOD = 1000000007;


int main(){

    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int R, C;
        cin >> R >> C;
        vector<string> cake(R);
        for(int i=0;i<R;i++){
            cin >> cake[i];
        }

        for(int j=0;j<C;j++){
            for(int i=1;i<R;i++){
                if(cake[i][j] == '?'){
                    cake[i][j] = cake[i-1][j];
                }
            }
        }
        for(int j=0;j<C;j++){
            for(int i=R-2;i>=0;i--){
                if(cake[i][j] == '?'){
                    cake[i][j] = cake[i+1][j];
                }
            }
        }
        for(int i=0;i<R;i++){
            for(int j=1;j<C;j++){
                if(cake[i][j] == '?'){
                    cake[i][j] = cake[i][j-1];
                }
            }
        }
        for(int i=0;i<R;i++){
            for(int j=C-2;j>=0;j--){
                if(cake[i][j] == '?'){
                    cake[i][j] = cake[i][j+1];
                }
            }
        }
        printf("Case #%d:\n", t);
        for(int i=0;i<R;i++){
            cout << cake[i] << endl;
        }
    }

    return 0;
}