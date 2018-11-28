#include <bits/stdc++.h>

#define Saiyan

using namespace std;

int main()
{
    #ifdef Saiyan
  freopen("inp.txt","r",stdin) ;
  freopen("out.txt","w",stdout) ;
  #endif

  long long int i,j,n,t,a[100],temp,c,z,k;

  cin>>t;

  for(k=1;k<=t;k++)
  {
      c=0;
      cin>>n;
      temp=n;
      while(temp!=0)
      {
          temp/=10;
          c++;
      }

      temp=n;

      for(i=c-1;i>=0;i--)
      {
          a[i]=temp%10;
          temp/=10;
      }

      if(c==1)
      {
          cout<<"Case #"<<k<<": ";
          cout<<n<<endl;

      }
      else
      {
          for(i=c-1;i>0;i--)
          {
              if(a[i]<a[i-1])
              {
                  a[i-1]--;
                  for(j=i;j<c;j++)
                  {
                      a[j]=9;
                  }
              }
          }

          z=0;
      if(a[0]==0)
      {
          z=1;
      }

      cout<<"Case #"<<k<<": ";
      for(i=z;i<c;i++)
      {
         cout<<a[i];
      }
      cout<<endl;

      }


  }

	return 0;
}
