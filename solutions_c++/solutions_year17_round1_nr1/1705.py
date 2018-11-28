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
    int r,c;
    cin>>r>>c;

   string s[r];
   loop(i,r)
   cin>>s[i];
   char ch='?';
   bool done[r]={0};
   loop(i,r)
   {
       ch='?';
       loop(j,c)
       {
           if(s[i][j]!=ch)
            {
                ch=s[i][j];
                break;
            }

       }
       if(ch=='?')
       {
           done[i]=false;
       }
       else
       {
           done[i]=true;
           loop(j,c)
           {
               if(s[i][j]=='?')
               {
                   s[i][j]=ch;
               }
               else
                ch=s[i][j];
           }
       }

   }
   int first=0;
       loop(i,r)
       {
           if(done[i])
           {
               first=i;
               break;
           }
       }
   loop(i,r)
   {
       if(done[i]==false)
       {
           done[i]=true;
           s[i]=s[first];
       }
       else
       {
           first=i;
        }

   }



        cout<<"Case #"<<te<<": "<<endl;
loop(i,r)
{
    cout<<s[i]<<endl;
}


}




    return 0;
}




