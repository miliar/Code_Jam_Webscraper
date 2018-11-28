#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("input2.txt");
    ofstream cout("salida2.txt");
    long long int t, t2 = 1, n, pos;
    cin >> t;
    string x;
    while(t2<=t)
    {
        bool valor = false;
        long long int cont = 0;
        cin >> x >> n;
        long long int tam = x.length();
        for(long long int i = 0; i<tam; i++)
        {
            if(x[i]=='-')
            {
                if(i+n>tam)
                {
                    valor = true;
                    break;
                }
                cont++;
                pos = 0;
                while(pos<n)
                {
                    x[i+pos]=='-'?x[i+pos]='+':x[i+pos]='-';
                    pos++;
                }
            }
            else
            {
                continue;
            }
        }
        cout << "Case #" << t2 << ": ";
        if(valor)
        {
            cout << "IMPOSSIBLE\n";
        }
        else
        {
            cont==0?cout << "0\n":cout <<cont << "\n";
        }
        t2++;
    }
    return 0;
}
