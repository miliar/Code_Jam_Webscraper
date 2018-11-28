#include <iostream>
#include <stdio.h>

using namespace std;

#define ull unsigned long long int

ull i,j,k,n,c,t,p,a[22],mxx,flg,dmx,l;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.in","w",stdout);
    cin>>t;
    l=1;
    while(t--)
    {
        scanf("%llu",&n);
        mxx=21;
        i=1;

        while(n!=0)
        {
            a[i]=n%10;
            if(a[i]==0)
                mxx=i;
            n=n/10;
            i++;
        }
        c=--i;
        dmx=1;
        if(mxx!=21)
            dmx=mxx+1;
        while(mxx>=1&&mxx!=21)
        {
            a[mxx--]=9;
        }
        if(mxx!=21)
            a[dmx]=a[dmx]-1;
        for(i=dmx;i<=c;i++)
        {
            if(a[i]<a[i+1]&&i+1!=c+1)
            {
                for(j=i;j>0;j--)
                {
                    a[j]=9;
                }
                a[i+1]=a[i+1]-1;
            }
        }
        cout<<"Case #"<<l<<":"<<" ";
        for(i=c;i>0;i--)
        {
            if(i==c&&a[i]==0)
                continue;
           cout<<a[i];
        }
        l++;
        cout<<endl;
    }
    return 0;
}
