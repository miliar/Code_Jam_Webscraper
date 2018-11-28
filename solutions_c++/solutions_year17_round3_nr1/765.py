#include<bits/stdc++.h>
using namespace std;

int N,K;
vector<pair<double,double> > A;

bool cmp1(pair<double,double> p1, pair<double,double> p2)
{
  return p1.first < p2.first;
}
bool cmp2(pair<double,double> p1, pair<double,double> p2)
{
  double r1 = p1.first;
  double h1 = p1.second;
  double r2 = p2.first;
  double h2 = p2.second;
  return 2*acos(-1)*h1*r1 > 2*acos(-1)*h2*r2;
}

int main()
{
  int T; cin>>T;
  for(int tc = 1; tc <= T; tc++)
  {
    A.clear();
    cin>>N>>K;
    for(int i = 0; i<N; i++)
    {
      double r,h;
      cin>>r>>h;
      A.push_back(make_pair(r,h));
    }
    double maxans = 0;
    sort(A.begin(),A.end(),cmp2);
    for(int i = 0; i<N; i++)
    {
      //treat i as first pancake
      double ans = 0;
      ans += A[i].first*A[i].first*acos(-1);
      ans += 2*acos(-1)*A[i].first*A[i].second;
      int left = K-1;
      for(int j = 0; j<N && left>0; j++){
        if(i==j) continue;
        if(A[i].first<A[j].first) continue;
        left--;
        ans += 2*acos(-1)*A[j].first*A[j].second;
      }
      maxans = max(maxans,ans);
    }
    cout<<fixed<<setprecision(10)<<"Case #"<<tc<<": "<<maxans<<endl;
  }
  return 0;
}
