#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
long long md=1000000007;
# define PI  3.14159265358979323846
static pair<double,double> r[2005];static double h[2005],x[2005][2005],y[2005];
bool compare(const pair<double, double>&i, const pair<double, double>&j)
{
    if(i.first==j.first)return i.second < j.second;
    return i.first < j.first;
}
int main()
{
  int t;
  long long n,k;
  //scanf("%d",&t);
  double z,a,b,c;

  std::ifstream in("A-large(1).in");
  //std::ifstream in("a.txt");
  std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
  std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

  std::ofstream out("a-outlarge.txt");
  std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
  std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

  cin>>t;
  for(int test=1;test<=t;test++)
  {
      cin>>n>>k;
      for(int i=0;i<n;i++)
      {
        cin>>r[i].first>>r[i].second;
      }
      sort(r,r+n,compare);
      // for(int i=0;i<n;i++)printf("%lf %lf\n",r[i].first,r[i].second);
      double ans=0.0,curr;
      for(int i=n-1;i>=k-1;i--)
      {
        curr=0.0;
        for(int j=0;j<i;j++)
        {
          y[j]=r[j].first*r[j].second;
        }
        sort(y,y+i);
        // for(int j=0;j<i;j++)printf("%lf ",y[j]);
        // printf("\n");
        for(int j=i-1;j>i-k;j--)
        {
          curr+=2*y[j];
        }
        curr+=2*r[i].first*r[i].second;
        curr+=r[i].first*r[i].first;
        if(curr>ans)ans=curr;
      }
      ans*=PI;
      cout<<"Case #"<<test<<": "<<std::setprecision(6)<<std::fixed<<ans<<endl;

  }

}
