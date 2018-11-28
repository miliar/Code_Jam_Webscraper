//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Mikhail Kharlov on 05.04.17.
//  Copyright © 2017 Mikhail Kharlov. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <utility>

int main(int argc, const char * argv[])
{
    std::cout.precision(9);
    std::cout.setf(std::ios::fixed, std:: ios::floatfield);
    
    int t = 0;
    std::cin >> t;
    
    int test = 0;
    while (test++ < t)
    {
        int d, n;
        std::cin >> d >> n;
        
        std::vector<double> v(n);
        for (int i = 0; i < n; i ++)
        {
            int k, s;
            std::cin >> k >> s;
            
            double dist = d - k;
            double time = dist / s;
         
            v[i] = time;
        }
        auto it = std::max_element(v.begin(), v.end());
        
        double speed = (double)(d) / (*it);
        std::cout << "Case #" << test << ": " << speed << std::endl;
    }
    return 0;
}




































