#include <iostream>
#include <bits/stdc++.h>
#include<math.h>
using namespace std;
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0 output.in","w",stdout);
    int t;
    long long int n,k,l,p,y,a,b,x,z;
    cin>>t;
    for(int c=1;c<=t;c++)
    {
        cin>>n>>k;
        for(int i=0;i<=60;i++)
        {
            if(k<=pow(2,i)-1)
            {
                l=i;
                break;
            }
        }
        a=pow(2,l);
        b=pow(2,l-1)-1;
        p=n/a;
        y=n-p*a+1;
        x=(a-y);

        cout<<"Case #"<<c<<": ";
        if(x==y)
        {
            cout<<p<<" "<<p-1<<endl;
        }
        else if(x>y)
        {
            if(k-b<=y)
                cout<<p<<" "<<p-1<<endl;
            else
                cout<<p-1<<" "<<p-1<<endl;
        }
        else if(y>x)
        {
            z=(y-x)/2;
            if(k-b<=z)
               cout<<p<<" "<<p<<endl;
            else
                cout<<p<<" "<<p-1<<endl;
        }
    }
    return 0;
}
