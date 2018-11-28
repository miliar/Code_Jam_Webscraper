#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
#define ll long long
vector<int>v;
ll pw(ll a,ll b)
{
  ll x=1;
  while(b)
  {
    if(b&1)
     x*=a;
    a*=a;
    b>>=1;
  }
  return x;
};
struct node
{
  int ind,mn,mx;
}a[1000001];
bool cmp(node n,node m)
{
   if(n.mn!=m.mn)
    return n.mn>m.mn;
   if(n.mx!=m.mx)
   return n.mx>m.mx;
   return n.ind<m.ind;
};
int cnt;
void sol(int l,int r)
{
  if(l>r)
   return;
  int mid=(l+r)/2;
  a[cnt].ind=mid;
  a[cnt].mn=min(mid-l,r-mid);
  a[cnt++].mx=max(mid-l,r-mid);
  sol(l,mid-1);
  sol(mid+1,r);
};
int main()
{
  //freopen("C-small-2-attempt0.in", "r", stdin);
  //freopen("a.out", "w", stdout);
  int t,i,j,n,k;
  scanf("%d",&t);
  //cout<<t<<endl;
  for(i=1;i<=t;i++)
  {
     cnt=0;
     scanf("%d%d",&n,&k);
     sol(1,n);
     sort(a,a+cnt,cmp);
     cout<<"Case #"<<i<<": "<<a[k-1].mx<<' '<<a[k-1].mn<<endl;
  }
  return 0;
}
