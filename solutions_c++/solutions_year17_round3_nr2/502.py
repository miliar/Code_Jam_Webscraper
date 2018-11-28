#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <sstream>
#include <string>
#include <map>
#include <set>
#include <stdlib.h>
#include <cmath>
#include <math.h>
#include <fstream>
#include <bitset>
#include <time.h>
#define int long long
using namespace std;
int t, ac, aj, l, r;
int dp[1441][721][2][2];
int32_t main(){
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    in >> t;
    for (int it=0;it<t;it++){
        cout << it << endl;
        in >> ac >> aj;
        vector<int> zan;
        for (int i=0;i<=2400;i++){
            zan.push_back(-1);
        }
        for (int i=0;i<ac;i++){
            in >> l >> r;
            for (int j=l+1;j<=r;j++){
                zan[j] = 0;
            }
        }
        for (int i=0;i<aj;i++){
            in >> l >> r;
            for (int j=l+1;j<=r;j++){
                zan[j] = 1;
            }
        }
        for (int i=0;i<=1440;i++){
            for (int j=0;j<=720;j++){
                for (int k=0;k<2;k++){
                    for (int m=0;m<2;m++){
                        dp[i][j][k][m] = 100000000;
                    }
                }
            }
        }
        dp[0][0][0][0] = 0;
        dp[0][0][0][1] = 0;
        dp[0][0][1][0] = 0;
        dp[0][0][1][1] = 0;
        for (int i=1;i<=1440;i++){
            for (int j=0;j<=720;j++){
                for (int k=0;k<2;k++){
                    if (zan[i] == k) continue;
                    for (int m=0;m<2;m++){
                        if (m != k && i == 1) continue;
                        if (k == 0){
                            if (j == 0) continue;
                            dp[i][j][k][m] = min(dp[i][j][k][m], dp[i-1][j-1][k][m]);
                            dp[i][j][k][m] = min(dp[i][j][k][m], dp[i-1][j-1][1-k][m] + 1);
                        }
                        else{
                            dp[i][j][k][m] = min(dp[i][j][k][m], dp[i-1][j][k][m]);
                            dp[i][j][k][m] = min(dp[i][j][k][m], dp[i-1][j][1-k][m] + 1);
                        }
                    }
                }
            }
        }
        dp[1440][720][0][1] ++;
        dp[1440][720][1][0] ++;
        int answer = 100000000;
        for (int i=0;i<2;i++){
            for (int j=0;j<2;j++){
                answer = min(answer, dp[1440][720][i][j]);
            }
        }
        out << "Case #" << it+1 << ": " << answer << endl;
    }
    return 0;
}
