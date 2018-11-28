// P2_Small
//  P2.cpp
//  GoogleAPAC
//
//  Created by xys on 2017/4/15.
//  Copyright © 2017年 xys. All rights reserved.
//

#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    ifstream inFile("/Users/xys/Coding/Google_Code_jam/2017/Round1A/B-small-attempt1.in");
    ofstream outFile("/Users/xys/Coding/Google_Code_jam/2017/Round1A/B-small-attempt1.out");
    int T;
    inFile >> T;
    for (int i = 1; i <= T; i++) {
        int N, P;
        inFile >> N >> P;
        vector<int> reqVec(N, 0);
        for (int j = 0; j < N; j++) {
            inFile >> reqVec[j];
        }
        vector<vector<int>> pacVec(N, vector<int>(P, 0));
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < P; k++) {
                inFile >> pacVec[j][k];
            }
            sort(pacVec[j].begin(), pacVec[j].end());
        }
        vector<vector<int>> lbVec(N, vector<int>(P, 0)), ubVec(N, vector<int>(P, 0));
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < P; k++) {
                lbVec[j][k] = ceil((double)pacVec[j][k] / reqVec[j] / 1.1);
                ubVec[j][k] = (double)pacVec[j][k] / reqVec[j] / 0.9;
            }
        }
        
        int kitCnt = 0;
        if (N == 1) {
            for (int k = 0; k < P; k++) {
                if (lbVec[0][k] <= ubVec[0][k]) {
                    kitCnt++;
                }
            }
        }
        else {
            // N == 2
            vector<vector<int>> dp(P + 1, vector<int>(P + 1, 0));
            for (int j = 1; j <= P; j++) {
                for (int k = 1; k <= P; k++) {
                    dp[j][k] = max(dp[j - 1][k], dp[j][k - 1]);
                    if (lbVec[0][j - 1] <= ubVec[1][k - 1] && ubVec[0][j - 1] >= lbVec[1][k - 1]) {
                        dp[j][k] = max(1 + dp[j - 1][k - 1], dp[j][k]);
                    }
                }
            }
            kitCnt = dp[P][P];
        }
        outFile << "Case #" << i << ": " << kitCnt << '\n';
    }
    inFile.close();
    outFile.close();
}
