#include <iostream>
#include <string>
#include <vector>

int solve(const std::string &s, int k)
{
    bool flip = false;
    std::vector<char> f(s.length()+1, false);

    int result = 0;
    for (int i=0;i<s.length();++i)
    {
        flip ^= f[i];
        bool needFlip = (s[i] == '-') ^ flip;
        if (needFlip)
        {
            //std::clog << "flip at " << i << std::endl;
            if (i+k >= f.size())
                return -1;
            ++result;
            flip = !flip;
            f[i+k] ^= 1;
        }
    }
    return result;
}

int main(int argc, char **argv)
{
    int T;
    std::cin >> T;
    for (int i=1;i<=T;++i)
    {
        std::string s;
        int k;
        std::cin >> s >> k;
        int n = solve(s, k);
        std::cout << "Case #" << i << ": ";
        if (n >= 0)
            std::cout << n << "\n";
        else
            std::cout << "IMPOSSIBLE\n";
    }
    return 0;
}