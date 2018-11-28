//Ashwani NSIT
//codejam 2017 round a - 1
#include <bits/stdc++.h>

using namespace std;

#define ll long int

int main()
{
   freopen("A-large.in","r",stdin);
 freopen("ansa.out","w",stdout);
ll t,t1=0;
cin>>t;
while(t--)
{t1++;
ll r,c,i,j,z;
cin>>r>>c;
string str[r];
for(i=0;i<r;i++)
{
cin>>str[i];
}
for(i=0;i<r;i++)
 {
  for(j=0;j<c;j++)
   {
    if(str[i][j]!='?')
     {
    for(z=0;(z<c)&&(str[i][z]=='?'||str[i][z]==str[i][j]||z<j);z++)
       {
        if((z<j)&&(str[i][z]=='?'))
          {
            str[i][z]=str[i][j];
          }
        else
         {if((z>j)&&(str[i][z]=='?'))
         {
      str[i][z]=str[i][j];
         }
         }
       }
     }
   }
 }

for(i=0;i<r;i++)
 {
  for(j=0;j<c;j++)
   {
    if(str[i][j]!='?')
     {
    for(z=0;z<r&&(str[z][j]=='?'||str[z][j]==str[i][j]||z<i);z++)
       {
        if((z<i)&&(str[z][j]=='?'))
          {
            str[z][j]=str[i][j];
          }
        else
         {if((z>i)&&(str[z][j]=='?'))
         {
      str[z][j]=str[i][j];
         }
         }
       }
     }
   }
 }


        cout<<"Case #"<<t1<<": "<<endl;
        for(i=0;i<r;i++)
        {
            cout<<str[i]<<endl;
        }

    }
     return 0;
}
