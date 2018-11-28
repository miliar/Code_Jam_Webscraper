//
//  main.cpp
//  2
//
//  Created by Sara Kollar on 08/04/2017.
//  Copyright © 2017 Sara Kollar. All rights reserved.
//

#include <iostream>


int main(int argc, const char * argv[]) {
    
    int T;
    std::cin >> T;
    std::cin.ignore();
    
    for (int t = 1; t <= T; ++t)
    {
        std::cout << "Case #" << t << ": ";
        
        // load number as string (too long for int)
        std::string sNumber;
        std::getline(std::cin, sNumber);
        std::string tidyNumber = sNumber;

        
        // check at which digit the tidyness is messed up
        bool isTidy = true;
        char digit1 = sNumber[0];
        char digit2 = digit1;
        
        for (int i = 1; i < sNumber.length(); ++i)
        {
            digit2 = sNumber[i];
            
            // check if tidy
            if (digit1 <= digit2)
            {
                digit1 = digit2;
            }
            else
            {
                isTidy = false;
                //if not tidy, decrease first digit by 1
                tidyNumber[i-1] = --digit1;
                
                // check if this decrease made it smaller than preceding digit - if yes decrease it too and remember index where 9s should be inserted
                int start9s = i;
                
                for (int j = i - 2; j >= 0; --j)
                {
                    if ( tidyNumber[j] <= digit1)
                    {
                        break;
                    }
                    else
                    {
                        tidyNumber[j] = digit1;
                        start9s--;
                        
                    }
                }
                
                //add trailing 9s
                for (int j = start9s; j < sNumber.length(); ++j)
                {
                    tidyNumber[j] = '9';
                }
                // break out of loop if not tidy
                break;
                
            }
        }
        
        // remove 0s from beginning
        for (int i = 0; i < sNumber.length(); ++i)
        {
            if (tidyNumber[i] != '0')
            {
                tidyNumber.erase(0, i);
                break;
            }
        }
        
        std::cout << tidyNumber << std::endl;
        
    }

    return 0;
}
