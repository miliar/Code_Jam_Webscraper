#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream ifs("A-large.in");
    ofstream ofs("A-large.out");

    int T;
    ifs >> T;


    for(int i=0; i<T; i++)
    {
        unsigned long long R, C;
        ifs >> R >> C;

        string *grid = new string[R];
        for(int r=0; r<R; r++)
        {
            ifs >> grid[r];
        }

        for(int r=0; r<R; r++)
        {
            string &row = grid[r];
            for(int c=0; c<C; c++)
            {
                if(row[c] != '?')
                {
                    int left, right;
                    for(int left=c-1; left>=0; left--)
                    {
                        if(row[left] == '?')
                        {
                            row[left] = row[c];
                        }
                        else break;
                    }
                    for(int right=c+1; right<C; right--)
                    {
                        if(row[right] == '?')
                        {
                            row[right] = row[c];
                        }
                        else break;
                    }
                }
            }

            for(int i=r-1; i>=0; i--)
            {
                if(grid[i][0] == '?')
                {
                    for(int j=0; j<C; j++)
                    {
                        grid[i][j] = grid[r][j];
                    }
                }
                else break;
            }

            for(int i=r+1; i<R; i++)
            {
                bool allBrank = true;
                for(int j=0; j<C; j++)
                {
                    allBrank = allBrank && (grid[i][j] == '?');
                }

                if(allBrank)
                {
                    for(int j=0; j<C; j++)
                    {
                        grid[i][j] = grid[r][j];
                    }
                }
                else break;
            }
        }

        ofs << "Case #" << i+1 << ":" << endl;
        for(int r=0; r<R; r++)
        {
            ofs << grid[r] << endl;
        }

        delete[] grid;
    }
}
