#include <fstream>

using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("output");
    int t, T;

    in >> t;

    for(T = 1 ; T <= t ; T++)
    {
        int r, c, i, j, k;
        in >> r >> c;

        char grid[r+1][c+1];

        for(i = 1; i <= r ; i++)
        {
            for(j = 1 ; j <= c ; j++)
            {
                in >> grid[i][j];
            }
        }
        for(j = 1; j <= c ; j++)
        {
            for(i = 1 ; i <= r ; i++)
            {
                if(grid[i][j] == '?' and grid[i-1][j] != '?' and i>=2)
                    {
                            grid[i][j] = grid[i-1][j];
                    }
            }
        }
         for(j = 1; j <= c ; j++)
        {
            for(i = 1 ; i <= r ; i++)
            {
                if(grid[i][j] != '?')
                {
                    for(k = 1 ; k < i ; k++)
                    {
                        if(grid[k][j] == '?')
                            grid[k][j] = grid[i][j];
                    }
                    break;
                }
            }
        }
         for(i = 1; i <= r ; i++)
        {
            for(j = 1 ; j <= c ; j++)
            {
                if(grid[i][j] != '?')
                {

                    for(k = 1 ; k < j ; k++)
                    {
                        if(grid[i][k] == '?')
                        grid[i][k] = grid[i][j];

                    }
                }
            }
        }
        for(i = r; i >= 1 ; i--)
        {
            for(j = c ; j >= 1 ; j--)
            {
                if(grid[i][j] != '?')
                {
                    for(k = c ; k > j ; k--)
                    {
                        if(grid[i][k] == '?')
                            grid[i][k] = grid[i][j];
                    }

                }
            }
        }
        out << "Case #"<< T << ": "<< '\n';
        for(i = 1; i <= r ; i++)
        {
            for(j = 1 ; j <= c ; j++)
            {
                out << grid[i][j] ;
            }
            out << '\n';
        }
    }
    return 0;
}
