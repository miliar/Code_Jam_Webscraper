#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

namespace
{
    using Val = unsigned int;
    using LVal = unsigned long long int;
    using ValCol = vector<Val>;

    LVal lastTidy(LVal v)
    {
        ValCol digits;
        while(v != 0)
        {
            digits.push_back(v%10);
            v /= 10;
        }
        for(auto iter = begin(digits); iter != end(digits); ++iter)
        {
            auto maxIter = max_element(iter, end(digits));
            if(maxIter != end(digits))
            {
                if(*maxIter > *iter)
                {
                    *iter = 9;
                    auto nextIter = iter;
                    ++nextIter;
                    for(; nextIter != end(digits); ++nextIter)
                    {
                        if(*nextIter > 0)
                        {
                            *nextIter -= 1;
                            break;
                        }
                        else
                        {
                            *nextIter = 9;
                        }
                    }
                    for(auto prevIter = begin(digits); prevIter != iter; ++prevIter)
                        *prevIter = 9;
                }
            }
        }
        LVal r = 0;
        LVal mult = 1;
        for(auto v : digits)
        {
            r += v*mult;
            mult *= 10;
        }
        return r;
    }
}

int main()
{
    int t = 0;
    cin>>t;
    for(int i = 0; i < t; ++i)
    {
        LVal v = 0;
        cin>>v;
        cout<<"Case #"<<i+1<<": "<<lastTidy(v)<<endl;
    }
    return 0;
}
