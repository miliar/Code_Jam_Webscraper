#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>
using namespace std;

void SolveTest(ifstream& in, ofstream& out);

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int T;
    in >> T;

    for (int t = 0; t < T; ++t)
    {
        out << "Case #" << t + 1 << ": ";
        SolveTest(in, out);
    }

    return 0;
}

enum Color
{
    R,
    O,
    Y,
    G,
    B,
    V,
    Count,
    Failed
};

Color MaxColor(vector<int>& colors)
{
    Color maxColor = R;

    int number = 0;
    for (int i = 0; i < Color::Count; ++i)
    {
        if (colors[i] > number)
        {
            number = colors[i];
            maxColor = (Color)i;
        }
    }

    return maxColor;
}

Color MaxColorBut(vector<int>& colors, Color butColor, Color firstColor)
{
    Color maxColor = (R == butColor ? B : R);

    int number = 0;
    for (int i = 0; i < Color::Count; ++i)
    {
        if (i == butColor)
        {
            continue;
        }

        if (i == firstColor)
        {
            if (colors[i] >= number)
            {
                number = colors[i];
                maxColor = (Color)i;
            }
        }
        else
        {
            if (colors[i] > number)
            {
                number = colors[i];
                maxColor = (Color)i;
            }
        }
    }

    return number > 0 ? maxColor : Failed;
}

void SolveTest(ifstream& in, ofstream& out)
{
    //  N, R, O, Y, G, B, and V.
    int N;
    vector<int> colors(Color::Count);
    in >> N >> colors[R] >> colors[O] >> colors[Y] >> colors[G] >> colors[B] >> colors[V];

    bool isReallyPossible = true;
    if (colors[R] > colors[Y] + colors[B])
    {
        isReallyPossible = false;
    }
    if (colors[Y] > colors[R] + colors[B])
    {
        isReallyPossible = false;
    }
    if (colors[B] > colors[Y] + colors[R])
    {
        isReallyPossible = false;
    }

    string stable(N, '?');
    bool possible = true;
    Color firstColor;
    // R Y B case
    for (int i = 0; i < N; ++i)
    {
        if (i == 0)
        {
            Color color = MaxColor(colors);
            colors[color]--;
            stable[i] = color;
            firstColor = color;
        }
        else
        {
            Color color = MaxColorBut(colors, (Color)stable[i - 1], firstColor);
            if (color == Failed)
            {
                possible = false;
                break;
            }
            colors[color]--;
            stable[i] = color;
        }
    }

    if (possible)
    {
        if (stable[0] == stable[stable.size() - 1])
        {
            possible = false;
        }
    }

    //if (possible)
    {
        for (int i = 0; i < stable.size(); ++i)
        {
            switch (stable[i])
            {
            case R:
                stable[i] = 'R';
                break;
            case O:
                stable[i] = 'O';
                break;
            case Y:
                stable[i] = 'Y';
                break;
            case B:
                stable[i] = 'B';
                break;
            case G:
                stable[i] = 'G';
                break;
            case V:
                stable[i] = 'V';
                break;
            }
        }
    }

    if (possible != isReallyPossible)
    {
        int a = 28;
    }

    if (possible)
    {
        out << stable << endl;
    }
    else
    {
        out << "IMPOSSIBLE" << endl;
    }
}