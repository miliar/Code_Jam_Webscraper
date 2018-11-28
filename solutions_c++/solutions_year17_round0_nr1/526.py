#include <bits/stdc++.h>

using namespace std;

string arr;
int k , tests , j , i , t , moves;

int main()
{

ifstream fin("input");
ofstream fout("output");

fin >> tests;
for (t = 1 ; t <= tests ; ++t)
{
    fin >> arr >> k;
    moves = 0;
    fout << "Case #" << t << ": ";

    for (i = 0 ; i < arr.size() ; ++i)
    if (arr[i] == '-')
    {
        if (i + k - 1 < arr.size())
        {
            for (j = i ; j <= i + k - 1 ; ++j)
            {
                if (arr[j] == '-') arr[j] = '+';
                else arr[j] = '-';
            }
            moves++;
        }
        else break;
    }

    if (i == arr.size()) fout << moves << '\n';
    else fout << "IMPOSSIBLE" << '\n';
}

return 0;
}
