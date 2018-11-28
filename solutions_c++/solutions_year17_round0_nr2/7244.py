#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
typedef long double ld;

#define MAX1 100005
#define mod1 1000000009
#define mod 1000000007
#define rep0(i,n) for(int(i)=0; (i)<(n);++(i))
#define rep1(i,n) for(int(i)=1; (i)<(n);++(i))
#define rep2(i,n) for(int(i)=1; (i)<=(n);++(i))
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

int main()
{
    ll t;
    cin>>t;
    int co=1;
    while(t--)
    {
        ll n;
        cin>>n;
        ll a[20];
        ll i=0;
        while(n>0)
        {
            a[i]=n%10;
            n=n/10;
            i++;
        }
        for(int j=0;j<i-1;j++)
        {
           if(a[j]<a[j+1])
           {
               a[j+1]-=1;
               for(int k=j;k>=0;k--)
               {
                   a[k]=9;
               }
           }
        }
        cout<<"Case #"<<co<<": ";
        co++;
        int flag=0;
        for(int j=i-1;j>=0;j--)
        {
            if(flag==0 && a[j]==0)
            {
                continue;
            }
            else
            {
                flag=1;
                cout<<a[j];
            }
        }
        cout<<"\n";

    }
    return 0;
}

