#include <iostream>
#include <algorithm>
using namespace std;

typedef unsigned int uint;

void calculateLsRsForStall(bool stalls[], uint stallCount, uint Ls[], uint Rs[], uint stall)
{
    Ls[stall] = stall;
    // First the stalls on the left
    for (uint i = stall - 1; i >= 0; i--)
    {
        if (stalls[i]) // occupied
        {
            Ls[stall] = stall - i - 1;
            break;
        }
    }

    // Then on the right
    Rs[stall] = stallCount - stall - 1;
    for (uint i = stall + 1; i < stallCount; i++)
    {
        if (stalls[i])
        {
            Rs[stall] = i - stall - 1;
            break;
        }
    }
}

uint enterPerson(bool stalls[], uint stallCount, uint *maxStall, uint *minStall)
{
    uint *Ls, *Rs;

    Ls = (uint*)malloc(sizeof(uint) * stallCount);
    Rs = (uint*)malloc(sizeof(uint) * stallCount);
    memset(Ls, 0, sizeof(uint) * stallCount);
    memset(Rs, 0, sizeof(uint) * stallCount);

    for (uint i = 0; i < stallCount; i++)
        calculateLsRsForStall(stalls, stallCount, Ls, Rs, i);

    bool hasValue = false,
         tie = false;
    uint bestPos = 0, bestValue = 0;
    
    uint stallChosen;
    uint bestPosMax = 0, bestValueMax = 0;

    for (uint i = 0; i < stallCount; i++)
    {
        if (stalls[i]) continue;
        uint val = min(Ls[i], Rs[i]);
        uint valMax = max(Ls[i], Rs[i]);

        if (val > bestValue || !hasValue)
        {
            bestValue = val;
            bestPos = i;
        }
        else if (val == bestValue)
        {
            tie = true;
        }

        if (valMax > bestValueMax || !hasValue)
        {
            bestValueMax = valMax;
            bestPosMax = i;
        }

        hasValue = true;
    }

    hasValue = false;
    if (tie)
    {
        bestValueMax = 0;
        bestPosMax = 0;

        for (uint i = 0; i < stallCount; i++)
        {
            if (stalls[i]) continue;
            uint valMax = max(Ls[i], Rs[i]);
            uint val = min(Ls[i], Rs[i]);

            if (val == bestValue && (valMax > bestValueMax || !hasValue))
            {
                bestValueMax = valMax;
                bestPosMax = i;
                hasValue = true;
            }
        }
    }

    if (tie)
        stallChosen = bestPosMax;
    else
        stallChosen = bestPos;

    stalls[stallChosen] = true;

    *maxStall = max(Ls[stallChosen], Rs[stallChosen]);
    *minStall = min(Ls[stallChosen], Rs[stallChosen]);

    free(Ls);
    free(Rs);

    return stallChosen;
}

void main()
{
    int numberOfCases;

    cin >> numberOfCases;

    for (int i = 1; i <= numberOfCases; i++)
    {
        uint numberOfStalls,
                  numberOfPeople;

        cin >> numberOfStalls >> numberOfPeople;

        // Stalls
        // [x][ ][y][ ][x]

        uint lastMin, lastMax;
        bool *stalls = (bool*)malloc(numberOfStalls);
        memset(stalls, 0, numberOfStalls);

        for (uint i = 0; i < numberOfPeople; i++)
        {
            enterPerson(stalls, numberOfStalls, &lastMax, &lastMin);
        }

        cout << "Case #" << i << ": " << lastMax << " " << lastMin << "\n";

        free(stalls);
    }
}