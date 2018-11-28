#include<iostream>
using namespace std;
int func(long long int i);
int main()
{
    int T,x=01;
    long long int N,i;
    cin>>T;
    while(T--)
    {
              cin>>N;
              i=N;
              while(i>0)
              {
                        if(func(i)==1)
                        {cout<<"Case #"<<x<<": "<<i<<endl;break;}
                        else i--;
              }
              x++;
    }
    return 0;
}
int func(long long int i)
{
    int j,flag=1;
    long long int x,l=0;
    x=i;
    while(x)
    {x/=10;l++;}
    int  A[l];
    for(j=0;j<l;j++)
    {
                    A[j]=i%10;
                    i/=10;
    }
    for(j=0;j<l-1;j++)
    {
                    if(A[j]<A[j+1])
                    {flag=0;break;}
    }
    return (flag);
}
