#include <iostream>
#include <ctype.h>
#include <stdio.h>

using namespace std;

void calc(int r, int c)
{
    int i, j;

    char cake[30][30];

    for (i=0 ; i<r ; i++)
    {
        for (j=0 ; j<c ; j++)
        {
            do{
                cake[i][j] = getchar();
            } while (cake[i][j]=='\r' || cake[i][j]=='\n');

        }
    }

    for (i=0 ; i<r ; i++)
    {
        for (j=0 ; j<c ; j++) // L>R
        {
            if (cake[i][j] == '?')
            {
                if (j>0)
                    cake[i][j] = cake[i][j-1];
            }
        }
        for (j=(c-1) ; j>=0 ; j--) // R>L
        {
            if (cake[i][j] == '?')
            {
                if (j<(c-1))
                    cake[i][j] = cake[i][j+1];
            }
        }
    }

    for (i=0 ; i<r ; i++) // U > D
    {
        for (j=0 ; j<c ; j++)
        {
            if (cake[i][j] == '?')
            {
                if (i>0)
                    cake[i][j] = cake[i-1][j];
            }
        }
    }

    for (i=(r-1) ; i>=0 ; i--) // D>U
    {
        for (j=0 ; j<c ; j++)
        {
            if (cake[i][j] == '?')
            {
                if (i<(r-1))
                    cake[i][j] = cake[i+1][j];
            }
        }
    }

    for (i=0 ; i<r ; i++)
    {
        for (j=0 ; j<c ; j++)
        {
            cout << cake[i][j];
        }
        cout << endl;
    }
}

int main()
{
    int T;
    cin >> T;
    int x;
    int r, c;

    for (x=0 ; x<T ; x++)
    {
        cin >> r;
        cin >> c;
        cout << "Case #" << x+1 <<":" << endl;
        calc(r, c);
    }
    return 0;
}
