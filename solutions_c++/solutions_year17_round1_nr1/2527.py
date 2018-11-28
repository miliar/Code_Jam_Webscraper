#include<bits/stdc++.h>
using namespace std;
#define ll long long
string st[1000];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
     ios::sync_with_stdio(0);
     ll t,tt=0;
     cin>>t;
     while(t--)
     {
          tt++;
          cout<<"Case #"<<tt<<":\n";
          ll r,c;
          cin>>r>>c;
          for(int i=0;i<r;i++)
          {
               cin>>st[i];
          }

          for(int i=0;i<r;i++)
          {
               for(int j=1;j<c;j++)
               {
                    if(st[i][j]=='?')
                    {
                         st[i][j]=st[i][j-1];
                    }
               }
               for(int j=c-2;j>=0;j--)
               {
                    if(st[i][j]=='?')
                    {
                         st[i][j]=st[i][j+1];
                    }
               }
          }

          for(int i=1;i<r;i++)
          {
               for(int j=0;j<c;j++)
               {
                    if(st[i][j]=='?')
                    {
                         st[i][j]=st[i-1][j];
                    }
               }
          }
          for(int i=r-2;i>=0;i--)
          {
               for(int j=0;j<c;j++)
               {
                    if(st[i][j]=='?')
                    {
                         st[i][j]=st[i+1][j];
                    }
               }
          }
          for(int i=0;i<r;i++)
          cout<<st[i]<<"\n";
          //cout<<"\n";
     }

}
