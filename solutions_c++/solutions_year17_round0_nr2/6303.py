//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Mikhail Kharlov on 05.04.17.
//  Copyright © 2017 Mikhail Kharlov. All rights reserved.
//

#include <iostream>
#include <vector>

static const int SizeNumber = 18;

static void decompose_number(std::vector<int> &v, long long number)
{
    int k = 0;
    while (number > 0)
    {
        v[k++] = number % 10;
        number /= 10;
    }
}

static void print_result(std::vector<int> &v, int test)
{
    int position = 0;
    for (int i = SizeNumber - 1; i >= 0; i --)
    {
        if (v[i] > 0)
        {
            position = i;
            break;
        }
    }
    
    std::cout << "Case #" << test << ": ";
    for (int i = position; i >= 0; i --)
        std::cout << v[i];
    std::cout << std::endl;
}

int main(int argc, const char * argv[])
{
    int t;
    std::cin >> t;
    
    int test = 0;
    while (test++ < t)
    {
        long long number;
        std::cin >> number;
        
        std::vector<int> v(SizeNumber);
        decompose_number(v, number);
        
        for (int i = SizeNumber - 1; i > 0; i --)
        {
            if (v[i] > v[i - 1])
            {
                int pos = i;
                for (int j = i + 1; j < SizeNumber; j ++)
                    if (v[j] >= v[i])
                        pos = j;
                
                v[pos] --;
                for (int j = pos - 1; j >= 0; j --)
                    v[j] = 9;
                
                break;
            }
        }
        print_result(v, test);
    }
    
    return 0;
}





































































