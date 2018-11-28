#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int T, AC, AJ, C, D;
    bitset<1505> Cfree, Jfree;
    short dp1[721][721];
    short dp2[721][721];
    cin >> T;
    for (int i = 1; i <= T; ++i){
        cin >> AC >> AJ;
        Cfree.set();
        Jfree.set();
        for (int j = 1; j <= AC; ++j){
            cin >> C >> D;
            for (int k = C; k <= D-1; ++k){
                Cfree[k] = 0;
            }
        }
        for (int j = 1; j <= AJ; ++j){
            cin >> C >> D;
            for (int k = C; k <= D-1; ++k){
                Jfree[k] = 0;
            }
        }
        for (int j = 0; j <= 720; ++j){
            for (int l = 0; l <= 720; ++l){
                dp1[j][l] = dp2[j][l] = 10000;
            }
        }
        dp1[0][0] = dp2[0][0] = 0;
        for (int j = 0; j <= 720; ++j){
            for (int l = 0; l <= 720; ++l){
                if (Cfree[j+l] == 1){
                    if (j > 0){
                        dp1[j][l] = min(dp1[j][l],dp1[j-1][l]);
                    }
                    if (l > 0){
                        dp1[j][l] = min(dp1[j][l],(short)(dp2[j][l-1]+1));
                    }
                }
                if (Jfree[j+l] == 1){
                    if (l > 0){
                        dp2[j][l] = min(dp2[j][l],dp2[j][l-1]);
                    }
                    if (j > 0){
                        dp2[j][l] = min(dp2[j][l],(short)(dp1[j-1][l]+1));
                    }
                }
            }
        }
        cout << "Case #" << i << ": " << min(dp1[720][720],dp2[720][720])+(min(dp1[720][720],dp2[720][720])&(short)1) << '\n';
    }
    return 0;
}


