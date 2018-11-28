//
//  main.cpp
//  Cruise Control
//
//  Created by Robotex on 22/04/17.
//  Copyright © 2017 Robotex. All rights reserved.
//

#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>

int main(int argc, const char * argv[]) {
    // insert code here...
    std::ifstream fin("/Users/robotex/Desktop/input.txt");
    std::ofstream fout("/Users/robotex/Desktop/output.txt", std::ios::trunc);
    size_t T, D, N;
    fin >> T;
    
    for (auto t=0; t<T; ++t)
    {
        double max = 0;
        fin >> D >> N;
        for (auto i=0; i<N; ++i)
        {
            size_t K, S;
            fin >> K >> S;
            
            max = std::max(static_cast<typeof max>(D-K)/S, max);
        }

        fout << "Case #" << t+1 << ": " << std::fixed << static_cast<typeof max>(D/max) << std::endl;
    }
    return 0;
}
