#include <iostream>
#include <stdio.h>

using namespace std;

#define ull unsigned long long int

ull i,j,k,n,c,t,p,a[22],maxx,flag,dmax,l;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.in","w",stdout);
    cin>>t;
    l=1;
    while(t--)
    {
        scanf("%llu",&n);
        maxx=21;
        i=1;

        while(n!=0)
        {
            a[i]=n%10;
            if(a[i]==0)
                maxx=i;
            n=n/10;
            i++;
        }
        c=--i;
        dmax=1;
        if(maxx!=21)
            dmax=maxx+1;
        while(maxx>=1&&maxx!=21)
        {
            a[maxx--]=9;
        }
        if(maxx!=21)
            a[dmax]=a[dmax]-1;
        for(i=dmax;i<=c;i++)
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
