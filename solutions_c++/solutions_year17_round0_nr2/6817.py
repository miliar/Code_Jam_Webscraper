#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define SF scanf
#define PF printf
#define PB push_back
#define MP make_pair
#define mx 4000001
#define INP          freopen("B-large.in", "r", stdin);
#define OUT          freopen("out.txt", "w", stdout);
#define BOOST        std::ios_base::sync_with_stdio(false);
ll a[mx];
ll b[mx];
map<string,int>mp;
int main()
{
   INP;
   OUT;
    ll n,t,i,j,m,f,p,p1,flag,c=0,c1,q,k,pai,s,s2,op=0,c2;
    t=1;
    string st;
    n=0;
    op=10;
    cin>>q;
    while(q--)
    {
        cin>>n;
        c=0;
        f=0;
        c1=9;
        c2=0;

        while(n!=0)
        {
            b[c++]=n%10;

            if(b[c-1]==0)
            {
                f=1;
            }
            c1=min(c1,b[c-1]);
            c2=max(c2,b[c-1]);
            n/=10;
        }
        for(i=c-1;i>=0;i--)
        {
            a[(c-1)-i]=b[i];
        }
        s=0;
        //if(s2==)
        f=0;

        if(f==0)
        {
            cout<<"Case #"<<t++<<": ";
            f=0;
            for(i=0;i<c-1;i++)
            {
                if(a[i]>a[i+1])
                {
                    f=1;
                }
                s=s*10+a[i];
            }
            if(f==0)
            {
                s=s*10+a[c-1];
            }
            else
            {
                f=0;
                s=0;
                for(i=0;i<c-1;i++)
                {
                   // cout<<a[i]<<endl;
                   c1=0;
                   p=0;
                   for(j=i+1;j<c;j++)
                   {
                     //  cout<<a[j]<<" "<<a[i]<<endl;
                       if(a[j]>=a[j-1])
                       {
                           p=a[j];

                       }
                       else
                        break;
                        //cout<<p<<endl;
                   }
                   //cout<<p<<endl;

                   if(a[i]<p)
                   {
                       s=s*10+a[i];
                   }
                   else if(a[i]==1)
                   {
                        i++;
                       while(i<c)
                       {
                           f=1;
                           i++;
                           s=s*10+9;

                       }
                   }
                   else
                   {
                       s=s*10+(a[i]-1);
                       i++;
                       while(i<c)
                       {
                           f=1;
                           i++;
                           s=s*10+9;

                       }
                   }

                }
                if(f==0)
                {
                    s=s*10+(a[c-1]);
                }


            }
            cout<<s<<endl;

        }

    }

return 0;
}
