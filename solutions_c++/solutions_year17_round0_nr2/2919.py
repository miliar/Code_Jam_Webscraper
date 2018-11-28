#include <fstream>
#include <algorithm>
#include <vector>
#include <assert.h>

#include <boost/range/algorithm/reverse.hpp>

size_t process(size_t N)
{
    std::vector<std::uint8_t> digits;
    while (N)
    {
        digits.push_back(N % 10);
        N /= 10;
    }

    boost::reverse(digits);

    for (size_t l = 0; l + 1 < digits.size(); ++l)
    {
        if (digits[l] > digits[l + 1])
        {
           while (l && digits[l - 1] == digits[l])
               --l;

           digits[l]--;
           for (l++; l != digits.size(); ++l)
               digits[l] = 9;

           break;
        }
    }

    size_t res = 0;
    for (auto d: digits)
        res = res * 10 + d;

    return res;
}

int main(int argc, char * argv[])
{
    std::ifstream in("in_b.txt");
    std::ofstream out("out_b.txt");

    size_t T;
    in >> T;
    for (int i = 0; i != T; ++i)
    {
        size_t N;
        in >> N;

        out << "Case #" << i + 1 << ": " << process(N) << std::endl;
    }
}
