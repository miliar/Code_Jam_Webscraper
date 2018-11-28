#include <bits/stdc++.h>

using namespace std;

int main()
{

    int tcc; cin >> tcc;
    for(int tc = 0; tc < tcc; tc++)
    {
        int r, c;
        cin >> r >> c;
        char  world[r][c];
        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++)
            {
                cin >> world[i][j];
            }
        }


        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++)
            {
                if(world[i][j] != '?')
                {
                    for(int k = i-1; k>=0; k--)
                    {
                        if(world[k][j] != '?') break;
                        world[k][j] = world[i][j];
                    }
                    for(int k = i+1; k<r; k++)
                    {
                        if(world[k][j] != '?') break;
                        world[k][j] = world[i][j];
                    }
                }
            }


        }

        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++)
            {
                if(world[i][j] != '?')
                {
                    for(int k = j-1; k>=0; k--)
                    {
                        if(world[i][k] != '?') break;
                        world[i][k] = world[i][j];
                    }
                    for(int k = j+1; k < c; k++)
                    {
                        if(world[i][k] != '?') break;
                        world[i][k] = world[i][j];
                    }
                }
            }


        }

        cout << "Case #" << tc + 1<< ": " << endl;
        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++)
            {
                cout << world[i][j];
            }
            cout << endl;
        }

    }



    return 0;
}
