//
//  P3.cpp
//  Google Code Jam 2017 Qualification Round
//
//  Created by xys on 2017/4/8.
//  Copyright © 2017年 xys. All rights reserved.
//

#include <fstream>
#include <vector>
#include <iomanip>
#include <string>
using namespace std;

pair<long long, long long> calc(long long N, long long K) {
    if (K == 1) {
        return make_pair(N / 2, (N - 1) / 2);
    }
    if (K % 2 == 0) {
        return calc(N / 2, K / 2);
    }
    else {
        return calc((N - 1) / 2, (K - 1) / 2);
    }
}


int main() {
    ifstream inFile("/Users/xys/Coding/Google_Code_jam/2017/QualificationRound/C-large.in");
    ofstream outFile("/Users/xys/Coding/Google_Code_jam/2017/QualificationRound/C-large.out");
    int T;
    inFile >> T;
    for (int i = 1; i <= T; i++) {
        long long N, K;
        inFile >> N >> K;
        pair<long long, long long> ans = calc(N, K);
        outFile << "Case #" << i << ": " << ans.first << ' ' << ans.second << '\n';
    }
    inFile.close();
    outFile.close();
}
