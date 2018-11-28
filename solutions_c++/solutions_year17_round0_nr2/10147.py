#include <bits/stdc++.h>
using namespace std;
int len(long long n)
{
    if(n==0)
    return 1;

    int l=0;
    while(n)
    {
        l++;
        n/=10;
    }
    return l;
}

long long power(int x,int y)
{
    long long res=1;
    for(int i=1;i<=y;i++)
    {
       res*=x;
    }
    return res;
}

long long tidy(long long n)
{
    int ln=len(n);
    if(ln==1)
    return n;

    int ar[ln],c=1,dn=n;
    for(int i=ln-1;i>=0;i--)
    {
       ar[i]=dn%10;
       dn/=10;
    }
    for(int i=1;i<ln;i++)
    {
        if(ar[i]<ar[i-1])
        break;
        c++;
    }
    if(c==ln)
    return n;

    long long n1=0;
    for(int i=0;i<c;i++)
    {
        n1=n1*10+ar[i];
    }
    long long n2=tidy(n1-1);
    long long n3=n2*power(10,ln-c);
    long long n4=power(10,ln-c)-1;
    return (n3+n4);
}

int main()
{
    int t;
    cin>>t;
    for(int l=1;l<=t;l++)
    {
        long long n;
        cin>>n;
        cout<<"Case #"<<l<<": "<<tidy(n)<<endl;
    }

    return 0;
}
