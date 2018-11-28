#include<bits/stdc++.h>
using namespace std;

long long int minimum(long long int a,long long int b)
{
    return a<b?a:b;
}
long long int maximum(long long int a,long long int b)
{
    return a>b?a:b;
}
int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("output_small.txt","w",stdout);
    long long int q,n,k,a,b,m[100005],x,y,bg,h,str,stp;
    cin>>q;
    int z=1;
    while(z!=q+1)
    {
        cin>>n>>k;
        for(int i=1;i<n+1;i++)
            m[i]=0;
        m[0]=1;
        m[n+1]=1;
        while(k--)
        {
            h = 0;bg = 1;str = stp = -1;
            for(int i=n;i>=0;i--)
            {
                if(m[i]==0)
                {
                    if(h==0)
                        x = i;
                    h++;
                }
                else
                {
                    if(h>=bg)
                    {
                        str = x;
                        stp = i;
                        bg=h;
                    }
                    h=0;
                }
            }
            //cout<<"big: "<<bg<<"  str: "<<str<<"  stp: "<<stp<<endl;
            if((str-stp)%2==0)
                m[ stp + (str-stp)/2 ]=1;
            else
                m[stp + (str-stp)/2+1]=1;
        }

        if((str-stp)%2==0)
            y =stp + (str-stp)/2 ;
        else
            y = stp + (str-stp)/2+1;
        a = 0;b=0;
        for(int i=y+1;m[i]!=1;i++)
        {
            if(m[i]==0)
                b++;
        }
        for(int i=y-1;m[i]!=1;i--)
        {
            if(m[i]==0)
                a++;
        }
        /*
        for(int i=0;i<n+2;i++)
            cout<<m[i]<<" ";
        cout<<endl;
        */
        cout<<"Case #"<<z<<": "<<maximum(a,b)<<" "<<minimum(a,b)<<endl;
        z++;
    }
    return 0;
}

