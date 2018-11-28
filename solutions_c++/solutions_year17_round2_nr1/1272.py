#include<bits/stdc++.h>
int K[1010];
int S[1010];
using namespace std;
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for(int i=1 ; i<=T ; i++)
    {
        fout << "Case #" << i << ": ";
        int D,N;
        fin >> D >> N;
        double M=0;
        for(int j=0 ; j<N ; j++)
        {
            fin >> K[i] >> S[i];
            M=max(M,((double)(D-K[i]))/S[i]) ;
        }
        fout << fixed << setprecision(10) << D/M << endl;
    }
}
