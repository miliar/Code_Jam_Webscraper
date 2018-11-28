#include <iostream>

using namespace std;

int check(int n)
{
    long long t,t2,i=0;
    while(n)
    {
        t2=t;
        t=n%10;
        if(i!=0&&t2<t)
        {
            return 0;
        }
        i++;
        n=n/10;
    }
    return 1;
}

int main()
{
    int T,c=1;
    long long n,ans,i;
    cin>>T;
    while(T--)
    {
    cin>>n;
    for(i=n;i>=1;i--)
    {
        if(check(i))
        {
            ans=i;
            break;
        }
    }

    cout<<"Case #"<<c<<": "<<ans;
    c++;
    }
    return 0;
}
