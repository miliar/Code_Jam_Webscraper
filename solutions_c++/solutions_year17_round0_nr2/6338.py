#include<bits/stdc++.h>
using namespace std;
char s[10000000];
long long a[1000000],b[1000000];
int main()
{
    long long n,t,i,j,k,l,m,a1,ans,f,mmm=1;
    cin>>t;m=1;
    while(t--)
     {cin>>n;
         for(i=0,j=n;j>0;++i,j=j/10)
         {k=j%10;
             a[i]=k;
         }
     l=0;
     for(j=i-1;j>=0;--j)
     {
         b[l]=a[j];l++;
     }

      for(i=1;i<l;++i)
      {
          if(b[i]>=b[i-1])
          {

          }
          else
          {
              for(k=i;k<l;++k)
              {
                  b[k]=9;
              }
              b[i-1]=b[i-1]-1;
             j=i-1;
             for(;j>0;--j)
             {
                 if(b[j]<b[j-1])
                 {
                     b[j]=9;
                     b[j-1]=b[j-1]-1;
                 }
                 else
                 {
                     break;
                 }
             }
              break;
          }
      }
      long long mm=0;
      cout<<"Case #"<<mmm<<": ";mmm++;
      for(i=0;i<l;++i)
      {
          if(b[i]==0 && mm==0)
          {
              mm=1;
          }
          else
          { mm=1;
              cout<<b[i];
          }
      }cout<<"\n";
     }
    return 0;
}
