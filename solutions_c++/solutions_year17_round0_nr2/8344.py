#include <iostream>
#include <fstream>

using namespace std;

unsigned long long test_number(unsigned long long N)
{
    if(N < 10) return 1;
    unsigned char NR, NL;
    unsigned long long D = 1, D2 = 1;
    for(NR = N % 10; N > 9; NR = NL)
    {
        N /= 10;
        D2 *= 10;
        NL = N % 10;
        if(NL > NR) D = D2;
    }
    return D;
}

unsigned long long tidy_number(unsigned long long N)
{
    unsigned long long S = N, D;
    while(S > 9)
    {
        D = test_number(S);
        if(D == 1)
        {
            return S;
        }
        S -= S%D + 1;
    }
    return S;
}

int main()
{
    ifstream file_input("B-large.in", ios::in);
    ofstream file_output("B-large(answer).in", ios::trunc | ios::out);
    if(file_input && file_output)
    {
        unsigned short T, t;
        unsigned long long N;

        file_input >> T;
        for(t = 1; t <= T; ++t)
        {
            file_input >> N;

            cout << "Case #" << t << ": " << N << endl;

            file_output << "Case #" << t << ": " << tidy_number(N) << "\n";
        }
        file_input.close();
        file_output.close();
    }
    else
        cerr << "Error : Cannot open the file(s) !" << endl;
    return 0;
}
