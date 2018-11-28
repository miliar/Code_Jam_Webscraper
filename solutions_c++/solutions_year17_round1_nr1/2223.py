#include <fstream>
#include <iostream>

using namespace std;

void fix(char a[25][25], int row, int col)
{
    if (a[row][col] != '?') return;
    int i = row, j;
    if (col == 0)
    {
        for (j = 0; a[i][j] == '?'; ++j);
        col = j;
        for (j = 0; j < col; ++j)
            a[i][j] = a[row][col];
    }
    else
        a[row][col] = a[row][col - 1];
}

void fixcol(char a[25][25], int row, int col)
{
    if (a[row][col] != '?') return;
    int i, j = col;
    if (row == 0)
    {
        for (i = 0; a[i][j] == '?'; ++i);
        row = i;
        for (i = 0; i < row; ++i)
            a[i][j] = a[row][col];
    }
    else
        a[row][col] = a[row - 1][col];
}

int main()
{
    ifstream fin;
    fin.open("A-large.in", ios::in);
    ofstream fout;
    fout.open("A-large_output.txt", ios::out);
    int t;
    fin >> t;
    for (int o = 1; o <= t; ++o)
    {
        fout << "Case #" << o << ": " << endl;
        int r, c;
        fin >> r >> c;
        char a[25][25] = {};
        bool check[25];
        for (int i = 0; i < r; ++i)
            check[i] = true;
        string s;
        for (int i = 0; i < r; ++i)
        {
            fin >> s;
            for (int j = 0; j < c; ++j)
                a[i][j] = s[j];
        }
        for (int i = 0; i < r; ++i)
        {
            int counter = 0;
            for (int j = 0; j < c; ++j)
            {
                if (a[i][j] == '?')
                    ++counter;
            }
            if (counter == c)
                check[i] = false;
        }
        for (int i = 0; i < r; ++i)
        {
            if (check[i] == false) continue;
            for (int j = 0; j < c; ++j)
                fix(a, i, j);
        }
        for (int j = 0; j < c; ++j)
        {
            for (int i = 0; i < r; ++i)
                fixcol(a, i, j);
        }
        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
                fout << a[i][j];
            fout << endl;
        }
    }
}
