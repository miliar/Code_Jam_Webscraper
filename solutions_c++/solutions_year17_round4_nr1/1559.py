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
int t, n, q, ai;
int dp[101][101][101][101];
int32_t main(){
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    in >> t;
    for (int i=0;i<t;i++){
        in >> n >> q;
        int init[4];
        for (int j=0;j<4;j++){
            init[j] = 0;
        }
        int summ = 0;
        for (int j=0;j<n;j++){
            in >> ai;
            summ += ai;
            init[ai%q]++;
        }
        for (int j=0;j<=n;j++){
            for (int k=0;k<=init[0];k++){
                for (int m=0;m<=init[1];m++){
                    for (int p=0;p<=init[2];p++){
                        dp[j][k][m][p] = -1;
                    }
                }
            }
        }
        dp[0][0][0][0] = 1;
        for (int j=1;j<=n;j++){
            for (int k=0;k<=init[0];k++){
                for (int m=0;m<=init[1];m++){
                    for (int p=0;p<=init[2];p++){
                        int u3 = j - k - m - p;
                        if (u3 > init[3] || u3 < 0) continue;
                        int pl = 0;
                        if (((m + 2*p + 3*u3) % q) == 0) pl++;
                        if (k>0) dp[j][k][m][p] = max(dp[j][k][m][p], dp[j-1][k-1][m][p] + pl);
                        if (m>0) dp[j][k][m][p] = max(dp[j][k][m][p], dp[j-1][k][m-1][p] + pl);
                        if (p>0) dp[j][k][m][p] = max(dp[j][k][m][p], dp[j-1][k][m][p-1] + pl);
                        if (u3>0) dp[j][k][m][p] = max(dp[j][k][m][p], dp[j-1][k][m][p] + pl);
                    }
                }
            }
        }
        int minn = 0;
        if (summ % q == 0) minn ++;
        out << "Case #" << i+1 << ": " << dp[n][init[0]][init[1]][init[2]] - minn << endl;
    }
    return 0;
}
