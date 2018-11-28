//
//  main.cpp
//  codejam
//
//  Created by Hyunjun Kim on 2017. 4. 8..
//  Copyright © 2017년 Hyunjun Kim. All rights reserved.
//

#include <iostream>
#include <queue>
#include <cstdint>
#include <cassert>

namespace ProblemC {
    
#define trace(msg) std::cout << msg << std::endl
//#define trace(msg) void()
    


// n + 2 stalls
// k person
void solve(int64_t n, int64_t k) {
    int64_t left_vacant = -1;
    int64_t right_vacant = -1;
    
    std::priority_queue<int64_t> pq;  // for consecutive vacant stalls
    pq.push(n);
    
    for (int i = 0; i < k; ++i) {
        assert(!pq.empty());
        
        int64_t vacant = pq.top();
        pq.pop();
        
        vacant -= 1;  // occupied by persion i
        left_vacant = vacant / 2;
        right_vacant = vacant - left_vacant;
        
        pq.push(left_vacant);
        pq.push(right_vacant);
    }
    
    assert(left_vacant != -1);
    assert(right_vacant != -1);
    
    // print solution - or return pair
    if (left_vacant > right_vacant)
        std::cout << left_vacant << " " << right_vacant << std::endl;
    else
        std::cout << right_vacant << " " << left_vacant << std::endl;
}

void test() {
    assert(INT64_MAX > 1e18);
    //trace("Test OK");
}
    
}  // namespace ProblemC


int main(int argc, const char* argv[]) {
    ProblemC::test();
    
//    ProblemC::solve(4, 2);
//    ProblemC::solve(5, 2);
//    ProblemC::solve(6, 2);
//    ProblemC::solve(1000, 1000);
//    ProblemC::solve(1000, 1);
    
    int t;
    int64_t n, k;
    
    std::cin >> t;
    for (int tc = 0; tc < t; ++tc) {
        std::cin >> n >> k;
        std::cout << "Case #" << (tc + 1) << ": ";
        ProblemC::solve(n, k);
    }
    
    return 0;
}
