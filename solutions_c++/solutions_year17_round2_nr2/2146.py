#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<map>
#include<cstdio>
#include<algorithm>
#define ll long long int
#define loop(i,n) for(ll i=0;i<n;i++)
#define loop2(i,a,b) for(ll i=a;i<b;i++)
#define mp(a,b) make_pair(a,b)
using namespace std;
ll power(ll a ,ll b)
{

    ll c=0;
    if(b==1)
        return a;
    if(b&1)//odd
    {
        c = power(a,b-1);
        return a*c;
    }
    else
    {
        c=power(a,b/2);
        return c*c;
    }

}
int main()
{

cin.tie(0);
cout.tie(0);

cin.sync_with_stdio(false);
cout.sync_with_stdio(0);

freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);



int t;
cin>>t;
for(ll te=1;te<=t;te++)
{

ll n;
cin>>n;
ll no=n;
ll r,o,y,g,b,v;
cin>>r>>o>>y>>g>>b>>v;
string ans="";
bool valid=true;
char ch='x';
while(n--)
{
    if(ch=='r')
    {
        if(g>0)
        {
            ans.append("G");
            g--;
            ch='g';
        }
        else if(b>y && b>0)
        {
            ans.append("B");
            b--;
            ch='b';
        }
        else if(y>0)
        {
             ans.append("Y");
            y--;
            ch='y';
        }
        else
        {
            valid=false;
            break;
        }

    }

    else if(ch=='o')
    {
        if(b>0)
        {
            ans.append("B");
            b--;
            ch='b';
        }
        else
        {
            valid=false;
            break;
        }
    }
      else if(ch=='g')
    {
        if(r>0)
        {
            ans.append("R");
            r--;
            ch='r';
        }
        else
        {
            valid=false;
            break;
        }
    }
     else if(ch=='v')
    {
        if(y>0)
        {
            ans.append("Y");
            y--;
            ch='y';
        }
        else
        {
            valid=false;
            break;
        }
    }
    else if(ch=='y')
    {
        if(v>0)
        {
            ans.append("V");
            v--;
            ch='v';
        }
        else if(b>r && b>0)
        {
            ans.append("B");
            b--;
            ch='b';
        }
        else if(r>0)
        {
             ans.append("R");
            r--;
            ch='r';
        }
        else
        {
            valid=false;
            break;
        }

    }
    else if(ch=='b')
    {
        if(o>0)
        {
            ans.append("O");
            o--;
            ch='o';
        }
        else if(r>y && r>0)
        {
            ans.append("R");
            r--;
            ch='r';
        }
        else if(y>0)
        {
             ans.append("Y");
            y--;
            ch='y';
        }
        else
        {
            valid=false;
            break;
        }

    }
    else if(r>0)
    {
        ch='r';
        ans.append("R");
        r--;

    }
    else if(y>0)
    {
        ch='y';
        ans.append("Y");
        y--;
    }
     else if(b>0)
    {
        ch='b';
        ans.append("B");
        b--;
    }
    else
    {
        if(n>1)
        {
            valid=false;
        }
           else
        {
            if(o>0)
            {
              if(ans[0]=='B')
              {
                  ans.append("O");
                  o--;
              }
              else
              {
                  valid=false;
              }
            }
            else if(g>0)
            {
                if(ans[0]=='R')
              {
                  ans.append("G");
                  g--;
              }
              else
              {
                  valid=false;
              }
            }
            else
            {
                 if(ans[0]=='Y')
              {
                  ans.append("V");
                  v--;
              }
              else
              {
                  valid=false;
              }
            }
       }
    }
}

if(valid)
{
   char c=ans[0];
    if(c=='O')
    {
        if(ans[no-1]!='B')
        {
            valid=false;
        }
    }
    else if(c=='G')
    {
       if(ans[no-1]!='R')
        {
            valid=false;
        }
    }
    else if(c=='V')
    {
       if(ans[no-1]!='Y')
        {
            valid=false;
        }
    }
    else if(c=='Y')
    {
       if(ans[no-1]!='R' && ans[no-1]!='B' && ans[no-1]!='V')
        {
            valid=false;
        }
    }
    else if(c=='R')
    {
       if(ans[no-1]!='Y' && ans[no-1]!='B' && ans[no-1]!='G')
        {
            valid=false;
        }
    }
    else
    {
               if(ans[no-1]!='Y' && ans[no-1]!='R' && ans[no-1]!='O')
        {
            valid=false;
        }
    }

}
//cout<<ans<<endl;
if(valid){
  cout<<"Case #"<<te<<": "<<ans<<endl;

}
else
{
    cout<<"Case #"<<te<<": "<<"IMPOSSIBLE"<<endl;
}

}
  //      cout<<"Case #"<<te<<": "<<endl;



    return 0;
}




