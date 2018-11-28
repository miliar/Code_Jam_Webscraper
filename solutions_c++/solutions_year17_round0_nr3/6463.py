#include <fstream>

using namespace std;

ifstream f ("C-small-1-attempt0.in");
ofstream g ("C-small-1-attempt0.out");

struct distanta
{
    int dr;
    int st;
}dist[1001], mn;

int i, j, indice, t, n, k, celmaidr, celmaist, cabina[1001], x;

void gasestecabina()
{
    mn.dr = mn.st = indice = -1;

    for(j = 1; j <= n; j++)
    {
        if( min( dist[j].dr, dist[j].st ) > min( mn.dr, mn.st) )
        {
            mn = dist[j];
            indice = j;
        }

        else if( min( dist[j].dr, dist[j].st ) == min( mn.dr, mn.st) && max( dist[j].dr, dist[j].st ) > max( mn.dr, mn.st) )
        {
            mn = dist[j];
            indice = j;
        }
    }
}

void modificadistante()
{
    celmaidr = indice - 1;

    for( j = celmaidr; j >= 0; j--)
    {
        if( cabina[j] == 1 )
        {
            celmaist = j + 1;
            break;
        }
    }

    for( j = celmaist; j <= celmaidr; j++ )
    {
        if( !cabina[j] )
        {
            dist[j].st = j - celmaist;
            dist[j].dr = celmaidr - j;
        }
    }

    celmaist = indice + 1;

    for( j = celmaist; j <= n + 1; j++ )
    {
        if( cabina[j] )
        {
            celmaidr = j - 1;
            break;
        }
    }

    for( j = celmaist; j <= celmaidr; j++ )
    {
        if( !cabina[j] )
        {
            dist[j].st = j - celmaist;
            dist[j].dr = celmaidr - j;
        }
    }
}

int main()
{
    f >> t;

    for(int x = 1; x <= t; x++ )
    {
        for( i = 1; i <= 1001; i++)
            cabina[i] = dist[i].st = dist[i].dr = 0;

        f >> n >> k;

        cabina[0] = cabina[n+1] = 1;

        for( i = 1; i <= n; i++)
        {
            dist[i].st = i - 1;
            dist[i].dr = n - i;
        }

        for( i = 1; i <= k - 1; i++ )
        {
            gasestecabina();
            cabina[indice] = 1;
            dist[indice].st = dist[indice].dr = -1;
            modificadistante();

            /*for( j = 1; j <= n; j++)
                g << dist[j].st << " " << dist[j].dr << "\n";

            g<<"\n\n\n";
            */
        }

        gasestecabina();

        g << "Case #" << x << ": " << max( mn.st, mn.dr ) << " " << min( mn.st, mn.dr ) << "\n";
    }
}
