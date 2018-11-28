//
//  main.cpp
//  Problem3
//
//  Created by Rugen Heidbuchel on 22/04/2017.
//  Copyright © 2017 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <iomanip>

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

size_t T;
int N, Q;

int main(int argc, const char * argv[]) {

    #ifdef USE_INPUT_FILE
    freopen("example_input.txt", "r", stdin);
    #endif
    
    std::cout << std::fixed << std::setprecision(8);
    
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cout << "Case #" << caseNumber + 1 << ": ";
        
        std::cin >> N >> Q;
        std::vector<double> E(N), S(N), D(N), t(N, 0);
        
        for (size_t i = 0; i < N; i++) {
            std::cin >> E[i] >> S[i];
        }
        
        for (size_t i = 0; i < N; i++) {
            for (size_t j = 0; j < N; j++) {
                double dist;
                std::cin >> dist;
                if (i+1 == j) {
                    D[i] = dist;
                }
            }
        }
        
        for (size_t i = 0; i < Q; i++) {
            int a, b;
            std::cin >> a >> b;
        }
        
        for (int i = N-2; i >= 0; i--) {
            double distanceLeft = E[i] - D[i], time = D[i]/S[i];
            if (distanceLeft < 0) {
                t[i] = std::numeric_limits<double>::max();
                continue;
            }
            int j = i+1;
            double minTime = time + t[i+1];
            while (true) {
                minTime = std::min(minTime, time + t[j]);
                distanceLeft -= D[j];
                time += D[j]/S[i];
                j++;
                if (distanceLeft < 0 || j >= N) {
                    break;
                }
            }
            t[i] = minTime;
        }
        
        std::cout << t[0] << "\n";
    }
    
    return 0;
}
