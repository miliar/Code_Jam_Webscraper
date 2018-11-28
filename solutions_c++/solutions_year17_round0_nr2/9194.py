#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int decrescente(int n)
{
    int minimo = 10;
    int conta = 0;
    while(n > 0)
    {
        int ultimo = n % 10;
        n = n/10;
        //cout << minimo << " " << ultimo << endl;
        if(ultimo <= minimo)
            minimo = ultimo;
        else
            return conta;
        conta++;
    }
    return -1;
}

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
        int numero;
        in >> numero;
        //int cont = 0;
        while(decrescente(numero) != -1)
        {
           // cout << numero << " " << decrescente(numero) << endl;
           // numero-= pow(10, a-1);
           // cont+= pow(10, a-1);
           numero--;
          // cont++;
        }
        out << numero << endl;
    }
}
