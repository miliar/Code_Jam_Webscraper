#include <iostream>
using namespace std;

long long check(long long n)
{
    long long temp,curr;
    temp=n%10;
    while(n>0)
    {
        curr=n%10;
        if(curr>temp)
            return 1;
        temp=curr;
        n/=10;
    }
    return 0;
}

int main() {
    long long t,n,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        while(check(n))
        n--;
        cout<<"Case #"<<i<<": "<<n<<endl;
    }
    return 0;
}