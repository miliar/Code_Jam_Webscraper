#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
long long md=1000000007;
int main()
{
  int t;
  long long n,k,x,y,z,c,l,r;



  //scanf("%d",&t);

  std::ifstream in("B-large.in");
  //std::ifstream in("a.txt");
  std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
  std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

  std::ofstream out("b3-out.txt");
  std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
  std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

  cin>>t;
  for(int test=1;test<=t;test++)
  {
      cin>>n;
      int a[20],b[20];
      l=0;
      x=n;y=0;
      while(x>0)
      {

        a[y++]=x%10;
        x/=10;

      }
      bool flag=false;l=-1;
      for(int i=y-1;i>=0;i--)
      {
        if(i==0){b[i]=a[i];break;}
        else if(a[i]<a[i-1]){b[i]=a[i];flag=false;}
        else if(a[i]==a[i-1]){if(flag==false){l=i;flag=true;};b[i]=a[i];flag=true;}
        else
        {
          if(flag==true)r=l;
          else r=i;
          b[r]=a[r]-1;
          for(int j=r-1;j>=0;j--)b[j]=9;
          break;
        }
      }
      z=0;
      for(int i=y-1;i>=0;i--)
      {
        z*=10;z+=b[i];
      }
      cout<<"Case #"<<test<<": "<<z<<endl;

  }

}
