//
//  main.cpp
//  Oversized Pancake Flipper
//
//  Created by Jun Hao Xia on 08/04/17.
//  Copyright © 2017 Jun Hao Xia. All rights reserved.
//

#include <fstream>

int main(int argc, const char * argv[]) {
    // insert code here...
    std::ifstream fin("/Users/robotex/Desktop/input.txt");
    std::ofstream fout("/Users/robotex/Desktop/output.txt", std::ios::trunc);
    std::string S;
    size_t T, K;
    fin >> T;
    for (auto t=0; t<T; ++t)
    {
        size_t flips = 0;
        fin >> S >> K;
        size_t pancakes = S.length();
        for (auto i=0; i<pancakes; ++i)
        {
            if (S[i] == '-')
            {
                ++flips;
                for (auto j=i; j<i+K; ++j)
                {
                    if (j>=pancakes)
                    {
                        flips = 0xDEADC0DE;
                        break;
                    }
                    else
                        S[j] = S[j] == '+' ? '-' : '+';
                }
            }
        }
        fout << "Case #" << t+1 << ": " << (flips != 0xDEADC0DE ? std::to_string(flips) : "IMPOSSIBLE") << std::endl;
    }
    return 0;
}
