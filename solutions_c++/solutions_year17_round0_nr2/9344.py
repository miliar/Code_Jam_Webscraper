#include <iostream>
#include <fstream>
using namespace std;
ifstream in("date.in");
ofstream out("date.out");
long long n;

long long sol1(long long x)
{
    bool ok=1;
    while(ok==1){
        long long aux=x;
        ok=0;
        while(aux>0 && ok==0)
        {
            int uc=aux%10;
            aux /= 10;
            if(uc < aux%10)
                ok=1;
        }
        if(ok==1)
            x--;
    }
    return x;
}

long long sol2(long long x)
{
    int v[20];
    int nrcif,i;

    long long aux=x;
    i=0;
    while(aux>0)
        i++, v[i]=aux%10, aux/=10;
    nrcif=i;

    bool ok=1;
    while(ok){
        for(i=nrcif;i>1 && v[i]<=v[i-1];i--);
        if(i>1)
        {
            v[i]--;
            for(i=i-1;i>0;i--)
                v[i]=9;
        }
        else
            ok=0;
    }

    x=0;
    for(int i=nrcif;i>0;i--)
        x=x*10 + v[i];

    return x;
}

int main()
{
    int t;
    in>>t;
    for(int i=1;i<=t;++i)
    {
        in>>n;
        out<<"Case #"<<i<<": "<<sol2(n)<<"\n";
    }
    return 0;
}
