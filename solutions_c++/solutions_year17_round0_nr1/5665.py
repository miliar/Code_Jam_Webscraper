#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

#define HAPPY '+'
#define SAD '-'
#define MAX_TRIES 1000

void flip(string &pancakes, int pos, int panSize)
{    
    for (int i = pos; i < min(panSize + pos, (signed int) pancakes.length()); i++)
    {
        pancakes[i] = pancakes[i] == HAPPY
            ? SAD : HAPPY;
    }
}

bool solved(string &pancakes)
{
    for (int i = 0; i < pancakes.length(); i++)
    {
        if (pancakes[i] != HAPPY)
            return false;
    }

    return true;
}

int simpleSolveStep(string &pancakes, int panSize)
{
    // First try to find the simple flips
    int combo = 0,
        len = pancakes.length();
    for (int i = 0; i < len; i++)
    {
        if (pancakes[i] == HAPPY)
            combo = 0;
        else combo++;

        if (combo == panSize)
            return i - panSize + 1;
    }

    // Then try flipping one beginning from the left.
    for (int i = 0; i < len - panSize; i++)
    {
        if (pancakes[i] == SAD)        
            return i;
    }

    // That fails, maybe the pancake is hidden on the right?
    for (int i = len - 1; i >= len - panSize; i--)
    {
        if (pancakes[i] == SAD)
            return len - panSize;
    }

    return -1;
}

int simpleSolve(string pancakes, int panSize)
{
    int pos;
    int tries = 0;
    while ((pos = simpleSolveStep(pancakes, panSize)) != -1)
    {
        tries++;
        flip(pancakes, pos, panSize);

        if (tries > MAX_TRIES) break;
    }

    return tries;
}

int complexSolveStep(string &pancakes, int panSize, int clusterStart, int clusterSize)
{
    // Left side of the cluster
    for (int i = 0; i < min(clusterStart, (signed int) pancakes.length() - panSize); i++)
    {
        if (pancakes[i] == SAD)
            return i;
    }

    // Right side of cluster
    for (int i = clusterStart + clusterSize; i < pancakes.length(); i++)
    {
        if (pancakes[i] == SAD)
            return min(i, (signed int) pancakes.length() - panSize);
    }

    // Finally flip the cluster itself.
    return simpleSolveStep(pancakes, panSize);
}

int complexSolve(string pancakes, int panSize)
{
    // We want to bunch all -'s to then solve them all in one go

    // Find a pancake cluster

    int combo = 0,
        comboStart = -1,
        maxCombo = 0,
        maxComboStart = 0;
    for (int i = 0; i < pancakes.length(); i++)
    {
        if (pancakes[i] == HAPPY)
        {
            if (combo > maxCombo)
            {
                combo = maxCombo;
                maxComboStart = comboStart;
            }

            comboStart = -1;
            combo = 0;
        }
        else
        {
            if (comboStart == -1) comboStart = i;
            combo++;
        }
    }

    if (combo > maxCombo)
    {
        combo = maxCombo;
        maxComboStart = comboStart;
    }

    // Now move all other 
    int tries = 0;

    while (!solved(pancakes))
    {
        tries++;
        int pos = complexSolveStep(pancakes, panSize, maxComboStart, maxCombo);

        flip(pancakes, pos, panSize);

        if (tries > MAX_TRIES)
            break;
    }

    return tries;
}

bool isImpossible(string &pancakes, int panSize)
{
    // It's impossible if any pan combination flips a pair of opposite pancakes.
    // So they must be somewhere in the middle.
    // That only can happen if pancakeLen - panSize <= panSize - 2
    int pancakeLen = pancakes.length();
    if (pancakeLen - panSize <= panSize - 2)
    {
        for (int i = pancakeLen - panSize; i < panSize; i++)
        {
            if (i != pancakeLen - panSize && pancakes[i] != pancakes[i - 1])
                return true;
        }
    }
    return false;
}

void main()
{
    int numberOfCases;

    cin >> numberOfCases;

    for (int i = 1; i <= numberOfCases; i++)
    {
        string pancakes;
        int panSize;
        cin >> pancakes >> panSize;

        int tries = 0;

        if (isImpossible(pancakes, panSize))
        {
            cout << "Case #" << i << ": IMPOSSIBLE\n";
            continue;
        }

        tries = min(simpleSolve(pancakes, panSize), complexSolve(pancakes, panSize));

        if (tries > MAX_TRIES)
            cout << "Case #" << i << ": IMPOSSIBLE\n";
        else
            cout << "Case #" << i << ": " << tries << "\n";
    }
}