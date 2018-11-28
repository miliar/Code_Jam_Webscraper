#include<bits/stdc++.h>
#define ull unsigned long long
using namespace std;
main()
{
    freopen("input1.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    ull t,T=1;
    cin>>t;
    while(t--)
    {
        ull n;
        cin>>n;
        int d[20],i=0;
        ull te=n;
        while(te)
        {
            d[i++]=te%10;
            te=te/10;
        }
        int di=i;
        for(i=0;i<di-1;i++)
        {
            if(d[i]<d[i+1])
            {
                for(int k=i;k>=0;k--)
                    d[k]=9;
                d[i+1]--;
            }
        }
        ull ans=0;
        bool c=0;
        cout<<"Case #"<<T<<": ";
        for(i=di-1;i>=0;i--)
        {
            if(d[i]>0)
                c=1;
            if(c!=0)
                cout<<d[i];
        }
        cout<<'\n';
        T++;
    }
}
