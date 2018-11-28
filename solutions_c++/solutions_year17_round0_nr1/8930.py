#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

long long int N, K;
long long int C = 0;
long long int numeri[10000100];


int main()
{
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    int N;
    in >> N;
    for(int i = 0; i < N; i++)
    {
        out << "Case #" << i+1 << ": ";
        int cont = 0;
        int K;
        string S;
        in >> S >> K;
        //cout << S;
        int lunghezza = S.size();
        for(int j = 0; j < lunghezza; j++)
        {
            if(S[j] == '+')
                continue;
            if(j > lunghezza - K)
            {cont = -1; break;}
            for(int k = j; k < j + K; k++)
            {
                if(S[k] == '-')
                    S[k] = '+';
                else
                    S[k] = '-';
            }
            cont++;
        }
       if(cont != -1) out << cont << endl;
       else out << "IMPOSSIBLE" << endl;
    }
}
