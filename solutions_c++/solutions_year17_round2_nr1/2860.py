#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
long long md=1000000007;
int main()
{
  int t;
  long long n,k,d,m,s;
  double x,y,z,a,b,c,l,r;
  //scanf("%d",&t);

  std::ifstream in("A-large.in");
  //std::ifstream in("a.txt");
  std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
  std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

  std::ofstream out("alarge.txt");
  std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
  std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

  cin>>t;
  for(int test=1;test<=t;test++)
  {
      cin>>d>>n;
      double min =0.0;
      z=(double)(d);
      for(int i=0;i<n;i++)
      {
        cin>>k>>s;
        x=(double)(k);
        y=(double)(s);
        a=(z-x)/y;
        if(min<a)min=a;
      }
      min=z/min;
      // printf("Case #"1: 101.000000");
      cout<<"Case #"<<test<<": "<<std::setprecision(6)<< std::fixed<<min<<endl;

  }

}
