#include <iostream>
#include <fstream>

using namespace std;

ifstream in("data.in");
ofstream out("data.out");


long long int x;

long long verif()
{
    int p=x;
    while(p>=10)
    {
        if(p%10<((p%100)/10))
        {
            return 0;
        }
        else
            p=p/10;
    }
    return 1;
}

int main()
{
    int tests;
    in>>tests;
    for(int i=1; i<=tests; i++)
    {
        out<<"Case #"<<i<<": ";
        in>>x;
        if(x<10)
        {
            out<<x<<'\n';
        }
        else
        {
            while(verif()==0)
            {
                x--;
            }
            out<<x<<'\n';
        }
    }
}
