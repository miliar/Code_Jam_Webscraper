#include<bits/stdc++.h>
#define X first
#define Y second
using namespace std;

const long double pi=3.14159265358979323846264338327950288419716939937510;
typedef pair<long long,long long> pii;
long long n,k,ans,sum;
pii P[2000];
multiset<long long>s;

int main()
{
  ios_base::sync_with_stdio(false);cin.tie(0);
  int qw;
  cin>>qw;
  for(int q=1;q<=qw;q++)
    {
      cin>>n>>k;
      ans=sum=0;
      s.clear();
      for(int i=0;i<n;i++)
	cin>>P[i].X>>P[i].Y;
      sort(P,P+n);
      for(int i=0;i<n;i++)
	{
	  ans=max(ans,sum-(s.size()==k?(*s.begin()):0)+2*P[i].X*P[i].Y+P[i].X*P[i].X);
	  //	  cout<<sum<<"#$@"<<s.size()<<" "<<k<<endl;
	  sum+=2*P[i].X*P[i].Y;
	  s.insert(2*P[i].X*P[i].Y);
	  if(s.size()>k)
	    {
	      sum-=*s.begin();
	      s.erase(s.begin());
	    }
	}
      cout<<"Case #"<<q<<": ";
      cout<<fixed<<setprecision(8)<<ans*pi<<endl;
    }
}
