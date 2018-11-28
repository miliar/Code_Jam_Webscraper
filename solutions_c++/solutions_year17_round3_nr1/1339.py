#include<bits/stdc++.h>

using namespace std;

const int maxN=1e4+100;

double r[maxN],h[maxN];
vector<long double> vec;
int n,k;

void input()
{
  cin>>n>>k;
  for(int i=1;i<=n;i++)
    cin>>r[i]>>h[i];
}
int main()
{
  long double PI=acos(-1);
  //cout<<PI<<endl;
  int T;
  cin>>T;
  int cnt=0;
  while(T--)
    {
      double ans=0,sum=0;
      cnt++;
      input();
      for(int i=1;i<=n;i++)
	{
	  sum=PI*r[i]*r[i]+2*PI*r[i]*h[i];
	  
	  vec.clear();
	  for(int j=1;j<=n;j++)
	    if(i!=j)
	      vec.push_back(2*PI*r[j]*h[j]);
	  sort(vec.begin(),vec.end());
	  int rem=k-1;
	  for(int j=(int)vec.size()-1;j>=0;j--){
	    if(rem<=0)
	      break;
	    sum+=vec[j];
	    rem--;}
	  ans=max(ans,sum);
	}
      cout<<fixed<<setprecision(10);
      cout<<"Case #"<<cnt<<": "<<ans<<endl;
    }
  return 0;
}
