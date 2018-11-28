#include <iostream>
#include <vector>


unsigned long long int solve(unsigned long long int n)
{
    std::vector<unsigned long long int> digits;

    while (n > 0)
    {
        digits.push_back(n % 10);
        n /= 10;
    }

    int index = -1;

    for (int i = 0; i < digits.size() - 1; ++i)
    {
        if (digits[i] < digits[i + 1])
        {
            index = i;
        }
        else
        {
            if (index != -1 && digits[i] == digits[i + 1])
            {
                index = i;
            }
        }
    }

    if (index != -1) {
        digits[index + 1] -= 1;

        for (int j = index; j >= 0; --j)
            digits[j] = 9;
    }

    unsigned long long int p = 1;
    unsigned long long int result = 0;

    for (int i = 0; i < digits.size(); ++i)
    {
        result += p * digits[i];
        p *= 10;
    }

    return result;
}

int main(int argc, char** argv)
{
    int t;
    std::cin >> t;

    for (int i = 0; i < t; ++i)
    {
        unsigned long long int n;
        std::cin >> n;
        std::cout << "Case #" << i + 1 << ": " << solve(n) << std::endl;
    }

    return 0;
}
