//
//  main.cpp
//  codejam
//
//  Created by Hyunjun Kim on 2017. 4. 8..
//  Copyright © 2017년 Hyunjun Kim. All rights reserved.
//

#include <iostream>
#include <string>
#include <cassert>

#define TRACE(msg) std::cout << msg << std::endl
#define MAX_PANCAKES 1000
#define IMPOSSIBLE -1

int solve(const std::string& pancakes, int filpper_size) {
    size_t pancakes_len = pancakes.length();
    bool is_happyside[MAX_PANCAKES];
    int flip_count = 0;

    assert(filpper_size >= 2);
    assert(pancakes_len >= filpper_size);
    assert(pancakes_len <= MAX_PANCAKES);
    
    // parse string
    for (int i = 0; i < pancakes_len; ++i) {
        is_happyside[i] = (pancakes[i] == '+');
//        TRACE(is_happyside[i]);
    }
    
    // start flip from the front
    for (int i = 0; i < pancakes_len; ++i) {
        if (is_happyside[i]) {
            continue;
        }
        
        // done or impossible
        if (i + filpper_size > pancakes_len) {
            for (int j = i; j < pancakes_len; ++j) {
                if (!is_happyside[j]) {
                    return IMPOSSIBLE;
                }
            }
            return flip_count;
        }
        
        // flip consecutive filpper_size pancakes
        for (int j = i; j < i + filpper_size; ++j) {
            is_happyside[j] = !is_happyside[j];
        }
        ++flip_count;
    }
    
    return flip_count;
}

int main(int argc, const char* argv[]) {
    
//    TRACE(solve("---+-++-", 3));
//    TRACE(solve("+++++", 4));
//    TRACE(solve("-+-+-", 4));
    
    int t, k;
    std::string s;
    
    std::cin >> t;
    for (int tc = 0; tc < t; ++tc) {
        std::cin >> s >> k;
        
        int result = solve(s, k);
        
        std::cout << "Case #" << (tc + 1) << ": ";
        if (result == IMPOSSIBLE)
            std::cout << "IMPOSSIBLE";
        else
            std::cout << result;
        std::cout << std::endl;
    }
    
    
    return 0;
}
