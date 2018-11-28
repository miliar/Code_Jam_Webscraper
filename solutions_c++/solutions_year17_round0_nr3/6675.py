#include<iostream>
#include<algorithm>
using namespace std;
int main()
{     int t1,tt;
       cin>>t1;
       tt=t1;
       while(t1--)
       {
     int n,i,k,yo,pos,j,y,z;
         cin>>n>>k;
        struct stall
        {
            int o;
            int d;
        };
        stall *s=new stall[n+2];
        for(i=1;i<=n;i++)
        {

            s[i].o=0;
            s[i].d=0;
        }
        s[0].o=1;
        s[n+1].o=1;
        s[0].d=n;
        s[n+1].d=0;
        for(i=0;i<k;i++)
        {   int m=0;
            for(j=0;j<n;j++)
            {
                if(s[j].d>m)
                {m=s[j].d;
                pos=j;
                }
            }
            if(m%2==0)
            {   yo=pos+m/2;
                s[yo].o=1;
            s[yo].d=m/2;
                s[pos].d=m/2-1;
            }
            if(m%2!=0)
            {
                yo=pos+m/2+1;
                s[yo].o=1;
            s[yo].d=m/2;
            s[pos].d=m/2;
            }
        }
        y=s[pos].d;
        z=s[yo].d;
        if(y>z)
            cout<<"Case #"<<tt-t1<<": "<<y<<" "<<z<<endl;
        else
            cout<<"Case #"<<tt-t1<<": "<<z<<" "<<y<<endl;

    }
return 0;
}


