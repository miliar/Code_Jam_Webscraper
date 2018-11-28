#include <fstream>

using namespace std;

ifstream f ("B-large.in");
ofstream g ("B-large.out");

unsigned long long a;
int t, mx[20], i, j, cnt, cifra[20], pozajut, pozprob, caz;

int main()
{
    f >> t;

    while( t-- )
    {
        caz++;
        cnt = 0;

        f >> a;

        while( a )
        {
            cifra[++cnt] = a % 10;
            a = a / 10;
        }

        for( i = cnt; i >= 1; i--)
        {
            pozprob = 0;

            for( j = i - 1; j >= 1; j--)
                if( cifra[j] < cifra[i] )
                {
                    pozprob = j;
                    break;
                }

            if( pozprob )
            {
                pozajut = 0;

                for( j = pozprob + 1; j <= cnt; j++)
                    if( cifra[j] > cifra[i] )
                    {
                        pozajut = j;
                        break;
                    }

                if( pozajut )
                    {
                        cifra[pozajut]--;

                        for( j = pozajut - 1; j >= 1; j-- )
                            cifra[j] = 9;
                    }

                else
                {
                    cifra[i]--;

                    for( j = i - 1; j >= 1 ; j--)
                        cifra[j] = 9;
                }
            }
        }

        while(!cifra[cnt])
            cnt--;

        g << "Case #" << caz << ": ";

        for( i = cnt; i >= 1; i--)
            g << cifra[i];

        g<<"\n";
    }
}
