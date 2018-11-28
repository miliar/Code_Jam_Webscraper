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
    long long t,n,i,a[20],l,ctr,j;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        ctr=0;
        cin>>n;
        while(n>0)
        {
            a[ctr]=n%10;
            ctr++;
            n/=10;
        }
        l=ctr-1;
        for(j=0;j<20;j++)
        {
            ctr=l-1;
            while(ctr>=0)
            {
                if(a[ctr]<a[ctr+1])
                {
                 a[ctr+1]--;
                 while(ctr>=0)
                 {
                     a[ctr]=9;
                     ctr--;
                 }
                  goto end;
                }
                ctr--;
            }
            end:;
        }
        cout<<"Case #"<<i<<": ";
        j=l;
        while(a[j]==0)
        j--;
        while(j>=0)
        {
            cout<<a[j];
            j--;
        }
        cout<<endl;
    }
    return 0;
}