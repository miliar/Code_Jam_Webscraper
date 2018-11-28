//
//  main.cpp
//  Tidy Numbers
//
//  Created by Jun Hao Xia on 09/04/17.
//  Copyright © 2017 Jun Hao Xia. All rights reserved.
//

#include <fstream>
#include <sstream>

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
    size_t T, N;
    fin >> T;
    for (auto t=0; t<T; ++t)
    {
        fin >> N;
        std::string digits;
        std::ostringstream oss;
        
        oss << N;
        digits = oss.str();
        
        if (N > 9)
        {
            if (!istidy(digits))
            {
                for (auto i=digits.length()-1; i>0; --i)
                {
                    if (digits[i] < digits[i-1])
                    {
                        for (auto j=i; j<digits.length(); ++j)
                            digits[j]='9';
                        digits[i-1]=digits[i-1]-1;
                        if (digits[i-1]=='0')
                            ++i;
                    }
                    bool flag=false;
                    while (digits[i]=='0')
                    {
                        flag=true;
                        --i;
                    }
                    if (flag)
                    {
                        digits[i]=digits[i]-1;
                        for (auto j=i+1; j<digits.length(); ++j)
                            digits[j]='9';
                        if (digits[i]=='0')
                            ++i;
                    }
                }
                auto startidx = digits.find_first_not_of("0");
                digits = digits.substr(startidx, digits.length() - startidx + 1);
            }
        }
        fout << "Case #" << t+1 << ": " << digits << std::endl;
    }
    return 0;
}
