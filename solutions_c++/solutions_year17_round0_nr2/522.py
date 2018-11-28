#include <bits/stdc++.h>

using namespace std;

long long tests , test , val , arr[21] , M = 20 , i , p;

int main()
{

ifstream fin("input");
ofstream fout("output");

fin >> tests;
for (test = 1 ; test <= tests ; ++test)
{
    fin >> val;
    fout << "Case #" << test << ": ";

    p = M;
    memset(arr , 0 , sizeof(arr));
    while (val) arr[p] = val % 10 , p-- , val /= 10;

    //for (i = 1 ; i <= M ; ++i)
    //cerr << arr[i];
    //cerr << '\n';

    for (i = 1 ; i <= M - 1 ; ++i)
    if (arr[i] > arr[i + 1]) break;

    if (i == M)
    {
        val = 0;
        for (i = 1 ; i <= M ; ++i)
        val = val * 10 + arr[i];

        fout << val << '\n';

        continue;
    }

    p = i; arr[p]--;
    while (arr[p] < arr[p - 1]) p-- , arr[p]--;
    for (i = p + 1 ; i <= M ; ++i) arr[i] = 9;

    val = 0;
    for (i = 1 ; i <= M ; ++i)
    val = val * 10 + arr[i];

    fout << val << '\n';
}

return 0;
}
