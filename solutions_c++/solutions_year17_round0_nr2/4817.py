#include<iostream>
using namespace std;
bool check(long long int &k)
{
    long long int n=k;
    if((n/10)==0)
    {
        return 1;
    }
    long long int c=0,l=0,a,b;
    while (true)
    {
        a=n%10;
        n/=10;
        b=n%10;
        c++;
        if(b>a)
        {
            while(c!=0)
            {
                n*=10;
                c--;
            }
            k=n;
            return 0;
        }
        if(n==0)
        {
            return 1;
        }
    }
}
int main()
{
    long long int a,n,c=0;
    cin>>n;
    for(long long int i=0;i<n;i++)
    {
        cin>>a;
        for(long long int j=a;j>=0;j--)
        {
            c++;
            if(check(j))
            {
                cout<<"Case #"<<i+1<<": "<<j<<endl;
                break;
            }
        }
    }
    return 0;
}