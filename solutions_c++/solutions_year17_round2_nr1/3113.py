#include<iostream>
#include<bits/stdc++.h>
using namespace std;
long long int a[10005],b[10005];
int main()
{
    int i=0,t;
    long long int d,n,j,temp,q,e;
    long double w,maxi;
    cin>>t;
    while(t--)
    {
        j=0;
        maxi=0;
       cin>>d>>n;
       //cout<<i<<endl<<endl<<endl;
       //cout<<d<<" "<<n<<endl;
       temp=n;
       while(n--)
       {
           cin>>a[j]>>b[j];
         //  cout<<a[j]<<" "<<b[j]<<endl;
           j++;
       }
        for(long long int k=0;k<temp;k++)
        {
         q=d-a[k];
         w=double(q)/double(b[k]);
         maxi=max(maxi,w);

        }
        //cout<<maxi<<"**"<<endl;
        w=d/maxi;
i++;
        cout<<"Case #"<<i<<": ";
          std::cout << std::fixed;
    std::cout << std::setprecision(6);
    std::cout << w;
        cout<<endl;

    }
    return 0;
}
