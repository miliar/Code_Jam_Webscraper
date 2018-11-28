//
//  main.cpp
//  problem3
//
//  Created by Joyce Zhang on 4/7/17.
//  Copyright © 2017 Joyce Zhang. All rights reserved.
//

#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>
struct Cell{
    int min;
    int max;
};


int easy(int n, int k) {
    if (k==1) return n;
    int level = floor(log2(k));
    int split = pow(2, level);
    int base  = (n-split+1) / split;
    int extra = (n-split+1) % split;
    int remainingStep = k - (split-1);
    //std::cout << "k: " << k << " base: " << base << " extra: " << extra << " remaining: " << remainingStep << std::endl;
    if (remainingStep <= extra)
        return base + 1;
    else
        return base;
}

/*Cell findIt(int n, int k, std::vector<Cell> &res){
    std::vector<int> process = {n};
    if (k < res.size())
        return res[k-1];
    //std::cout << "not using cached data";
    for (int i=0; i<k; i++){
        int ma = *std::max_element(process.begin(),  process.end());
        process.erase(std::max_element(process.begin(), process.end()));
        if (ma == 0)
            res.push_back({0,0});
        else
            res.push_back({(ma-1)/2, (ma)/2});
        process.push_back((ma-1)/2);
        process.push_back((ma-1)/2 + (ma-1)%2);
    }
    return res[k-1];
}*/

int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << argc << argv[0] << std::endl;
    //const char* filename = argv[1];
    //std::ifstream infile(filename);
    /*for (int i = 1; i < 7; ++i) {
        std::cout << i<< ' ' << easy(6, i) << std::endl;
    }*/
    /*std::cout<< easy(6, 2) << std::endl;
    std::cout<< easy(5, 2) << std::endl;
    std::cout<< easy(4, 2) << std::endl;
    std::cout << easy(1000, 1000) << std::endl;
    std::cout << easy(999999, 475712) << std::endl;
    std::cout << easy(999999, 499999) << std::endl;
    std::cout << easy(1000000, 493916) << std::endl;
    std::cout << easy(430602, 325185) << std::endl;
    std::cout << easy(2,2) << std::endl;
    std::cout << easy(1000000, 262143) << std::endl;*/
    int number;
    std::cin >> number;
    
    std::vector<Cell> input;
    int max_n=0;
    for (int i = 0; i < number; i++){
        int n, k;
        if (std::cin >> n >> k) {
            input.push_back({n, k});
            if (n > max_n) max_n = n;
        }
    }
    
    std::vector<std::vector <Cell>> res(max_n, std::vector<Cell>(0));
    std::vector<Cell> result;
    for (int i = 0; i < input.size(); ++i) {
        int aa = easy(input[i].min, input[i].max);
        std::cout << "Case #" << i+ 1 << ": " << aa/2 << ' ' << (aa-1)/2 << "\n";
    }
    
    return 0;
}
