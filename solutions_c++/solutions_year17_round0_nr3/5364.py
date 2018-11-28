#include <iostream>
#include <fstream>

using namespace std;
typedef long long ll;

ifstream fin ("A.in");
ofstream fout ("A.out");

void run()
{
    ll N, K;
    fin >> N >> K;

    ll cpow = 1;
    while (cpow * 2 <= K)
        cpow *= 2;

    ll nleft = N - cpow + 1;
    ll tot = nleft / cpow;
    if (K - cpow < nleft % cpow)
        tot++;
    fout << tot / 2 << " " << (tot - 1) / 2;
}

int main()
{
    int T; fin >> T;
    for (int i = 1; i <= T; i++)
    {
        fout << "Case #" << i << ": ";
        run();
        fout << "\n";
    }
}