#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define FOR(i,f,c) for(int i=f;i<c;i++)
#define FORM(i,f,c) for(int i=f;i>c;i++)
const int  OCCU = 1 ,  VACC = 0;
int N ,K;
vector<int> Toilet(1000);
int LS(int pos)
{
  int Ls= 0;
  if(pos > 0)
  {
  for(int k = pos-1 ; k >= 0 ; k-- )
  {
    if(Toilet[k] == OCCU)
    break;
    Ls++;
  }
}
  return Ls;
}
int RS(int pos)
{
  int Rs=0;
  FOR(k,pos+1,N)
  {
    if(Toilet[k] == OCCU)
    break;
    Rs++;
  }
  return Rs;
}
int  FLS()
{
  vector<int> minspaces;
  vector<int> maxspaces;
  vector<int> maxindex[N];
  vector<int> minindex[N];
  FOR(j,0,N)
  {
    if(Toilet[j] == VACC)
    {
      minspaces.push_back(min(LS(j),RS(j)));
      maxspaces.push_back(max(LS(j),RS(j)));
      maxindex[j].push_back(max(LS(j),RS(j)));
      minindex[min(LS(j),RS(j))].push_back(j);
    }
  }
  sort(minspaces.begin(),minspaces.end());
  sort(maxspaces.begin(),maxspaces.end());
  int nmin , nmax;
  nmin = minindex[minspaces[minspaces.size()-1]].size();
  nmax = maxindex[maxspaces[maxspaces.size()-1]].size();
  if(nmin == 1)
  {
    return minindex[minspaces[minspaces.size()-1]][0];
  }
  else
  {
    pair<int,int> max;
    max.first=-1;
    max.second=-1;
    int loop=0;
    vector<int> lo;
    FOR(l,0,nmin)
    {
      int o = minindex[minspaces[minspaces.size()-1]][l];
      if(maxindex[o][0] > max.second)
      {
      max.first = o;
      max.second = maxindex[o][0];
      loop = 1;
      lo.clear();
      lo.push_back(o);
    }
    else if(maxindex[o][0] == max.second)
    {
      loop++;
      lo.push_back(o);
    }
    }
    if(loop == 1)
    {
      //return maxindex[maxspaces[maxspaces.size()-1]][0];
      return max.first;
    }
    else
    {
      sort(lo.begin(),lo.end());
      return lo[0];
      //sort(maxindex[maxspaces[maxspaces.size()-1]].begin(),maxindex[maxspaces[maxspaces.size()-1]].end());
      //return maxindex[maxspaces[maxspaces.size()-1]][0];
    }
  }
  }
int main()
{
  int T;
  cin >> T;
  FOR(t,1,T+1)
  {
  cin >> N >> K;
  cout << "Case #" << t << ": ";
  int spaces = N , pos=0;
  Toilet.clear();
  Toilet.resize(N);
  int d;
  FOR(i,0,K)
  {
    d = FLS();
    Toilet[d]=OCCU;
  }
  int ls,rs;
  ls = LS(d);
  rs = RS(d);
  cout << max(ls,rs) << " " << min(ls,rs) << endl;
  }
  return 0;
}
