#include <bits/stdc++.h>

using namespace std;

const int nmax = 59;

int T , tests , N , K , i , j;
double d , x , U , p[nmax] , ret;

int main()
{

ifstream fin("input");
ofstream fout("output");

fin >> tests;
for (T = 1 ; T <= tests; ++T)
{
    fin >> N >> K;
    fin >> U;

    for (i = 1 ; i <= N ; ++i)
    fin >> p[i];
    p[N + 1] = 1.0;

    sort(p + 1 , p + N + 1);
    for (i = 2 ; i <= N + 1 ; ++i)
    {
        d = p[i] - p[i - 1];

        if (d * (i - 1) <= U)
        {
            U -= d * (i - 1);

            for (j = 1 ; j <= i - 1 ; ++j)
            p[j] += d;
        }
        else
        {
            x = U / (i - 1) , U = 0.0;

            for (j = 1 ; j <= i - 1 ; ++j)
            p[j] += x;
            break;
        }
    }

    ret = 1.0;
    for (i = 1 ; i <= N ; ++i)
    ret *= p[i];

    fout << "Case #" << T << ": " << fixed << setprecision(10) << ret << '\n';
}

return 0;
}
