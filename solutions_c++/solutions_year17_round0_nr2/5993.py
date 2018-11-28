#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("input2.txt");
    ofstream cout("salida2.txt");
    string x;
    long long int t, t2 = 1;
    cin >> t;
    while(t2<=t)
    {
        cin >> x;
        long long int tam = x.length();
        long long int y = tam-1, pos = tam;
        bool valor = false;
        while(y>0)
        {
            if(x[y]<x[y-1])
            {
                if(y-1==0)
                {
                    valor = true;
                    break;
                }
                if(x[y-1]=='0')
                {
                    pos = y-1;
                }
                else
                {
                    x[y-1] = x[y-1]-1;
                    pos = y;
                }
            }
            y--;
        }
        cout << "Case #" << t2 << ": ";
        if(tam==1)
            cout << x;
        else
        {
            if(valor)
            {
                if(x[0]!='1')
                {
                    cout << char(x[0]-1);
                }
                for(int i = 0; i<tam-1; i++)
                {
                    cout << "9";
                }
            }
            else
            {
                cout << x.substr(0,pos);
                for(int i = pos; i<tam; i++)
                {
                    cout << "9";
                }
            }
        }
        cout << endl;
        t2++;
    }
    return 0;
}
