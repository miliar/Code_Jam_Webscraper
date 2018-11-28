#include <string>
#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned long long UINT64;

UINT64 DigitCount(UINT64 N)
{
    UINT64 result = 0;
    while (N > 0)
    {
        result++;
        N = N / 10;
    }
    return result;
}

bool CheckDigit(UINT64 N, UINT64 start, UINT64 &last)
{
    N = N / start; last = N % 10;
    UINT64 last1 = last;
    N = N / 10;
    while (N > 0)
    {
        UINT64 next = N % 10;
        if (next > last1)
        {
            return false;
        }
        last1 = N % 10;
        N = N / 10;
    }
    return true;
}


int main()
{
    ifstream fin("C:\\Compete\\FB2016\\B-large.in");

    ofstream fout("C:\\Compete\\FB2016\\output.txt");

    int T;  fin >> T;
    for (int i = 0; i < T; i++)
    {
        unsigned long long N;
        fin >> N;

        unsigned long long mul = 1;
        UINT64 count = DigitCount(N);

        for (UINT64 j = count; j > 1; j--)
        {
            UINT64 last = 0;
            if (!CheckDigit(N, mul, last))
            {
                N = N - mul * (last + 1);
            }
            mul = mul * 10;
        }


       
       fout << "Case #" << i + 1 << ": " << N << endl;
       

    }
    return 0;
}