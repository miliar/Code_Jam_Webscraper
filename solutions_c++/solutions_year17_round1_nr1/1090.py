//
//  P1.cpp
//  GoogleAPAC
//
//  Created by xys on 2017/4/15.
//  Copyright © 2017年 xys. All rights reserved.
//

#include <fstream>
#include <vector>
using namespace std;

int main() {
    ifstream inFile("/Users/xys/Coding/Google_Code_jam/2017/Round1A/A-large.in");
    ofstream outFile("/Users/xys/Coding/Google_Code_jam/2017/Round1A/A-large.out");
    int T;
    inFile >> T;
    for (int i = 1; i <= T; i++) {
        int R, C;
        inFile >> R >> C;
        vector<vector<char>> gridVec(R, vector<char>(C, '?'));
        for (int j = 0; j < R; j++) {
            for (int k = 0; k < C; k++) {
                inFile >> gridVec[j][k];
            }
        }
        
        int rowIdx = 0;
        for (int j = 0; j < R; j++) {
            int fillIdx = 0;
            if (gridVec[j][0] != '?') {
                fillIdx++;
            }
            for (int k = 1; k < C; k++) {
                if (gridVec[j][k] == '?') {
                    if (fillIdx == k) {
                        gridVec[j][k] = gridVec[j][k - 1];
                        fillIdx++;
                    }
                }
                else {
                    for (int s = fillIdx; s < k; s++) {
                        gridVec[j][s] = gridVec[j][k];
                    }
                    fillIdx = k + 1;
                }
            }
            if (fillIdx != 0) {
                // fill up
                if (j > rowIdx) {
                    for (int k = rowIdx; k < j; k++) {
                        for (int s = 0; s < C; s++) {
                            gridVec[k][s] = gridVec[j][s];
                        }
                    }
                }
                rowIdx = j + 1;
            }
        }
        if (rowIdx < R) {
            for (int j = rowIdx; j < R; j++) {
                for (int k = 0; k < C; k++) {
                    gridVec[j][k] = gridVec[rowIdx - 1][k];
                }
            }
        }
        outFile << "Case #" << i << ":\n";
        for (int j = 0; j < R; j++) {
            for (int k = 0; k < C; k++) {
                outFile << gridVec[j][k];
            }
            outFile << '\n';
        }
    }
    inFile.close();
    outFile.close();
}
