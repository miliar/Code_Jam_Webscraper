#include<bits/stdc++.h>
using namespace std;
int main()
{       //freopen("C-large.in","r",stdin);
        //freopen("alok.out","w",stdout);
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        unsigned long long v[61];
        unsigned long long t,i,j,k,n,counter=0;
        unsigned long long level,element,last;
       for(k=1;k<61;k++)
        {
            v[k]=pow(2,k)-1;
        }
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n>>k;
        v[0]=0;
        /*for(i=0;i<61;i++)
        {
            cout<<v[i]<<" ";
            counter++;
        }
        cout<<"\n";
        cout<<counter;*/
        for(j=0;j<61;j++)
        {
            if(k<=v[j])
            {
                level=j;
                element=v[j];
                last=v[j-1];
                break;
            }
        }
        //cout<<level<<" "<<element<<" "<<last;
        unsigned long long x,y;
        x=n;
        for(j=1;j<=level;j++)
        {
            x=x/2;
        }
        //cout<<x;
        y=x-1;
        unsigned long long a,b,z,m,rema,final1,final2,diff;
        z=n-element;
        m=element+1;
       // cout<<z<<"\n";
       // cout<<m<<"\n";
       a=((z-(m*y))/(x-y));
       b=(((m*x)-z)/(x-y));
       //cout<<a<<"\n";
       //cout<<b<<"\n";
       rema=k-last;
       if(a>b)
       {
           diff=a-b;

           if(rema<=diff/2)
           {
              final1=x;
              final2=x;
           }
           else
           {
               final1=x;
               final2=y;
           }

       }
      else  if(b>a)
       {
           if(rema<=a)
           {
              final1=x;
              final2=y;
           }
           else
           {
               final1=y;
               final2=y;
           }
       }
       else if(b==a)
       {
           final1=x;
           final2=y;
       }
       cout<<"Case #"<<i<<": "<<final1<<" "<<final2<<endl;
    }
    return 0;

}
