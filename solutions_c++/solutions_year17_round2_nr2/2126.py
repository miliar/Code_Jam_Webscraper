#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll pw(ll a,ll b)
{
  ll x=1;
  while(b)
  {
    if(b&1)
     x*=a;
    a*=a;
    b>>=1;
  }
  return x;
};
int a[10];
int main()
{
   //freopen("B-small-attempt2.in", "r", stdin);
   //freopen("a.out", "w", stdout);
  cout.precision(7);
  int t,c,n,i;
  ll d;
  scanf("%d",&t);
  string s;
  for(c=1;c<=t;c++)
  {
    for(i=0;i<7;i++)
    {
      scanf("%d",&a[i]);
    }
    s.clear();
    int x,y,z,j;
    x=a[1];
    y=a[3];
    z=a[5];
    if(x>=y && x>=z)
    {
      if(x>(y+z))
       s="IMPOSSIBLE";
      else if(x==(y+z))
      {
        for(j=0;j<x;j++)
        {
          s+='R';
          if(y>0)
          {
            s+='Y';
            y--;
          }
          else if(z>0)
          {
            z--;
            s+='B';
          }
        }
      }
      else
      {
        int tmp=y+z-x;
        if(y<tmp/2 || z<tmp/2)
         s="IMPOSSIBLE";
        else
        {
         if(tmp>0){
         if(x%2==0 && tmp&1)
         {
           if(y&1)
           {
             y--;
             s+='Y';
             for(j=0;j<tmp/2;j++)
             {
               s+='B';
               s+='Y';
               y--;
               z--;
             }
           }
           else if(z&1)
           {
             z--;
             s+='B';
             for(j=0;j<tmp/2;j++)
             {
               s+='Y';
               s+='B';
               y--;
               z--;
             }
           }
         }
         else
         {
           if(y>0)
           {
             y--;
             s+='Y';
             for(j=0;j<tmp/2;j++)
             {
               s+='B';
               s+='Y';
               y--;
               z--;
             }
           }
           else if(z>0)
           {
             z--;
             s+='B';
             for(j=0;j<tmp/2;j++)
             {
               s+='Y';
               s+='B';
               y--;
               z--;
             }
           }
         }
         }
         for(j=0;j<x;j++)
         {
          s+='R';
          if(s[0]=='Y' && y>0)
          {
            y--;
            s+='Y';
          }
          else if(s[0]=='B' && z>0)
          {
            z--;
            s+='B';
          }
          else if(y>0)
          {
            y--;
            s+='Y';
          }
          else if(z>0)
          {
            z--;
            s+='B';
          }
         }
        }
      }
    }
    else if(y>=x && y>=z)
    {
       if(y>(x+z))
       s="IMPOSSIBLE";
      else if(y==(x+z))
      {
        for(j=0;j<y;j++)
        {
          s+='Y';
          if(x>0)
          {
            s+='R';
            x--;
          }
          else if(z>0)
          {
            z--;
            s+='B';
          }
        }
      }
      else
      {
        int tmp=x+z-y;
        if(x<tmp/2 || z<tmp/2)
         s="IMPOSSIBLE";
        else
        {
         if(tmp>0){
         if(y%2==0 && tmp&1)
         {
           if(x&1)
           {
             x--;
             s+='R';
             for(j=0;j<tmp/2;j++)
             {
               s+='B';
               s+='R';
               x--;
               z--;
             }
           }
           else if(z&1)
           {
             z--;
             s+='B';
             for(j=0;j<tmp/2;j++)
             {
               s+='R';
               s+='B';
               x--;
               z--;
             }
           }
         }
         else
         {
           if(x>0)
           {
             x--;
             s+='R';
             for(j=0;j<tmp/2;j++)
             {
               s+='B';
               s+='R';
               x--;
               z--;
             }
           }
           else if(z>0)
           {
             z--;
             s+='B';
             for(j=0;j<tmp/2;j++)
             {
               s+='R';
               s+='B';
               x--;
               z--;
             }
           }
         }
         }
         for(j=0;j<y;j++)
         {
          s+='Y';
          if(s[0]=='R' && x>0)
          {
            s+='R';
            x--;
          }
          else if(s[0]=='B' && z>0)
          {
            z--;
            s+='B';
          }
          else if(x>0)
          {
            x--;
            s+='R';
          }
          else if(z>0)
          {
            z--;
            s+='B';
          }
         }
        }
      }
    }
    else if(z>=x && z>=y)
    {
       if(z>y+x)
       s="IMPOSSIBLE";
      else if(z==(y+x))
      {
        for(j=0;j<z;j++)
        {
          s+='B';
          if(y>0)
          {
            s+='Y';
            y--;
          }
          else if(x>0)
          {
            x--;
            s+='R';
          }
        }
      }
      else
      {
        int tmp=y+x-z;
         if(y<tmp/2 || x<tmp/2)
          s="IMPOSSIBLE";
         else
         {
         if(tmp>0)
         {
         if(z%2==0 && tmp&1)
         {
           if(y&1)
           {
             y--;
             s+='Y';
             for(j=0;j<tmp/2;j++)
             {
               s+='R';
               s+='Y';
               y--;
               x--;
             }
           }
           else if(x&1)
           {
             x--;
             s+='R';
             for(j=0;j<tmp/2;j++)
             {
               s+='Y';
               s+='R';
               y--;
               x--;
             }
           }
         }
         else
         {
           if(y>0)
           {
             y--;
             s+='Y';
             for(j=0;j<tmp/2;j++)
             {
               s+='R';
               s+='Y';
               y--;
               x--;
             }
           }
           else if(x>0)
           {
             x--;
             s+='R';
             for(j=0;j<tmp/2;j++)
             {
               s+='Y';
               s+='R';
               y--;
               x--;
             }
           }
         }
         }
         for(j=0;j<z;j++)
         {
          s+='B';
          if(s[0]=='R' && x>0)
          {
            x--;
            s+='R';
          }
          else if(s[0]=='Y' && y>0)
          {
            y--;
            s+='Y';
          }
          else if(y>0)
          {
            y--;
            s+='Y';
          }
          else if(x>0)
          {
            x--;
            s+='R';
          }
         }
        }
      }
    }
    cout<<"Case #"<<c<<": "<<s<<endl;
  }
  return 0;
}
