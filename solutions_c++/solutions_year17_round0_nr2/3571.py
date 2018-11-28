#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cstdio>

long long roundUp(long long x)
{
    std::ostringstream ss;
    ss << x;
    std::string xx = ss.str();
    char maxc = '0';
    for (char &c : xx)
    {
        maxc = std::max(maxc, c);
        c = maxc;
    }
    return atoll(xx.c_str());
}

long long search(long long a, long long b)
{
    while (a<b)
    {
        //std::clog << a << " : " << b << std::endl; 
        long long c = (a+b+1)/2;
        long long cc = roundUp(c);
        //std::clog << c << " : " << cc << std::endl;
        //std::clog << std::endl;

        if (cc > b)
            b = c-1;
        else
            a = cc;
    }
    return a;
}

int main(int argc, char **argv)
{
    int T;
    std::cin >> T;
    for (int i=1;i<=T;++i)
    {
        long long N;
        std::cin >> N;
        std::cout << "Case #" << i << ": " << search(1, N) << "\n";
   }
   return 0;
}