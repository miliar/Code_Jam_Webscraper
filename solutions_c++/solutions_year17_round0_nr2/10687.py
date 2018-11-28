#include <iostream>
#include <fstream>
using namespace std;
ifstream f("B-small-attempt0.in");
ofstream g("B-small-attempt0.out");
long long n;
int c1,c2;
int t;
bool correct()
{
    long long k=n;
    c1=k%10;
    k=k/10;
    while(k)
    {
        c2=k%10;
        k=k/10;
        if(c1<c2) return 0;
        c1=c2;
    }
    return 1;
}
int main()
{
    f>>t;
    for(int i=1;i<=t;i++)
    {
        f>>n;
        while(!correct())
        {
            n--;
        }
        g<<"Case #"<<i<<": "<<n<<"\n";
    }
    return 0;
}
