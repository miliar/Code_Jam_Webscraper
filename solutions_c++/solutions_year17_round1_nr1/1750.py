#include <bits/stdc++.h>

using namespace std;

int n;

void fill(char cake[25][25], int maxR, int maxC, int r, int c)
{
    int mnC = c;
    int mxC = c;
    int mnR = r;
    int mxR = r;

    while (mnC >= 1 && cake[r][mnC - 1] == '?')
    {
        mnC--;
        cake[r][mnC] = cake[r][c];
    }
    while (mxC < maxC - 1 && cake[r][mxC + 1] == '?')
    {
        mxC++;
        cake[r][mxC] = cake[r][c];
    }
    while (mnR >= 1)
    {
        bool valid = true;
        for (int i = mnC; i <= mxC; i++)
        {
            if (cake[mnR - 1][i] != '?')
            {
                valid = false;
                break;
            }
        }
        if (!valid) break;
        mnR--;
        for (int i = mnC; i <= mxC; i++)
        {
            cake[mnR][i] = cake[r][c];
        }
    }
    while (mxR < maxR - 1)
    {
        bool valid = true;
        for (int i = mnC; i <= mxC; i++)
        {
            if (cake[mxR + 1][i] != '?')
            {
                valid = false;
                break;
            }
        }
        if (!valid) break;
        mxR++;
        for (int i = mnC; i <= mxC; i++)
        {
            cake[mxR][i] = cake[r][c];
        }
    }
}

int main()
{
    ifstream input;
    ofstream output;
    input.open("data/A-large.in");
    output.open("data/A-large.out");
    input >> n;
    for (int test = 0; test < n; test++)
    {
        int r,c;
        input >> r >> c;
        char cake[25][25];
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                input >> cake[i][j];
            }
        }
        set<char> done;
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                if (cake[i][j] != '?' && done.find(cake[i][j]) == done.end())
                {
                    fill(cake, r, c, i, j);
                    done.insert(cake[i][j]);
                }
            }
        }
        output << "Case #" << (test + 1) << ":" << endl;
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                output << cake[i][j];
            }
            output << endl;
        }
    }
}
