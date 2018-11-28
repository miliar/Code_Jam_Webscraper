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
  ll cnt=1,n;
  std::vector<char> v(1007);
  std::vector<pair<int,char> > cols;
  std::vector<int> slots;

  while(t--)
  {
      ifile>>n;
      pair<int,char > r,o,y,g,b,vio;
      ifile>>r.f>>o.f>>y.f>>g.f>>b.f>>vio.f;
      bool poss=true;
      if(r.f>n/2||o.f>n/2||y.f>n/2||g.f>n/2||b.f>n/2||vio.f>n/2){poss=false;}
      fill(v.begin(),v.end(),'a');
      r.s='R';
      b.s='B';
      y.s='Y';
      cols.clear();
      cols.pb(r);
      cols.pb(b);
      cols.pb(y);
      sort(cols.begin(),cols.end());
      reverse(cols.begin(),cols.end());
      // L(i,3)
      // {cout<<cols[i].f<<" "<<cols[i].s<<endl;}
      int max=cols[0].f;

      for(int i=0;i<max;i++)
      {
        v[2*i]=cols[0].s;
      }
      int c,d;
      c=cols[1].f;
      d=cols[2].f;
      int ind=1;
      while(c!=d)
      {
          v[ind]=cols[1].s;
          c--;
          ind+=2;
      }
      slots.clear();
      L(i,n)
      {
        if(v[i]=='a'){slots.pb(i);}
      }
      // L(i,3)
      // {cout<<cols[i].f<<" "<<cols[i].s<<endl;}

      bool color=false;
      L(i,slots.size())
      {
        //cout<<slots[i]<<" ";
        if(color)
        {
          v[slots[i]]=cols[1].s;
          color=false;
        }
        else
        {
          v[slots[i]]=cols[2].s;
          color=true;
        }
      }

      // L(i,n)
      // {cout<<v[i]<<" ";}

      if(poss)
      {
        ofile<<"Case #"<<cnt<<": ";
        L(i,n)
        {ofile<<v[i];}
        ofile<<endl;
      }
      else
      {
        ofile<<"Case #"<<cnt<<": "<<"IMPOSSIBLE"<<endl;
      }
      cnt++;
  }
  ofile.close();
  ifile.close();
}
