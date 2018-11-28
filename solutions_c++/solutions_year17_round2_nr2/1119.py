#include <fstream>

using namespace std;

int number[7];

int solution[1001];

int maxPos()
{
    int maxVal = -1;
    int maxPos = -1;
    for (int i = 1; i < 7; i++)
    {
        if (maxVal < number[i])
        {
            maxVal = number[i];
            maxPos = i;
        }
        else if (maxVal == number[i] && i == solution[0])
        {
            maxVal = number[i];
            maxPos = i;
        }
    }
    return maxPos;
}

int maxPosCompat(int color)
{
    int pos = -1;
    int val = -1;
    for (int i = 1; i < 7; i++)
    {
        if (val < number[i] && ((color & i) == 0))
        {
            val = number[i];
            pos = i;
        }
        else if (val < number[i] && ((color & i) == 0) && i == solution[0])
        {
            val = number[i];
            pos = i;
        }
    }
    if (val <= 0)
        return -1;
    return pos;
}

char getColor(int color)
{
    switch (color)
    {
        case 1: return 'R';
        case 2: return 'B';
        case 3: return 'V';
        case 4: return 'Y';
        case 5: return 'O';
        case 6: return 'G';
    }
    return 'B';
}

int main()
{
    ifstream f ("stable.in");
    ofstream g ("stable.out");
    int t;
    int n;
    int i;
    int color;
    f >> t;
    for (int ii = 0; ii < t; ii++)
    {
        f >> n;
        f >> number[1] >> number[5] >> number[4] >> number[6] >> number[2] >> number[3];
        solution[0] = maxPos();
        number[solution[0]]--;
        for (i = 1; i < n; i++)
        {
            color = maxPos();
            if ((color & solution[i - 1]) == 0)
            {
                solution[i] = color;
                number[color]--;
            }
            else
            {
                color = maxPosCompat(color);
                if (color == -1)
                    break;
                solution[i] = color;
                number[color]--;
            }
        }
        g << "Case #" << ii + 1 << ": ";
        if (i < n || ((solution[0] & solution[n - 1]) != 0))
        {
            g << "IMPOSSIBLE\n";
        }
        else
        {
            for (i = 0; i < n; i++)
            {
                g << getColor(solution[i]);
            }
            g << '\n';
        }
    }
    f.close();
    g.close();
    return 0;
}