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
#define MAX_INT 100000007
#define LEEP(i,n) for(int i=1;i<=n;i++)
#define pi 3.141592653589793238462643

bool sortinrev1(const pair<int,double> &a,
               const pair<int,double> &b)
{
       return (a.first > b.first);
}

bool sortinrev2(const pair<double,int> &a,
               const pair<double,int> &b)
{
       return (a.first > b.first);
}

int main()
{
  ll t;
  ifstream ifile;
  ofstream ofile;
  ifile.open("input");
  ofile.open("Output");
  ifile>>t;
  ll cnt=1,n;

  while(t--)
  {
    int n,k;
    ifile>>n>>k;
    std::vector<pair<int,double> > v;
    std::vector<pair<double,int> > v1;

    L(i,n)
    {
        int h,r;
        ifile>>r>>h;
        v.pb(mp(r,2*pi*r*h));
        v1.pb(mp(2*pi*r*h,r));
    }
    sort(v.begin(),v.end(),sortinrev1);
    sort(v1.begin(),v1.end(),sortinrev2);
    double area=0,area1=0;

    L(i,n-k+1)
    {
      area1=0;
      area1+=pi*v[i].f*v[i].f;
      area1+=v[i].s;
      int r_max=v[i].f;
      int count=0;
      bool done=false;
      L(j,n)
      {
        if(!done && v[i].f==v1[j].s && v[i].s==v1[j].f){done=true;continue;}
        if(count==k-1){break;}
        if(v1[j].s>r_max){continue;}
        else
        {
          area1+=v1[j].f;
          count++;
        }
      }
      if(area<area1)
      {area=area1;}
    }

      ofile<<"Case #"<<cnt<<": "<<fixed<<setprecision(7)<<area<<endl;
      cnt++;
    }
  ofile.close();
  ifile.close();
}
