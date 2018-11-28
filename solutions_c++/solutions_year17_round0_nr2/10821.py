#include <iostream>
#include<bits/stdc++.h>
using namespace std;
typedef long long int ull;

int main()
{
    ull t;
    cin>>t;
    for(ull p=1;p<=t;p++)
    {
        ull n,tm,cnt,f;
        cin>>n;
        ull ar[100];
        for(ull i=n;i>=0;i--)
        {cnt=0,f=0;
            tm=i;
            while(tm!=0)
            {
               ar[cnt++]=tm%10;
               tm/=10;
            }
            for(ull j=0;j<cnt-1;j++)
            {
                if(ar[j+1]>ar[j])
                {
                    f=1;
                    break;
                }
            }
            if(f==0)
            {
               cout<<"Case #"<<p<<": "<<i<<endl;
               break;
            }
        }
    }
    return 0;
}
