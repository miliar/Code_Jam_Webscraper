#include<stdlib.h>
#include<iostream>
#include<string.h>

using namespace std;

bool isTidy(long long int n,long long int *m)
{
    int dig,lastDig=9;
    long long int mf=1;
    while(n!=0)
    {
        dig=n%10;
        n/=10;
        mf*=10;
        if(dig>lastDig)
        {
            *m=mf;
            return false;
        }
        lastDig=dig;
    }
    return true;
}

int main()
{
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        long long int n,j,mf=1;
        cin>>n;
        for(j=n;j>=1;)
        {
            if(isTidy(j,&mf))
                break;
            mf/=10;
            j/=mf;
            j*=mf;
            j--;
        }
        if(j<1)
            j=1;
        cout<<"Case #"<<i<<": "<<j<<endl;
    }
}
