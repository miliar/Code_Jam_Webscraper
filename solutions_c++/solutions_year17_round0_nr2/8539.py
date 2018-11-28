#include<bits/stdc++.h>
using namespace std;
long long int na[20];
void check(long long na[], int n)
{
    for(int i=1; i<n; i++)
    {
        if(na[i]>na[i-1])
        {
            na[i]-=1;
            for(int j=0; j<i; j++)
            {
                na[j]=9;
            }
            check(na,n);
        }
    }
    return;
}
int main()
{
    int z;
    cin>>z;
    long long int n,k;

    for(int t=1; t<=z; t++)
    {
        cin>>n;
        k=n;
        int i=0;
        while(k)
        {
            na[i]=k%10;
            k/=10;
            i++;
        }
        if(i==1)
        {
            cout<<"Case #"<<t<<": "<<n<<endl;
            continue;
        }
        check(na,i);
        k=0;
        long long int x=1;
        for(int j=0; j<i; j++)
        {
            k+=x*na[j];
            x*=10;
        }
        cout<<"Case #"<<t<<": "<<k<<endl;
    }
}
