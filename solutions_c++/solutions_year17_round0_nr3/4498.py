#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int main()
{
    ifstream fin("C-small-2-attempt0.in");
    ofstream fout("output.out");

    //-- check if the files were opened successfully
    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int numCase;
    fin >> numCase;
    int i,d;
    long long n,k ,c;
    for (i = 0; i < numCase; i++)
    {
        fin >> n >> k;
        c = k;
        int count = log2(k);
        int g = pow(2,count);
        n = (((n-c))/g)+1;
        fout << "Case #" << (i + 1) << ": " << n/2 <<" "<<(n-1)-n/2 << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
