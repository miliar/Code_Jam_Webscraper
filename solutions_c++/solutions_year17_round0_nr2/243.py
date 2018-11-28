#include <ios>
#include <iostream>
#include <cstdio>

int main()
{
    //std::ios_base::sync_with_stdio(false);
    //std::cin.tie(NULL);
    //std::cout.tie(NULL);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    std::string s;
    std::cin >> tc;
    for (int t = 0; t < tc; t++)
    {
        std::cout << "Case #" << t+1 << ": ";
        std::cin >> s;
        bool tidy = true;
        int stop = -1;
        for (int i = 1; i < s.length(); i++)
        {
            if (s.at(i) < s.at(i-1))
            {
                stop = i;
                tidy = false;
                break;
            }
        }
        if (tidy)
            std::cout << s << '\n';
        else
        {
            s = "0" + s;
            int i;
            for (i = stop; s.at(i) == s.at(i-1); i--);
            s[i]--;
            for (i++; i < s.length(); i++)
                s[i] = '9';
            for (i = 0; s.at(i) == '0'; i++);
            for (; i < s.length(); i++)
                std::cout << s.at(i);
            std::cout << '\n';
        }
    }
}
