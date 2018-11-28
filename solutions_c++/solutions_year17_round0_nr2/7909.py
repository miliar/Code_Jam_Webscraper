#include<fstream>
#include<vector>
#include<string>
#define modulo 666013

using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");


string sir;

long long int i, n, k, j,t,st,dr,sol,x,y,aux;
int a[100];

int nrDigit(long long int x)
{
    int k = 0;
    while(x)
    {
        k++;
        x = x / 10;
    }
    return k;
}


bool check(long long int x,int test)
{
    int k = nrDigit(x);
    int aux = k;
    //fout <<k<<"\n";
    while(x)
    {
        //fout<<k <<" ";
        a[k] = x % 10;
        k--;
        x = x / 10;
    }
    k = aux;
    int poz = -1;
    for(int i = 1; i < k; i++)
    {
        if(a[i] >= a[i + 1])
        {
            poz = i;
            break;
        }

    }
    a[poz]--;
    for(i = poz + 1; i <= k; i++)
    {
       a[i] = 9;
    }

    fout << "Case #" << test <<": ";
    for(int i = 1; i <= k; i++)
    {
        if(a[i] != 0)
        {
            fout << a[i];
        }

    }
    fout <<"\n";
}


bool verifSol(long long int x)
{
    int k = nrDigit(x);
    int aux = k;
    //fout <<k<<"\n";
    while(x)
    {
        //fout<<k <<" ";
        a[k] = x % 10;
        k--;
        x = x / 10;
    }
    k = aux;
    int poz = -1;
    for(int i = 1; i < k; i++)
    {
        if(a[i] > a[i + 1])
        {
            return false;
        }
    }
    return true;
}

bool hasZero(long long int x)
{
    int k = 0;
    while(x)
    {
        if(x % 10 == 0)
            return true;
        x = x / 10;
    }
    return false;
}



int main()
{
    fin >> t;
    for(int  r = 1; r <= t; r++)
    {
        fin >> aux;
        x = aux;
        if(verifSol(x) == true)
        {
            fout << "Case #" << r <<": " << x <<"\n";
        }
        else
        {
            x = aux;
            /*if(hasZero(x) == true)
            {
                 fout << "Case #" << r <<": ";
                 k = nrDigit(x);
                 for(i = 1; i < k; i++)
                 {
                     fout <<"9";
                 }
                 fout<<"\n";
            }
            else*/
            {
                x = aux;
                check(x, r);
                //fout << "Case #" << r <<": " << sol <<"\n";
            }
        }

    }
}
