//
//  P1.cpp
//  Google Code Jam 2017 Qualification Round
//
//  Created by xys on 2017/4/8.
//  Copyright © 2017年 xys. All rights reserved.
//

#include <fstream>
#include <vector>
#include <iomanip>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    ifstream inFile("/Users/xys/Coding/Google_Code_jam/2017/QualificationRound/A-large.in");
    ofstream outFile("/Users/xys/Coding/Google_Code_jam/2017/QualificationRound/A-large.out");
    int T;
    inFile >> T;
    for (int i = 1; i <= T; i++) {
        string S;
        int K;
        inFile >> S >> K;
        
        int stepCnt = 0;
        int UB = S.length() - K;
        int j = 0;
        for (; j <= UB; j++) {
            if (S[j] == '-') {
                stepCnt++;
                S[j] = '+';
                for (int l = j + 1; l < j + K; l++) {
                    S[l] = S[l] == '-' ? '+' : '-';
                }
            }
        }
        for (; j < S.length(); j++) {
            if (S[j] == '-') {
                outFile << "Case #" << i << ": IMPOSSIBLE\n";
                break;
            }
        }
        if (j == S.length()) {
            outFile << "Case #" << i << ": " << stepCnt << '\n';
        }
    }
    inFile.close();
    outFile.close();
}
