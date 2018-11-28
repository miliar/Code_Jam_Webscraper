#define _USE_MATH_DEFINES
#include<iostream>
#include<fstream>
#include<iomanip>
#include<cmath>
#include<cctype>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;

int main(int argc, char** argv)
{
    ifstream fin; 
    ofstream fout;
    if (argc != 3)
    {
        cout << "incorrect usage" << endl;
        return -1;
    }
    fin.open(argv[1]);
    if (!fin)
    {
        cout << "input file not open error" << endl;
        return -1;
    }
    fout.open(argv[2]);
    if (!fout)
    {
        cout << "output file not open error" << endl;
        return -1;
    }
    int n;
    fin >> n;
    for (int i = 0; i < n; i++)
    {
        long long k; 
        fin >> k;
        bool tidy=false;
        long long j;
        if (k<19)
            fout << "Case #" << i + 1 << ": " << k << endl;
        else
        {
            for (j = k; j >= 1 && !tidy; j--)
            {
                long long n1 = j;
                int last = n1 % 10;
                int p;
                tidy = true;
                while (n1 != 0 && tidy)
                {
                    p = n1 % 10;
                    if (p <= last)
                        last = p;
                    else
                        tidy = false;
                    n1 = n1 / 10;
                }
            }
            fout << "Case #" << i + 1 << ": " << j+1 << endl;
        }

    }
    return 0;
}


