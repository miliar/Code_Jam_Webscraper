//
//  main.cpp
//  1
//
//  Created by Sara Kollar on 08/04/2017.
//  Copyright © 2017 Sara Kollar. All rights reserved.
//


#include <iostream>
#include <vector>
#include <string>

void flip(std::vector<bool> &pancakes, int K, int start)
{
    for (int i = start; i < start + K; ++i)
    {
        pancakes[i] = !pancakes[i];
    }
}

int main(int argc, const char * argv[]) {
    // read stack of pancakes
    int T;
    std::cin >> T;
    std::cin.ignore();
    
    for (int t = 1; t <= T; ++t)
    {
        // output line
        std::cout << "Case #" << t << ": ";
        
        // read pancake stack from file

        std::vector<bool> vPancakes;
        std::string sPancakes;
        std::getline(std::cin, sPancakes, ' ');
        
        // convert string to vector of bools
        for (int j = 0; j < sPancakes.size(); ++j)
        {
            if (sPancakes[j] == '+')
            {
                vPancakes.push_back(true);
            }
            else if (sPancakes[j] == '-')
            {
                vPancakes.push_back(false);
            }
        }
        
        //read flip capacity from file
        int K;
        std::cin >> K;
        std::cin.ignore();
        
        
        int flipped = 0;
        int impossible = false;
        // start flipping!
        
        // flip if not happy
        for (int i = 0; i < vPancakes.size(); ++i)
        {
            // flip
            if (i <= vPancakes.size() - K)
            {
                if (!vPancakes[i])
                {
                    flip(vPancakes, K, i);
                    flipped++;
                }
            }
            // can't flip starting from this index - check if they are happy
            else
            {
                if (!vPancakes[i])
                {
                    impossible = true;
                    std::cout << "IMPOSSIBLE"<< std::endl;
                    break;
                }
            }
        }
        
        if (!impossible)
        {
            std::cout<< flipped << std::endl;
        }
        
        
    }
    return 0;
}

