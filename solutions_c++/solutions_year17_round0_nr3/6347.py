//
//  main.cpp
//  Bathroom Stalls
//
//  Created by Jun Hao Xia on 09/04/17.
//  Copyright © 2017 Jun Hao Xia. All rights reserved.
//

#include <fstream>
#include <queue>
#include <vector>

bool istidy(std::string digits)
{
    for (auto it=digits.begin()+1; it!=digits.end(); ++it)
    {
        if (*(it-1) > *(it))
            return false;
    }
    return true;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    std::ifstream fin("/Users/robotex/Desktop/input.txt");
    std::ofstream fout("/Users/robotex/Desktop/output.txt", std::ios::trunc);
    size_t T, N, K;
    fin >> T;
    for (auto t=0; t<T; ++t)
    {
        fin >> N >> K;

        std::priority_queue<size_t> loc;
        
        std::vector<size_t> arr(N);
        size_t j=1, ls, rs;
        auto curr = N;
        while(j<=K && curr>0) {
            if(!loc.empty()) {
                curr = loc.top();
                loc.pop();
            }
            if(curr>0) {
                if(curr%2==0) {
                    ls = (curr/2)-1;
                    rs = curr/2;
                } else {
                    ls = (curr-1)/2;
                    rs = (curr-1)/2;
                }
            }
            
            loc.push(rs);
            loc.push(ls);
            j++;
        }
        
        fout << "Case #" << t+1 << ": " << rs << " " << ls << std::endl;
    }
    return 0;
}
