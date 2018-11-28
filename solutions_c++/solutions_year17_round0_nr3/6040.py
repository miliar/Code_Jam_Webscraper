//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Mikhail Kharlov on 05.04.17.
//  Copyright © 2017 Mikhail Kharlov. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>

class Range
{
public:
    Range(long long l, long long r) : left(l), right(r)
    {
        length = right - left + 1;
        middle = (left + right) / 2;
    }
    
public:
    long long left;
    long long right;
    long long length;
    long long middle;
};

inline bool operator< (const Range &range1, const Range &range2)
{
    if (range1.length == range2.length)
        return (range1.left >= range2.left);
    return (range1.length < range2.length);
}


int main(int argc, const char * argv[])
{
    int t;
    std::cin >> t;
    
    int test = 0;
    while (test ++ < t)
    {
        long long n, k;
        std::cin >> n >> k;
        
        std::vector<Range> v;
        v.push_back(Range(0, n - 1));
        
        long long left = 0;
        long long right = 0;
        for (long long i = 0; i < k; i ++)
        {
            Range max = v.front();
            
            Range range1(max.left, max.middle - 1);
            Range range2(max.middle + 1, max.right);
            
            std::pop_heap(v.begin(), v.end());
            v.pop_back();
            
            if (range1.length > 0)
            {
                v.push_back(range1);
                std::push_heap(v.begin(), v.end());
            }
            
            if (range2.length)
            {
                v.push_back(range2);
                std::push_heap(v.begin(), v.end());
            }
            
            left = max.middle - max.left;
            right = max.right - max.middle;
        }
        std::cout << "Case #" << test << ": ";
        std::cout << std::max(left, right) << " " << std::min(left, right) << std::endl;
    }
    
    return 0;
}

































