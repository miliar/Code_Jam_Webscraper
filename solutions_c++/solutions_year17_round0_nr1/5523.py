#include <bits/stdc++.h>
using namespace std;


int main()
{
     int n,i,j,p[1000],t;
     cin>>n;
     for(i=0;i<n;i++)
     {
         string s;
         int k,m,l,ans=0,c=0,i1=0;
         cin>>s>>k;
         m=s.size();
         for(j=0;j<m-k;j++)
         {
             l=0;
             if(s[j]=='-')
             {
                 for(i1=j;i1<j+k;i1++)
                 {
                     if(s[i1]=='-')
                     {
                         s[i1]='+';
                     }
                     else
                     {
                         s[i1]='-';
                     }
                 }
                 ans++;
             }
         }
         for(j=m-k;j<m;j++)
         {
             if(s[j]=='-')
             {
                 c++;
             }
         }
         if(c==k)
         {
             p[i]=ans+1;
         }
         else if(c==0)
         {
             p[i]=ans;
         }
         else
         {
             p[i]=-1;
         }
     }
     for(i=0;i<n;i++)
     {
         cout<<"Case #"<<i+1<<": ";
         if(p[i]==-1)
         {
             cout<<"IMPOSSIBLE";
         }
         else
         {
             cout<<p[i];
         }

         cout<<endl;
     }


     return 0;
}


