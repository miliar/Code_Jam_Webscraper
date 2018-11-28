#include <ios>
#include <iostream>
#include <cstdio>
#include <string>

int main()
{
    //std::ios_base::sync_with_stdio(false);
    //std::cin.tie(NULL);
    //std::cout.tie(NULL);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc, k;
    std::string s;
    std::cin >> tc;
    for (int t = 0; t < tc; t++)
    {
        std::cout << "Case #" << t+1 << ": ";
        std::cin >> s >> k;
        int flips = 0;
        for (int i = 0; i < s.length(); i++)
        {
            if (s.at(i) == '-')
            {
                flips++;
                if (i+k > s.length())
                {
                    flips = -1;
                    break;
                }
                for (int j = i; j < i+k; j++)
                {
                    if (s.at(j) == '+')
                        s[j] = '-';
                    else
                        s[j] = '+';
                }
            }
        }
        if (flips == -1)
            std::cout << "IMPOSSIBLE\n";
        else
            std::cout << flips << '\n';
    }
}
