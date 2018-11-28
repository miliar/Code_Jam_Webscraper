//
//  main.cpp
//  Bathroom Stalls
//
//  Created by Rugen Heidbuchel on 08/04/2017.
//  Copyright © 2017 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>

// Shortcuts for "common" data types in contests
typedef long long ll;
typedef std::vector<int> vi;
typedef std::pair<int, int> ii;
typedef std::vector<ii> vii;
typedef std::set<int> si;
typedef std::map<std::string, int> msi;

// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000 // 2 billion

// If you need to recall how to use memset:
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array of integers


#pragma mark - MAIN

std::pair<size_t, size_t> answer(size_t N, size_t K) {
    
    if (K == 1) {
        if (N % 2 == 0) {
            return {N/2 - 1, N/2};
        } else {
            return {N/2, N/2};
        }
    }
    
    --K;
    if (N % 2 == 0) {
        if (K % 2 == 0) {
            return answer(N/2 - 1, K/2);
        } else {
            return answer(N/2, K/2 + 1);
        }
    } else {
        if (K % 2 == 0) {
            return answer(N/2, K/2);
        } else {
            return answer(N/2, K/2 + 1);
        }
    }
}

size_t T, N, K;

int main(int argc, const char * argv[]) {

    #ifdef USE_INPUT_FILE
    freopen("example_input.txt", "r", stdin);
    #endif
    
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cout << "Case #" << caseNumber + 1 << ": ";
        
        std::cin >> N >> K;

        std::pair<size_t, size_t> minMax = answer(N, K);
        
        std::cout << minMax.second << " " << minMax.first << "\n";
    }
    
    return 0;
}
