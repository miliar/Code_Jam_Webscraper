#include<iostream>
using namespace std;
bool check(unsigned long long n)
{
    unsigned long long l=n%10;
    n=n/10;
    while(n>0)
    {
        unsigned long long a=n%10;
        n=n/10;
        if(l>=a)
        {
            l=a;
            continue;
        }
        else
        {
            return 0;
        }
    }
    return 1;
}
unsigned long long cool(unsigned long long n)
{
    unsigned long long count=9,oo;
    n=n/10;
    while(n>0)
    {
        oo=n;
        n=n/10;
        count=count*10+9;
    }
    if(oo==1)
    return count;
    else
        return 0;
}
int main()
{
    unsigned long long t;
    cin>>t;
    unsigned long long b[t];
    for(unsigned long long i=0;i<t;i++)
    {
        unsigned long long n;
        cin>>n;
        unsigned long long ii=n;
        if(n%10==0)
        {
            n=n/10;
            unsigned long long h=cool(n);
            b[i]=h;
            if(b[i]!=0)
            continue;
        }
        n=ii;
        unsigned long long a=check(n);
        while(a!=1)
        {
            n--;
            a=check(n);
        }
        b[i]=n;
    }
    for(unsigned long long i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": "<<b[i]<<"\n";
    }
    return 0;
}
