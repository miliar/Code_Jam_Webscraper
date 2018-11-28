#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("INPUT.IN");
    ofstream fout("OUTPUT.OUT");

    int T; fin >> T;
    int Limit = T;

    string S;
    int Case = 0, K, i, j;

    while(T--)
    {
        Case++;
        int flips = 0;

        fin >> S >> K;
        int l = S.length();

        bool C[l];
        bool impossible = 0;

        for(i = 0;i < l;i++)
        {
            if(S[i] == '-') C[i] = 0;
            else C[i] = 1;
        }

        for(i = 0;i < l;i++)
        {
            if(C[i] == 0)
            {
                if(i > (l-K)) break;
                for(j = 0;j < K;j++) C[i+j] = !C[i+j];
                flips++;
            }
        }

        for(i = 0;i < l;i++)
        {
            if(C[i] == 0)
            {
                impossible = 1;
                break;
            }
        }

        if(impossible == 1) fout << "Case #" << Case << ": " << "IMPOSSIBLE";
        else fout << "Case #" << Case << ": " << flips;
        if(Case != Limit) fout << '\n';
    }
    return 0;
}
