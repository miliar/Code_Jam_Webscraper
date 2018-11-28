#include <bits/stdc++.h>
#include <iostream>
#include <bitset>

using namespace std;

#define L(i,n) for(int i=0;i<n;i++)
#define ALL(X) (X).begin(),(x).end()
#define DRC(n)  char n;scanf("%c",&n)
#define DRI(n) int n;scanf("%d",&n)
#define DR2I(n,m) int n,m;scanf("%d%d",&n,&m)
#define RI(n) scanf("%d",&n)
#define ll long long
#define pb(n) push_back(n)
#define pii pair<int,int>
#define mp(i,j) make_pair(i,j)
#define f first
#define s second
#define MAX_INT 10000007
#define LEEP(i,n) for(int i=1;i<=n;i++)


int main()
{
  ll t;
  ifstream ifile;
  ofstream ofile;
  ifile.open("input");
  ofile.open("Output");
  ifile>>t;
  ll cnt=1,n,d;

  while(t--)
  {
    ifile>>d>>n;
    std::vector<pii > v;
    L(i,n)
    {
      ll k,s;
      ifile>>k>>s;
        v.pb(mp(k,s));
    }
    sort(v.begin(),v.end());
    double speed;
    std::vector<double > time;
    L(i,n)
    {
      double temp=(double)(d-v[i].f)/v[i].s;
      time.pb(temp);
    }
    double max=-1;
    L(i,n)
    {
      if(time[i]>max){max=time[i];}
    }
    speed=(double)d/max;
      ofile<<"Case #"<<cnt<<": "<<fixed<<setprecision(7)<<speed<<endl;
      cnt++;
  }
  ofile.close();
  ifile.close();
}
