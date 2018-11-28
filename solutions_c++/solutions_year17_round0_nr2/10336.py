#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<fstream>
#include<string>

using namespace std;

int tam(long long int x)
{
    int k=0;
    while(x>=pow(10,k))
    {
        k++;
    }
    return k-1;
}
int main ()
{
    int n,numero;
    fstream in;
    ofstream out;
    string line;
    in.open("input.in");
    out.open("output.txt");
    if(in)
    {
        in>>line;
        n=stoi(line);
        int tr=1;
        while(getline (in,line) && tr==1)
        {
            in>>line;
            numero=stoi(line);
            for(int i=1; i<=n; i++)
            {
                if(i>1){
                    in>>line;
                    numero=stoi(line);
                }
                for(int k=numero; k>=0; k--)
                {
                    int siz=tam(k);
                    int A[siz];
                    int copia=k;
                    for(int j=siz; j>=0; j--)
                    {
                        A[j]=copia%10;
                        copia=copia/10;
                    }
                    bool sw=true;
                    int cont=0;
                    while(cont <siz && sw)
                    {
                        if(A[cont]<=A[cont+1])
                        {
                            cont++;
                        }
                        else
                        {
                            sw=false;
                            cont++;
                        }
                    }
                    if(sw)
                    {
                        int num=0;
                        for(int j=0; j<=siz; j++)
                        {
                            num=num+A[siz-j]*pow(10,j);
                        }
                        out<<"Case #"<<i<<": "<<num<<endl;
                        break;
                    }
                }

            }
        }
        in.close();
        out.close();
    }
    return 0;

}
