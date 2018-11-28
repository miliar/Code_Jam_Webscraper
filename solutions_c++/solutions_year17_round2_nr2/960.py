//
//  main.cpp
//  Stable Neigh-bors
//
//  Created by Robotex on 22/04/17.
//  Copyright © 2017 Robotex. All rights reserved.
//

#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <sstream>

int main(int argc, const char * argv[]) {
    // insert code here...
    std::ifstream fin("/Users/robotex/Desktop/input.txt");
    std::ofstream fout("/Users/robotex/Desktop/output.txt", std::ios::trunc);
    size_t T;
    size_t N, R, O, Y, G, B, V;
    fin >> T;
    
    for (auto t=0; t<T; ++t)
    {
        std::vector<std::pair<size_t,char>> vec;
        fin >> N >> R >> O >> Y >> G >> B >> V;
        
        vec.emplace_back(std::make_pair(R, 'R'));
        vec.emplace_back(std::make_pair(Y, 'Y'));
        vec.emplace_back(std::make_pair(B, 'B'));
        
        std::sort(vec.begin(), vec.end(), [](std::pair<size_t,char> l, std::pair<size_t,char> r) { return l.first>r.first;});
        
        bool isImpossible = false;
        std::ostringstream result;
        if (!vec[2].first)
        {
            if (vec[0].first == vec[1].first)
                for (auto i=0; i<vec[0].first; i++)
                {
                    result << vec[0].second << vec[1].second;
                }
            else
                isImpossible = true;
        }
        else
        {
            if (vec[0].first > vec[1].first + 1)
                isImpossible = true;
            else if (vec[0].first == vec[1].first + 1)
            {
                size_t h = vec[1].first - vec[2].first;
                for (auto i=0; i<h; ++i)
                {
                    result << vec[0].second << vec[1].second;
                }
                result << vec[2].second;
                for (auto i=0; i<vec[2].first; ++i)
                {
                    result << vec[1].second << vec[0].second << vec[2].second;
                }
            }
            else
            {
                size_t h = vec[1].first - vec[2].first;
                for (auto i=0; i<h; ++i)
                {
                    result << vec[0].second << vec[1].second;
                }
                result << vec[2].second;
                for (auto i=0; i<vec[2].first; ++i)
                {
                    result << vec[0].second << vec[1].second << vec[2].second;
                }
            }
        }
        
        fout << "Case #" << t+1 << ": " << (isImpossible ? "IMPOSSIBLE" : result.str() ) << std::endl;
    }
    return 0;
}
