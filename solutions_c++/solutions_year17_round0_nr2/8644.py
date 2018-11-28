#include <algorithm>
#include <iostream>
#include <string>
#include <cstdint>
#include <cstring>

bool isTidy(uint64_t N)
{
    if(N < 10)
        return true;

    uint32_t prev = N % 10;
    while(N > 1)
    {
        N = N/10;
        uint32_t curr = N % 10;

        if(curr > prev)
            return false;

//        std::cout << "prev: " << prev << " curr: " << curr << std::endl;

        prev = curr;
    }

    return true;
}

bool isTidy2(uint64_t N)
{
    if(N < 10)
        return true;

    char n[20];
    snprintf(n, sizeof(n), "%llu", N);
    for(int i = strlen(n)-1; i > 0; ++i)
    {
        if(n[i] < n[i-1])
            return false;
    }
    return true;

}

uint64_t calcTidy(uint64_t N)
{
    for(auto i = N; i >= 1; --i)
    {
        if(isTidy(i))
            return i;
    }
    return 0;
}

int main(int argc, char* argv[])
{
    int T = 0;
    std::cin >> T;

    for(int i = 0; i < T; ++i)
    {
        uint64_t N = 0;
        std::cin >> N;
        std::cout << "Case #" << i+1 << ": " << calcTidy(N) << std::endl;
    }

    return 0;
}

