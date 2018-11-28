//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Mikhail Kharlov on 05.04.17.
//  Copyright © 2017 Mikhail Kharlov. All rights reserved.
//

#include <iostream>
#include <string>

static bool validate_string(std::string &string)
{
    for (int i = 0; i < string.length(); i ++)
        if (string[i] == '-')
            return false;
    return true;
}

static void change_string(std::string &string, int start, int finish)
{
    for (int i = start; i < finish; i ++)
        string[i] = (string[i] == '+') ? '-' : '+';
}

int main(int argc, const char * argv[])
{
    int t;
    std::cin >> t;
    
    int g = 0;
    while (g++ < t)
    {
        std::string string;
        std::cin >> string;
        
        int k;
        std::cin >> k;
        
        int count = 0;
        for (int i = 0; i <= string.length() - k; i ++)
        {
            if (string[i] == '-')
            {
                count ++;
                change_string(string, i, i + k);
            }
        }
        
        if (validate_string(string))
            std::cout << "Case #" << g << ": " << count << std::endl;
        else std::cout << "Case #" << g << ": IMPOSSIBLE" << std::endl;
    }
    
    return 0;
}




































