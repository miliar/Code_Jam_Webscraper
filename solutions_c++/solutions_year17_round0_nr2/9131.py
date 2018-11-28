#include<iostream>
using namespace std;

int greattidy( unsigned long long int x)
{
    unsigned long long int k=x,q;
    int a[20],temp[20],y=0,r,i=0;
    if(k>=0 && k<10)
    {
        return k;
    }

   else{

    while(k!=0)
    {
        r=k%10;
        q=k/10;
        k=q;
        a[i]=r;
        i=i+1;

    }
int n=0;
    for(int j=i-1;j>=0;j--)
    {

      for(int b=j-1;b>=0;b--)
      {
          if(!(a[j]<=a[b]))
          {
              y=1;
          }
      }
    }




    if(y==0)
    {
        return x;
    }
else if(y==1)
   {return -1;}
}
}

int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
         unsigned long long int m;
       unsigned long long int x;
       cin>>x;
       for(unsigned long long int j=x;j>=0;j--)
       {
           m=greattidy(j);
           if(m!= -1)
           {
               goto x1;
           }
       }

      x1: {cout<<"Case #"<<i<<": "<<m<<"\n";}
    }
    return 0;
}
