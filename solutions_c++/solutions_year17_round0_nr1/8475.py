#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

long long flip(long long, int, int);

int T, K, S;
string str;
int pank[1000];
long long INF = (1ULL << 63) - 1;

int main()
{
    ifstream in("input.in");
    ofstream out("output.txt");
    in >> T;
    for(int c = 0;c < T;++c)
    {
        in >> str;
        in >> K;
        S = str.length();
        int chk = 0;
        for(int i = 0;i < S;++i)
        {
            if(str[i] == '+')
                pank[i] = 1;
            else
                pank[i] = 0;
            chk += pank[i];
        }
        long long ans = flip(0, 0, chk);
        if(ans == INF)
            out << "Case #" << c + 1 << ": IMPOSSIBLE" << endl;
        else
            out << "Case #" << c + 1 << ": " << ans << endl;
    }

    return 0;
}

long long flip(long long n, int s, int chk)
{
    if(chk == S)
        return n;
    long long minF = INF;
    for(int i = s;i <= S - K;++i)
    {
        for(int j = 0;j < K;++j)
        {
            chk -= pank[i + j];
            pank[i + j] = !pank[i + j];
            chk += pank[i + j];
        }
        minF = min(minF, flip(n + 1, i + 1, chk));
        for(int j = 0;j < K;++j)
        {
            chk -= pank[i + j];
            pank[i + j] = !pank[i + j];
            chk += pank[i + j];
        }
    }
    return minF;
}
