#include <fstream>

using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    int t;
    in>>t;
    for (int q =0 ;q<t; q++)
    {
        out << "Case #" << q+1 << ":\n";
        int r, c;
        in >> r >> c;
        char ** grid = new char * [r];
        int * nrow = new int[r];
        for (int i = 0; i<r; i++)
            nrow[i] = 0;
        for (int i = 0; i<r; i++)
        {
            grid[i] = new char[c];
            for (int j = 0; j<c; j++)
            {
                char ch;
                in >> ch;
                grid[i][j] = ch;
                nrow[i] += (ch!='?');
            }
        }
        for (int i = 0; i<r; i++)
        {
            if (nrow[i]==0 && nrow[i] ==c)
            {
                continue;
            }
            else
            {
                for (int j = 0; j<c; j++)
                {
                    if (grid[i][j]=='?')
                        continue;
                    else
                    {
                        char cur = grid[i][j];
                        int l = j - 1, r = j + 1;
                        while (l >= 0 && grid[i][l]=='?')
                        {
                            grid[i][l] = cur;
                            l--;
                        }
                        while (r < c && grid[i][r]=='?')
                        {
                            grid[i][r] = cur;
                            r++;
                        }
                    }
                }
            }
        }
        bool prev = false;
        for (int i = 0; i<r; i++)
        {
            if (nrow[i] != 0)
            {
                prev = true;
                continue;
            }
            else
            {
                if (prev)
                {
                    for (int j = 0; j<c; j++)
                        grid[i][j] = grid[i-1][j];
                }
                else
                {
                    int k = i+1;
                    while (k<r && nrow[k]==0)
                        k++;
                    for (int j = 0; j<c; j++)
                        grid[i][j] = grid[k][j];
                }
            }
        }
        for (int i = 0; i<r; i++)
        {

            for (int j = 0; j<c; j++)
                out << grid[i][j];
            out << '\n';
        }
    }
    in.close();
    out.close();
    return 0;
}
