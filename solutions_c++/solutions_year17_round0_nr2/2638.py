#include <iostream>
#include <string>
#include <vector>

std::vector<int> doStuff(std::vector<int> s)
{
    for (int i = s.size() - 1; i > 0; --i)
    {
        if (s[i-1] > s[i])
        {
            std::fill(s.begin() + i, s.end(), 9);
            --s[i-1];
        }
    }

    if (s[0] == 0)
    {
        s.erase(s.begin());
    }
    return s;
}

int main()
{
    int nTests;
    std::cin >> nTests;

    for (int iTest = 1; iTest <= nTests; ++iTest)
    {
        std::cout << "Case #" << iTest << ": ";

        std::string s;
        std::cin >> s;
        std::vector<int> N;
        for (auto c : s)
        {
            N.push_back(c - '0');
        }

        std::vector<int> res = doStuff(N);

        for (auto n : res)
        {
            std::cout << n;
        }
        std::cout << std::endl;
    }

    return 0;
}