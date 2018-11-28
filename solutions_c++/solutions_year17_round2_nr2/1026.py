//
//  main.cpp
//  Problem2
//
//  Created by Rugen Heidbuchel on 22/04/2017.
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

size_t T;
int N, R, O, Y, G, B, V;

int main(int argc, const char * argv[]) {

    #ifdef USE_INPUT_FILE
    freopen("example_input.txt", "r", stdin);
    #endif
    
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cout << "Case #" << caseNumber + 1 << ": ";
        
        std::cin >> N >> R >> O >> Y >> G >> B >> V;
        std::string s(N, '.');
        if (R > 0) {
            R--;
            s[0] = 'R';
        } else if (Y > 0) {
            Y--;
            s[0] = 'Y';
        } else if (B > 0) {
            B--;
            s[0] = 'B';
        }
        
        bool possible = true;
        for (int i = 1; i < N; i++) {
            char c = s[i-1];
            if (c == 'R') {
                if (Y > B) {
                    Y--;
                    s[i] = 'Y';
                } else if (B > 0) {
                    B--;
                    s[i] = 'B';
                } else {
                    possible = false;
                    break;
                }
            } else if (c == 'B') {
                if (Y > R) {
                    Y--;
                    s[i] = 'Y';
                } else if (R > 0) {
                    R--;
                    s[i] = 'R';
                } else {
                    possible = false;
                    break;
                }
            } else if (c == 'Y') {
                if (R > B) {
                    R--;
                    s[i] = 'R';
                } else if (B > 0) {
                    B--;
                    s[i] = 'B';
                } else {
                    possible = false;
                    break;
                }
            }
        }
        
        if (s[N-1] == s[0]) {
            possible = false;
        }
        
        if (possible) {
            std::cout << s;
        } else {
            std::cout << "IMPOSSIBLE";
        }
        
        std::cout << "\n";
    }
    
    return 0;
}
