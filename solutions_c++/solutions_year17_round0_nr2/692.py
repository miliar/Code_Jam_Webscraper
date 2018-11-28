//
//  P2.cpp
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
    ifstream inFile("/Users/xys/Coding/Google_Code_jam/2017/QualificationRound/B-large.in");
    ofstream outFile("/Users/xys/Coding/Google_Code_jam/2017/QualificationRound/B-large.out");
    int T;
    inFile >> T;
    for (int i = 1; i <= T; i++) {
        long long N;
        inFile >> N;
        int NLen = log10(N) + 1;
        vector<int> digitVec(NLen + 1, 0);
        for (int i = NLen; i > 0; i--) {
            digitVec[i] = N % 10;
            N /= 10;
        }
        vector<int> ansVec;
        ansVec.push_back(0);
        int idx = 1;
        while (idx <= NLen) {
            ansVec.push_back(digitVec[idx]);
            if (ansVec[idx] < ansVec[idx - 1]) {
                while (idx > 0) {
                    if (ansVec[idx] >= ansVec[idx - 1]) {
                        break;
                    }
                    else {
                        ansVec.pop_back();
                        idx--;
                        ansVec.back() = ansVec.back() - 1;
                    }
                }
                ansVec.insert(ansVec.end(), NLen - idx, 9);
                idx = NLen;
                break;
            }
            idx++;
        }
        idx = 0;
        while (ansVec[idx] == 0) {
            idx++;
        }
        outFile << "Case #" << i << ": ";
        for (; idx < ansVec.size(); idx++) {
            outFile << ansVec[idx];
        }
        outFile << '\n';
    }
    inFile.close();
    outFile.close();
}
