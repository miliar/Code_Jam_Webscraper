#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int test = 1;test<=t;test++)
    {
        int R,C;
        cin >> R >> C;
        char cake[R][C];
        string temp;
        for(int row = 0;row<R;row++)
        {
            cin >> temp;
            for(int col = 0;col<C;col++)
            {
                cake[row][col] = temp[col];
            }
        }

        for(int row = 1;row < R;row++)
        {
            for(int col = 0;col<C;col++)
            {
                if(cake[row][col] == '?')
                {
                    cake[row][col] = cake[row-1][col];
                }
            }
        }

        for(int row = R-2;row >=0;row--)
        {
            for(int col = 0;col<C;col++)
            {
                if(cake[row][col] == '?')
                {
                    cake[row][col] = cake[row+1][col];
                }
            }
        }

        for(int col = 1;col <C;col++)
        {
            if(cake[0][col]=='?')
            {
                for(int row = 0;row<R;row++)
                {
                    cake[row][col] = cake[row][col-1];
                }
            }
        }

        for(int col = C-1;col >= 0;col--)
        {
            if(cake[0][col]=='?')
            {
                for(int row = 0;row<R;row++)
                {
                    cake[row][col] = cake[row][col+1];
                }
            }
        }

        cout << "Case #" << test << ":" << endl;
        for(int row = 0;row<R;row++)
        {
            for(int col = 0;col<C;col++)
            {
                cout << cake[row][col];
            }
            cout << endl;
        }


    }
}
