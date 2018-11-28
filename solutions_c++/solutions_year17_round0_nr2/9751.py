#include <iostream>
#include <fstream>
#define ull unsigned long long

using namespace std;
ifstream FE ("B-small-attempt0.in");
ofstream FS("ouput.out");
bool EsOrdenada(ull n)
{
    int m=10;
    while(n)
    {
        if(n%10>m)
            return false;
        else if(n%10<m)
            m=n%10;
        n/=10;
    }
    return true;
}
void Caso(int caso)
{
    ull n;
    FE>>n;
    while(EsOrdenada(n)==false)
        n--;
    FS<<"Case #"<<caso<<": "<<n<<endl;
}

int main()
{
    int T;
    FE>>T;
    for(int i=1;i<=T;i++)
        Caso(i);
    FE.close();
    FS.close();
}
