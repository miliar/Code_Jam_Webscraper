#include <bits/stdc++.h>
using namespace std;

int main()
{
     int n,i,j,k,m=0,p1[200][20]={0},t;
     cin>>n;
     t=n;
     while(n--)
     {
         string s;
         int p[20],f=0;
         cin>>s;
         k=s.size();
         for(i=0;i<k;i++)
         {
             p[i]=s[i]-48;
         }
         for(i=k-2;i>=0;i--)
         {
             if(p[i+1]>=p[i])
             {

             }
             else
             {
                 p[i]--;
                 for(j=i+1;j<k;j++)
                 {
                     p[j]=9;
                 }
             }
         }


         j=1;
         int p2=0;
         for(i=0;i<k;i++)
         {
             if(p[i]<=0&&f==0)
             {

             }
             else
             {
                f=1;
                p1[m][j++]=p[i];
                p2++;
             }
         }
         p1[m][0]=p2;
         m++;
     }
     for(i=0;i<t;i++)
     {
         k=p1[i][0];
         cout<<"Case #"<<i+1<<": ";
         for(j=1;j<=k;j++)
         {
             cout<<p1[i][j];
         }
         cout<<endl;
     }

     return 0;
}
