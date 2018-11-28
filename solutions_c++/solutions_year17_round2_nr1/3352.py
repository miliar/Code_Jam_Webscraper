#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <cmath>

using namespace std;

static long long int testCase, D, N, K, S, minK, minS;
ifstream fin("A-large.in");
ofstream fout("output.txt");

int main(void)
{
    fin >> testCase;
    
    for (int i = 0; i < testCase; i++)
    {
        minK = minS = -1;
        
        fin >> D >> N;
        
        for (int j = 0; j < N; j++)
        {
            fin >> K >> S;
            
            if (minS == -1)
            {
                minK = K;
                minS = S;
            }
            
            else if ( ((D - minK) / (double)minS) < ((D - K) / (double)S) )
            {
                minK = K;
                minS = S;
            }
            
        }
        
        fout << fixed;
        fout.precision(6);
        fout << "Case #" << i + 1 << ": " << (double)D / ((D - minK) / (double)minS) << endl;
    }
    
    return 0;
}
