// P1
//  P1.cpp
//  Google code jam 2017 round 1B
//
//  Created by xys on 2017/4/23.
//  Copyright © 2017年 xys. All rights reserved.
//

#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    ifstream inFile("/Users/xys/Coding/Google_Code_jam/2017/Round1B/A-large.in");
    ofstream outFile("/Users/xys/Coding/Google_Code_jam/2017/Round1B/A-large.out");
    int T;
    inFile >> T;
    for (int i = 1; i <= T; i++) {
        int D, N;
        inFile >> D >> N;
        vector<pair<int, int>> horse(N);
        for (int j = 0; j < N; j++) {
            inFile >> horse[j].first >> horse[j].second;
        }
        auto myComp = [](pair<int, int> &p1, pair<int, int> &p2) {
            return p1.first > p2.first;
        };
        sort(horse.begin(), horse.end(), myComp);
        double s = D + 1;
        double curTime = 0;
        for (int j = N - 1; j >= 0; j--) {
            double tmp = double(D - horse[j].first) / horse[j].second;
            if (tmp > curTime) {
                curTime = tmp;
            }
        }
        outFile << "Case #" << i << ": " << std::fixed << std::setprecision(6) << D / curTime << '\n';
    }
    inFile.close();
    outFile.close();
}
