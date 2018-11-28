#include <bits/stdc++.h>

using namespace std;

int n;

int main()
{
    ifstream input;
    ofstream output;
    input.open("A-large.in");
    output.open("A-large.out");
    input >> n;
    for (int test = 0; test < n; test++)
    {
        string pancakes;
        int width, flips = 0;
        input >> pancakes >> width;
        int pan[pancakes.length()];
        for (int i = 0; i < pancakes.length(); i++)
        {
            pan[i] = (pancakes[i] == '+' ? 1 : 0);
        }
        for (int i = 0; i < pancakes.length() - width + 1; i++)
        {
            if (pan[i] == 0)
            {
                for (int j = 0; j < width; j++)
                {
                    pan[i + j] = 1 - pan[i + j];
                }
                flips++;
            }
        }
        bool possible = true;
        for (int i = pancakes.length() - width + 1; i < pancakes.length(); i++)
        {
            if (pan[i] == 0)
            {
                possible = false;
                break;
            }
        }
        output << "Case #" << (test + 1) << ": ";
        if (possible)
        {
            output << flips << endl;
        }
        else
        {
            output << "IMPOSSIBLE" << endl;
        }
    }
}
