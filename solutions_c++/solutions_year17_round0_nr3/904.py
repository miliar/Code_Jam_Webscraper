#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");
//#define fin cin
//#define fout cout

typedef unsigned long long ull;

int T;
ull K, N;
ull Q, R, L;
ull ls, rs, alls;

int main()
{
    fin >> T;
    for (int z = 1; z <= T; ++z)
    {
        fin >> N >> K;
        N += 1;
        Q = 1;
        while (Q <= K)
            Q <<= 1;
        Q >>= 1;
        R = N % Q;
        L = K % Q + 1;
        if (L > R)
            alls = N / Q;
        else
            alls = N / Q + 1;
        rs = alls >> 1;
        ls = alls - rs;
        rs -= 1; ls -= 1;
        fout << "Case #" << z << ": " << ls << " " << rs << endl;
    }
    return 0;
}
