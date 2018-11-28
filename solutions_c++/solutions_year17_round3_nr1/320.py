#include <bits/stdc++.h>

using namespace std;

const int nmax = 1009;
const double pi = 3.14159265359;

long long tests , T , N , i , K , j , act , answer;
long long aux[nmax];
pair < long long , long long > p[nmax];

int main()
{

ifstream fin("input");
ofstream fout("output");

fin >> tests;
for (T = 1 ; T <= tests ; ++T)
{
    fout << "Case #" << T << ": ";
    fin >> N >> K;
    for (i = 1 ; i <= N ; ++i)
    fin >> p[i].first >> p[i].second;

    sort(p + 1 , p + N + 1);
    reverse(p + 1 , p + N + 1);

    answer = 0;
    for (i = 1 ; i <= N - K + 1 ; ++i)
    {
        act = p[i].first * p[i].first + 2 * p[i].first * p[i].second;
        for (j = i + 1 ; j <= N ; ++j)
        aux[j - i] = 2 * p[j].first * p[j].second;
        sort(aux + 1 , aux + N - i + 1);
        reverse(aux + 1 , aux + N - i + 1);
        for (j = 1 ; j <= K - 1 ; ++j)
        act += aux[j];

        answer = max(act , answer);
    }

    fout << fixed << setprecision(7) << pi * answer << '\n';
}


return 0;
}
