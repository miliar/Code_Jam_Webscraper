#include<bits/stdc++.h>
using namespace std;
char s[10000000];
long long a[1000000],b[1000000];
int main()
{
    long long n,t,i,j,k,l,m,a1,ans,f,mmm=1,mmmm=1;
    cin>>t;
    while(t--)
     {

         cin>>s;
         cin>>n;k=0;f=0;
         for(i=0;i<strlen(s);++i)
         {
             if(s[i]=='-')
             {k++;
             if(i+n>strlen(s))
             {
                 f=1;
                 break;
             }
             else{
                 for(j=i;j<i+n;++j)
                 {
                     if(s[j]=='-')
                     {
                         s[j]='+';
                     }
                     else
                     {
                         s[j]='-';
                     }
                 }
             }
             }
         }
         if(f==1)
         {
             for(i=0;i<strlen(s);++i)
             {
                 if(s[i]=='+')
                 {
                     f=0;
                 }
                 else
                 {
                     f=1;break;
                 }
             }
         }
         if(f==0)
         {
             cout<<"Case #"<<mmmm<<": "<<k<<"\n";
         }
         else
         {
             cout<<"Case #"<<mmmm<<": IMPOSSIBLE"<<"\n";
         }mmmm++;
     }
    return 0;
}
