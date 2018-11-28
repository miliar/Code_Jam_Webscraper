#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double db;
const int N=1e6+5;
int ac, aj;
vector<pair<pair<int,int>,int>> v;
void solve()
{
  v.clear();
  int result=0;
  int free_exchange=0; //
  int fixed_c=0; //
  int fixed_j=0; //
  vector<int> buy; //
  
  scanf("%d%d",&ac,&aj);
  for(int i=1; i<=ac; ++i)
  {
    int d,c; scanf("%d%d", &d,&c);
    v.push_back(make_pair(make_pair(d,c),0));
    fixed_c+=c-d;
  }
  for(int i=1; i<=aj; ++i)
  {
    int d,c; scanf("%d%d", &d,&c);
    v.push_back(make_pair(make_pair(d,c),1));
    fixed_j+=c-d;
  }
  sort(v.begin(),v.end());
  for(int i=1; i<(int)v.size(); ++i)
  {
    if(v[i-1].second!=v[i].second)
    {
      ++result;
      free_exchange+=v[i].first.first-v[i-1].first.second;
    }
    else
    {
      if(v[i].second==0) buy.push_back(v[i].first.first-v[i-1].first.second);
      else buy.push_back(v[i].first.first-v[i-1].first.second);
    }
  }
  if(v.back().second!=v[0].second)
  {
    ++result;
    free_exchange+=(1440-v.back().first.second)+v[0].first.first;
  }
  else
  {
    if(v[0].second==0) buy.push_back((1440-v.back().first.second)+v[0].first.first);
    else buy.push_back((1440-v.back().first.second)+v[0].first.first);
  } 
  sort(buy.begin(),buy.end());reverse(buy.begin(),buy.end());
  int sum=free_exchange;
  int Result=1e9;
  for(int i=0; i<=(int)buy.size(); ++i)
  { 
    if(i!=0) 
    {
      sum+=buy[i-1];  
      result+=2;
    }
    if((fixed_c+sum>=720&&fixed_j+sum>=720)) Result=min(Result,result);
  }
  printf("%d\n",Result);
}
int main()
{
	int tt; scanf("%d",&tt); 
	for(int i=1; i<=tt; ++i)
	{
		printf("Case #%d: ",i);
		solve();
	}
}
