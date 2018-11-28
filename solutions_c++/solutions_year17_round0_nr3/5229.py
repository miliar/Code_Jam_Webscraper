#include<bits/stdc++.h>

using namespace std;

#define L second.first
#define R second.second
#define len first
#define MP make_pair
set<pair<int,pair<int,int> > >myst;
int n,k;

int main()
{
  int num=0;
  int T;
  cin>>T;
  while(T--)
    {
      num++;
      myst.clear();
  cin>>n>>k;
  myst.insert(MP(n,MP(1,n)));
  for(int i=1;i<k;i++)
    {
      pair<int,pair<int,int> > p=*myst.rbegin();
      myst.erase(p);
      int mid=(p.L+p.R)/2;
      myst.insert(MP(mid-p.L,MP(p.L,mid-1)));
      myst.insert(MP(p.R-mid,MP(mid+1,p.R)));
    }
  pair<int,pair<int,int> > p=*myst.rbegin();
  //cout<<p.len<<endl;
  p.len--;
  cout<<"Case #"<<num<<": ";
  cout<<ceil(p.len/2.0)<<" "<<floor(p.len/2.0)<<endl;
    }
  return 0;
}
