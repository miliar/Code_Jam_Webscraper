#include<fstream>
#include<vector>
#include<string>
#define modulo 666013

using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");


string sir;
int i, n, k, j,t,st,dr,sol,x,y;

int main()
{
    fin >> t;
    for(int r = 1; r <= t; r++)
    {
        sol = 0;
        fin >> sir >> k;
        n = sir.length();
        x = 0;
        y = n - 1;
        while(x <= y)
        {
            if(sir[x] == '-')
            {
                sol++;
                for(int i = x; i <= min(x + k - 1, n-1); i++)
                {
                    if(sir[i] == '-')
                        sir[i] = '+';
                    else
                        sir[i] = '-';
                }
            }
            if(sir[y] == '-')
            {
                sol++;
                for(int i = y; i >= max(0, y - k + 1); i--)
                {
                    if(sir[i] == '-')
                        sir[i] = '+';
                    else
                        sir[i] = '-';
                }
            }
            x++;
            y--;

        }
        bool ok = true;
        for(i = 0; i < n; i++)
        {
            if(sir[i] == '-')
                ok = false;
        }
        if(ok == true)
        {
            fout << "Case #" << r <<": " << sol <<"\n";
        }
        else
        {
            fout << "Case #" << r <<": IMPOSSIBLE\n";
        }
       //fout << sir <<"\n";
        //fout << sir <<"\n";
        //fout << "Case #" << r <<": " << sol <<"\n";
    }
}
