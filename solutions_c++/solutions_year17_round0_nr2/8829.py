#include<bits/stdc++.h>
using namespace std;
int main()
{
  freopen("input.txt","r",stdin);
  freopen("output1.txt","w",stdout);
  int t,test;
  cin>>t;
  for(test=1;test<=t;test++)
  {
      long long int num,n,i,k,res=0;
      cin>>n;
      int len=0,j=0,flag=0;
      num=n;
      while(num!=0)
      {
          len++;
          num/=10;
      }
      int a[len];
      if(len==1)
      cout<<"Case #"<<test<<": "<<n;
      else
      {
          for(i=n;i>=0;i--)
          {
              j=len-1;
            num=i;
              do
              {
                 a[j]=num%10;
                 num/=10;
                 j--;
              }while(num!=0);
              for(j=0;j<len-1;j++)
              {
                  if(a[j]<=a[j+1])
                    flag++;
              }
              if(flag==(len-1))
              {cout<<"Case #"<<test<<": "<<n;goto abc;}
              else if(flag!=(len-1))
              {

              for(int p=1;p<len;p++)
              {
                for(j=0;j<len;j++)
                {
                  if(a[j]>a[j+1])
                  {
                      a[j]--;
                      for(k=j+1;k<=len;k++)
                      {
                          a[k]=9;
                      }
                  }
                 }}
            for(k=0;k<len;k++)
            res=(res*10)+a[k];
            cout<<"Case #"<<test<<": "<<res;
            goto abc;

      }}
      }
      abc:
      cout<<"\n";
    }
    return 0;
  }
