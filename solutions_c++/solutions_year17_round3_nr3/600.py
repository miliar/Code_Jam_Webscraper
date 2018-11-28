#include<bits/stdc++.h>
using namespace std;

bool cmp(double a, double b)
{
  return a>b;
}

int main()
{
  int T; cin>>T;
  for(int tc = 1; tc<=T; tc++)
  {
    int N, K;
    cin>>N>>K;
    double U; cin>>U;
    priority_queue<double,vector<double>,greater<double> > pq;
    for(int i = 0; i<N; i++)
    {
      double x; cin>>x;
      pq.push(x);
    }
    while(U>1e-8)
    {
      double c = pq.top(); pq.pop();
      c+=0.0001;
      U-=0.0001;
      pq.push(c);
    }
    double ans = 1;
    while(!pq.empty())
    {
      ans*=pq.top(); pq.pop();
    }
    cout<<"Case #"<<tc<<": "<<fixed<<setprecision(8)<<ans<<endl;
  }
}
