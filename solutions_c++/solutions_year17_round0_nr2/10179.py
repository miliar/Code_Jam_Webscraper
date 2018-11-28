#include <iostream>
#include<stdio.h>

typedef unsigned long long ull;

using namespace std;

void conv(int *a,ull n)
{
    a[0]=0;
    while(n)
    {
        a[++a[0]]=n%10;
        n/=10;
    }
}

ull display(int *a)
{
    ull n=0;
    int i=a[0];
    while(i)
    {
        n*=10;
        n+=a[i];
        i--;
    }
    return n;
}

void check(int *a,int i,int j)
{
    if(i==1)
        return;
    if(a[i]==a[i-1])
        check(a,i-1,j);
    if(a[i]<a[i-1])
        check(a,i-1,j-1);
    if(a[i]>a[i-1])
    {
     for(int k=1;k<j;k++)
            a[k]=9;
     a[j]--;
    }
}

int main()
{
   freopen("B-small-attempt0.in","r",stdin);
   freopen("outputtd0.out","w",stdout);

   ull n;
   int a[20],t;

   cin>>t;
   for(int i=1;i<=t;i++)
   {
    cin>>n;
    conv(a,n);
    check(a,a[0],a[0]);
    cout<<"Case #"<<i<<": "<<display(a)<<endl;
   }

   return 0;
}
