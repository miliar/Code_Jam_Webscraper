//
//  main.cpp
//  Problem1
//
//  Created by Rugen Heidbuchel on 30/04/2017.
//  Copyright © 2017 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <iomanip>
#include <math.h>

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

struct Pancake {
    double H, R;
    int id;
    
    double product() const{
        return R * H;
    }
};

bool radius_compare(const Pancake& lhs, const Pancake& rhs) {
    return lhs.R > rhs.R || (lhs.R == rhs.R && lhs.H < rhs.H);
}

bool product_compare(const Pancake& lhs, const Pancake& rhs) {
    return lhs.product() > rhs.product();
}

size_t T;

int main(int argc, const char * argv[]) {

    #ifdef USE_INPUT_FILE
    freopen("example_input.txt", "r", stdin);
    #endif
    
    std::cout << std::fixed << std::setprecision(8);
    
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cout << "Case #" << caseNumber + 1 << ": ";
        
        int N, K;
        std::cin >> N >> K;
        
        std::vector<Pancake> pancake(N);
        std::vector<Pancake> sortedOnProduct(N);
        
        for (int i = 0; i < N; i++) {
            std::cin >> pancake[i].R >> pancake[i].H;
            pancake[i].id = i;
            sortedOnProduct[i] = pancake[i];
        }
        
        std::sort(pancake.begin(), pancake.end(), radius_compare);
        std::sort(sortedOnProduct.begin(), sortedOnProduct.end(), product_compare);
        
        double maximum = 0;
        for (size_t i = 0; i <= N-K; i++) {
            Pancake &bottom = pancake[i];
            double area = (M_PI * bottom.R * bottom.R) + (2 * M_PI * bottom.product());
            int toTake = K-1;
            for (size_t j = 0; j < N; j++) {
                if (toTake == 0) break;
                Pancake &next = sortedOnProduct[j];
                if (next.R > bottom.R) continue;
                if (next.id == bottom.id) continue;
                area += 2 * M_PI * next.product();
                toTake--;
            }
            maximum = std::max(maximum, area);
        }
        
        std::cout << maximum << "\n";
    }
    
    return 0;
}
