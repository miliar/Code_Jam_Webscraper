#include"bits/stdc++.h"
using namespace std;
char a[30][30];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("ans.out", "w", stdout);
    int T;
    int r, c;
    cin >> T;
    for(int cas = 1; cas <= T; cas ++){
        cin >> r >> c;
        for(int i = 0; i < r; i ++){
            cin >> a[i];
        }
        printf("Case #%d:\n", cas);
        for(int i = 0; i < c; i ++){
            for(int j = 0; j < r; j ++){
                if(a[j][i] != '?'){
                    for(int k = j - 1; k >= 0; k --){
                        if(a[k][i] == '?'){
                            a[k][i] = a[j][i];
                        }
                        else{
                            break;
                        }
                    }
                }
            }
            for(int j = r - 1; j >= 0; j --){
                if(a[j][i] != '?'){
                    for(int k = j + 1; k < r; k ++){
                        a[k][i] = a[j][i];
                    }
                    break;
                }
            }
        }
        for(int i = 0; i < c; i ++){
            if(a[0][i] == '?'){
                if(i == c - 1){
                    for(int j = c - 2; j >= 0; j --){
                        if(a[0][j] != '?'){
                            for(int k = j + 1; k < c; k ++){
                                for(int p = 0; p < r; p ++){
                                    a[p][k] = a[p][j];
                                }
                            }
                            break;
                        }
                    }
                }
                else{
                    for(int j = i + 1; j < c; j ++){
                        if(a[0][j] != '?'){
                            for(int k = i; k < j; k ++){
                                for(int p = 0; p < r; p ++){
                                    a[p][k] = a[p][j];
                                }
                            }
                            break;
                        }
                    }
                }
            }
        }
        for(int i = 0; i < r; i ++){
            cout << a[i] << endl;
        }
    }
    return 0;
}
