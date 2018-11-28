#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("INPUT.IN");
    ofstream fout("OUTPUT.OUT");

    long long T,b; fin >> T;
    long long Case = 0;

    for(b = 1;b <= T;b++)
    {
        Case++;

        long long j,n,i,count = 0;
        fin >> n;

        //Count digits
        long long clone = n;
        do{count++;}while(clone/=10);

        //Store digits
        long long a[count]; clone = n, i = count;
        while(clone != 0)
        {
            a[--i] = clone % 10;
            clone /= 10;
        }

        fout << "Case #" << Case << ": ";

        //Exception #1
        if(count == 1)
        {
            fout << n;
            if(b != T) fout << '\n';
            continue;
        }

        //Exception #2
        clone = 0;
        for(i = count-1;i >= 0;i--) clone += pow(10,i);
        if(n < clone)
        {
            for(i = 1;i < count;i++) fout << '9';
            if(b != T) fout << '\n';
            continue;
        }

        for(i = 0;i < count-1;i++)
        {
            if(a[i] > a[i+1])
            {
                a[i] = a[i]-1;

                for(j = i+1;j < count;j++) a[j] = 9;
                i = -1;
            }
        }

        if(a[0] != 0) for(i = 0;i < count;i++) fout << a[i];
        else for(i = 1;i < count;i++) fout << a[i];
        if(b != T) fout << '\n';
    }
    return 0;
}
