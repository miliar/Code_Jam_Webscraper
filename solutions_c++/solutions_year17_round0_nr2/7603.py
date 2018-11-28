#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int b=1;
    while(b<=t)
    {
        long long int n;
        cin>>n;
        int a[19],j=0,k,i;
        for(i=0;i<=18;i++)
            a[i]='$';
        while(n!=0)
        {
            a[j]=n%10;
            n=n/10;
            j++;
        }
        for(i=1;i<j;i++)
        {
            if(a[i]>a[i-1])
            {
                a[i]=a[i]-1;
                for(k=0;k<=i-1;k++)
                   a[k]=9;
                }
        }
        cout<<"Case #"<<b<<": ";
        b++;
        int g=0;
        for(i=j-1;i>=0;i--)
        {
            if(a[i]==0)
            g++;
            else
                break;
        }
        for(i=j-1-g;i>=0;i--)
        {
          cout<<a[i];
        }
          cout<<"\n";
    }
}
