//
//  main.cpp
//  Oversized_Pancake_Flipper
//
//  Created by Alexandru Andronache on 08/04/2017.
//  Copyright © 2017 Alexandru Andronache. All rights reserved.
//

#include <iostream>
#include <vector>

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int T;
char str[1030];
std::vector<int> v;

int main(int argc, const char * argv[]) {
    fscanf(f, "%d\n", &T);
    for (int t = 1; t <= T; ++t) {
        fgets(str, 1030, f);
        
//        if (t == 36)
//        {
//            std::cout << "a";
//        }
        
        v.clear();
        int N = 0;
        for (int i = 0; i <= strlen(str); ++i) {
            if (str[i] == '-') {
                v.push_back(0);
            }
            else if (str[i] == '+') {
                v.push_back(1);
            }
            else if (str[i] >= '0' && str[i] <= '9') {
                N = N * 10 + str[i] - '0';
            }
        }
        
        long long rez = 0;
        int li = 0;
        int ls = (int)v.size() - 1;
        while (ls - li >= N) {
            if (v[li] == 0) {
                for (int i = 0; i < N; ++i) {
                    v[li + i] = !v[li + i];
                }
                rez++;
                li++;
            }
            else if (v[ls] == 0) {
                for (int i = 0; i < N; ++i) {
                    v[ls - i] = !v[ls - i];
                }
                rez++;
                ls--;
            }
            else {
                li++;
                ls--;
            }
        }
        int neg = 0;
        for (int i = li; i <= ls; ++i) {
            if (v[i] == 0) {
                neg++;
            }
        }
        
        if (neg == N) {
            rez++;
        }
        
        if (neg == 0 || neg == N) {
            fprintf(g, "Case #%d: %lld\n", t, rez);
        }
        else {
            fprintf(g, "Case #%d: IMPOSSIBLE\n", t);
        }
    }
    
    return 0;
}
