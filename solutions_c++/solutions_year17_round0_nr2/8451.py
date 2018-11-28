#include <iostream>
#include <list>

using namespace std;

void PrintResult(uint64_t i, uint64_t n)
{
    std::cout << "Case #" + to_string(i) << ": ";
    std::cout << n;
    std::cout << std::endl;
}

std::list<uint8_t> ToList(uint64_t n)
{
    std::list<uint8_t> result;
    while (n)
    {
        result.push_front(n % 10);
        n = n / 10;
    }
    return result;
}

uint64_t ToNum(const std::list<uint8_t>& n)
{
    uint64_t result = 0;
    for (uint8_t c: n)
    {
        result *= 10ULL;
        result += c;
    }
    return result;
}

uint64_t TidyUp(uint64_t n)
{
    std::list<uint8_t> ciphers = ToList(n);
    // find the first untidy cipher, zero it and the remaining ciphers
    auto it = ciphers.begin();
    uint8_t previousCipher = *it;
    bool zeroing = false;
    for (++it; it != ciphers.end(); ++it)
    {
        if (previousCipher > *it)
            zeroing = true;
        previousCipher = *it;
        if (zeroing)
            *it = 0;
    }
    if (zeroing)
    {
        // the number was untidy, let's decrease it a bit
        return TidyUp(ToNum(ciphers) - 1);
    }
    else
    {
        return ToNum(ciphers);
    }
}

void SolveTestCaseI(uint64_t i, uint64_t n)
{
    uint64_t result = TidyUp(n);
    PrintResult(i, result);
}

int main()
{
    uint64_t t;
    cin >> t;
    for (uint64_t i = 1; i <= t; ++i)
    {
        uint64_t n;
        std::cin >> n;
        SolveTestCaseI(i, n);
    }
    return 0;
}
