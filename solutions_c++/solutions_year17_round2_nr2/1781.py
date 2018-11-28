#include <iostream>
#include <string>
#include <vector>

std::string doStuff(int R, int Y, int B)
{
    std::string stable;

    char startWith;
    if (R > Y && R > B && R > 0)
    {
        startWith = 'R';
        R--;
    }
    else if (Y > B && Y > 0)
    {
        startWith = 'Y';
        Y--;
    }
    else if (B > 0)
    {
        startWith = 'B';
        B--;
    }

    stable += startWith;

    while (R > 0 || Y > 0 || B > 0)
    {
        bool couldPlace = false;
        //std::cout << stable << "   " << R << " " << Y << " " << B << std::endl;
        if (stable.back() == 'R')
        {
            if ((Y > B || (Y == B && startWith == 'Y')) && Y > 0)
            {
                stable += "Y";
                Y--;
                couldPlace = true;
            }
            else if (B > 0)
            {
                stable += "B";
                B--;
                couldPlace = true;
            }
        }
        else if (stable.back() == 'B')
        {
            if ((R > Y || (R == Y && startWith == 'R')) && R > 0)
            {
                stable += "R";
                R--;
                couldPlace = true;
            }
            else if (Y > 0)
            {
                stable += "Y";
                Y--;
                couldPlace = true;
            }
        }
        else if (stable.back() == 'Y')
        {
            if ((R > B || (R == B && startWith == 'R')) && R > 0)
            {
                stable += "R";
                R--;
                couldPlace = true;
            }
            else if (B > 0)
            {
                stable += "B";
                B--;
                couldPlace = true;
            }
        }
        

        if (!couldPlace)
        {
            return "IMPOSSIBLE";
        }
    }

    if (stable.front() == stable.back())
    {
        return "IMPOSSIBLE";
    }

    return stable;
}

int main()
{
    int nTests;
    std::cin >> nTests;

    for (int iTest = 1; iTest <= nTests; ++iTest)
    {
        int N, R, O, Y, G, B, V;
        std::cin >> N >> R >> O >> Y >> G >> B >> V;

        std::cout << "Case #" << iTest << ": ";
        std::cout << doStuff(R, Y, B) << std::endl;
    }

    return 0;
}