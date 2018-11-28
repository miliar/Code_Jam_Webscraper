#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
long long md=1000000007;
int main()
{
  int t;
  long long n,k,x,y,z,a,b,c,l,r;
  //scanf("%d",&t);

  std::ifstream in("C-large.in");
  //std::ifstream in("a.txt");
  std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
  std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

  std::ofstream out("c3-out.txt");
  std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
  std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

  cin>>t;
  for(int test=1;test<=t;test++)
  {
      cin>>n>>k;
      x=0,y=1;
      while(x<k)
      {
        x+=y;
        if(x>=k){x-=y;break;}
        y*=2;
      }
      z=n-x;
      a=z/y;
      if(z%y>=k-x)a++;
      l=(a-1)/2;
      r=l;
      if(a%2==0)r=l+1;

      cout<<"Case #"<<test<<": "<<r<<" "<<l<<endl;

  }

}
