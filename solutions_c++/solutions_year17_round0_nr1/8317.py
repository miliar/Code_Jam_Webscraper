#include <fstream>
#include <cstring>

using namespace std;

int t, k, sze, i, j, rez, cnt;
char sir[100];

ifstream f("A-small-attempt0.in");
ofstream g("A-small-attempt0.out");

bool check()
{
    for( i = 0; i <= sze; i++)
        if(sir[i] == '-')
            return 0;

    return 1;
}

int main()
{
    f >> t;

    while(t--)
    {
        memset(sir, 0, 100);
        rez = 0;
        cnt ++;

        f >> sir >> k;

        sze = strlen(sir) - 1;

        for( i = 0; i <= sze - k + 1; i++ )
        {
            if(sir[i] == '-')
            {
                for( j = i + k - 1; j >= i; j--)
                    {
                        if(sir[j] == '-')
                            sir[j] = '+';

                        else if(sir[j] == '+')
                            sir[j] = '-';
                    }

                rez++;
            }
        }

        g << "Case #" << cnt <<": ";

        if(check())
            g << rez << "\n";
        else
            g << "IMPOSSIBLE\n";
    }
}
