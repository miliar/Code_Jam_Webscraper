//
//  main.cpp
//  Tidy_Numbers
//
//  Created by Alexandru Andronache on 08/04/2017.
//  Copyright © 2017 Alexandru Andronache. All rights reserved.
//

#include <iostream>
#include <vector>

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int T;
char str[50];
std::vector<int> v;

bool isTidy() {
    for (int i = 0; i < v.size() - 1; ++i) {
        if (v[i] > v[i + 1]) {
            return false;
        }
    }
    return true;
}


int main(int argc, const char * argv[]) {
    
    fscanf(f, "%d\n", &T);
    for (int t = 1; t <= T; ++t) {
        fgets(str, 40, f);
        v.clear();
        
        int i = 0;
        while (str[i] >= '0' && str[i] <= '9') {
            v.push_back(str[i] - '0');
            i++;
        }
        
        if (!isTidy()) {
            i = 0;
            while (i + 1 < v.size() && v[i] <= v[i + 1]) {
                i++;
            }
            int j = i;
            while (i - 1 >= 0 && v[i] == v[i - 1]) {
                i--;
            }
            i--;
            if (i + 1 < v.size()) {
                v[i + 1] = v[i + 1] - 1;
            }
            for (int j = i + 2; j < v.size(); ++j) {
                v[j] = 9;
            }
        }
        fprintf(g, "Case #%d: ", t);
        int k = 0;
        while (v[k] == 0) {
            k++;
        }
        for (int i = k; i < v.size(); ++i) {
            fprintf(g, "%d", v[i]);
        }
        fprintf(g, "\n");
    }
    
    return 0;
}
