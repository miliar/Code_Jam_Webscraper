#include <iostream>
#include <string>

int doStuff(std::string pancakes, int flipperSize, int pancakeIndex, int nFlips)
{
    bool isAllGood = true;
    for (auto p : pancakes)
    {
        if (p == '-')
        {
            isAllGood = false;
            break;
        }
    }

    if (isAllGood)
    {
        return nFlips;
    }

    if (pancakeIndex + flipperSize > pancakes.size())
    {
        return 10000;
    }

    if (pancakeIndex > 0 && pancakes[pancakeIndex - 1] == '-')
    {
        return 10000;
    }

    int minFlips1 = doStuff(pancakes, flipperSize, pancakeIndex + 1, nFlips);

    for (int i = pancakeIndex; i < pancakeIndex + flipperSize; ++i)
    {
        if(pancakes[i] == '-')
        {
            pancakes[i] = '+';
        }
        else
        {
            pancakes[i] = '-';
        }
    }

    int minFlips2 = doStuff(pancakes, flipperSize, pancakeIndex + 1, nFlips + 1);

    return minFlips1 < minFlips2 ? minFlips1 : minFlips2;
}

int main()
{
    int nTests;
    std::cin >> nTests;

    for (int iTest = 1; iTest <= nTests; ++iTest)
    {
        std::cout << "Case #" << iTest << ": ";

        std::string pancakes;
        int k;
        std::cin >> pancakes >> k;
        int res = doStuff(pancakes, k, 0, 0);

        if (res != 10000)
        {
            std::cout << res << std::endl;
        }
        else
        {
            std::cout << "IMPOSSIBLE" << std::endl;
        }
    }

    return 0;
}