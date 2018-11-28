#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include <algorithm>
#include<bitset>
#include<set>
#include<utility>
#include<string>
using namespace std;
const double pi = 3.1415926;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define ll long long
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end();i++)
#define present(c,x) ((c).find(x) != (c).end())

/*int start;
int destination;
void dij()
{
  vector<int> D(sz, default_v);
  set<ii> Q;
  D[start] = 0;
  Q.insert(ii(0,start));
  while(!Q.empty())
  {
    ii top = *Q.begin();
    Q.erase(Q.begin());
    int v = top.second;
    int d= top.first;
    if(v == destination)
    {
      break;
    }
    tr(G[v],it)
    {
    int vv = it->first;
      int cost =
      if(D[index] > d + cost)
    }
  }





}

*/

struct cake{
  ll r;
  ll h;
  double scemian;
};
cake ck[1005];
bool cmp(cake i,cake j) // sort from small to large
{
  if(i.r < j.r)
    return true;
  else if(i.r > j.r)
    return false;
  else{
    if(i.scemian< j.scemian)
    return true;
    else return false;
  }
//    return i < j;
}
int bi_search(ll* A,int lo,int hi,ll e) // return the index of X such that X <= e
{
  int mi = 0;
  while(lo < hi)
  {
    mi = (lo + hi) >> 1;
    e < A[mi] ? hi = mi: lo = mi +1;
  }
  return --lo;
}
double dp[1005][1005];
int main()
{
    freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
int T;
scanf("%d",&T);
int n,k;
for(int t = 1; t <= T;t++)
{
  printf("Case #%d: ",t);
  scanf("%d%d",&n,&k);
  for(int i = 1; i<= n;i++)
  {
    scanf("%lld%lld",&ck[i].r,&ck[i].h);
    ck[i].scemian = 2*pi*ck[i].r*ck[i].h;
  }
  sort(ck+1,ck+1+n,cmp);
  for(int i = 0; i<= n;i++)
    dp[i][0] = 0;
    dp[1][1] = ck[1].scemian;
for(int i = 1; i<= n;i++)
{
  for(int j = 1; j <= i;j++)
  {
    dp[i][j] = max(dp[i-1][j-1]+ck[i].scemian,dp[i-1][j]);
  }
}
double dk[1005];
for(int i = k; i <= n;i++)
{
  dk[i] = -1;
  for(int j = i; j>= k;j--)
  {
    dk[i] = max(dk[i],dp[j-1][k-1]+ck[i].scemian+ck[i].r*ck[i].r*pi);
  }
}
int max_index = -1;
double max_val = -1;
for(int i = k;i <= n;i++)
{
    if(max_val < dk[i])
    {
      max_val = dk[i];
    }

}
printf("%lf\n",max_val);
}

  return 0;
}
