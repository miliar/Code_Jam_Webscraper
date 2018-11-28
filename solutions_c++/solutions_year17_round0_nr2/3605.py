#include <iostream>
#include <algorithm>
#include <numeric>

std::string solve(std::string v)
{
    std::string minV(v.size(), '\0');
    std::partial_sum(v.rbegin(), v.rend(), minV.rbegin(), [](char a, char b) { return std::min(a, b); });
    if (v[0] == '1' && minV.front() == '0')
    {
        return std::string(v.size() - 1, '9');
    }
    std::string ans(v.size(), '1');
    char c = '1';
    for (size_t i = 0; i < v.size(); i++)
    {
        std::string next = ans;
        while (c < '9')
        {
            std::fill(next.begin() + i, next.end(), c + 1);
            if (next <= v)
            {
                ans = next;
                c++;
            }
            else
            {
                break;
            }
        }
    } 
    return ans;
    
}

int main()
{
    int t;
    std::cin >> t;
    for (int i=1; i<=t; i++)
    {
        std::string v;
        std::cin >> v;
        std::cout << "Case #" << i << ": " << solve(v) << "\n";
    }
}
