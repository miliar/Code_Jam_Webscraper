#include <iostream>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t=1; t<=T; t++)
    {
        int R,C;
        cin >> R >> C;
        string grid, line;
        for (int r=0; r<R; r++)
        {
            cin >> line;
            grid+=line;
        }
        int flag[26] = {0};
        for(int r=0; r<R; r++)
        {
            for(int c=0; c<C; c++)
            {
                if(grid[r*C+c]!='?' && flag[grid[r*C+c]-'A']==0)
                {
                    flag[grid[r*C+c]-'A'] = 1;
                    int j1=c, j2=c, i1=r, i2=r;
                    while(j1>0 && grid[r*C+(j1-1)]=='?') j1--;
                    while(j2<C-1 && grid[r*C+(j2+1)]=='?') j2++;
                    while(i1>0)
                    {
                        int b = 0;
                        for (int j=j1; j<=j2; j++)
                        {
                            if(grid[(i1-1)*C+j]!='?')
                            {b=1; break;}
                        }
                        if(b) break;
                        i1--;
                    }
                    while(i2<R-1)
                    {
                        int b = 0;
                        for (int j=j1; j<=j2; j++)
                        {
                            if(grid[(i2+1)*C+j]!='?')
                            {b=1; break;}
                        }
                        if(b) break;
                        i2++;
                    }
                    for(int i=i1; i<=i2; i++)
                    {
                        for(int j=j1; j<=j2; j++) grid[i*C+j] = grid[r*C+c];
                    }
                }
            }
        }

        cout << "Case #" << t << ":" << endl;
        for(int r=0; r<R; r++)
        {
            for(int c=0; c<C; c++) cout << grid[r*C+c];
            cout << endl;
        }
    }
    return 0;
}
