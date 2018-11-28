#include<bits/stdc++.h>
#define tr(v,it) for(auto it=v.begin();it!=v.end();it++)
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define F first
#define S second
#define endl "\n"
#define mod 1000000007
#define pi 3.141592653589793
const int N=1e7+1;

using namespace std;

int main()
{
//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
long long t;
cin>>t;
for(int lauda=1;lauda<=t;lauda++)
{

long long n,k;
cin>>n>>k;

vector<long long>v(n+2);
v[0]=1;v[n+1]=1;
for(int j=1;j<=k;j++)
{
  vector<int>l(n+2),r(n+2);
  int p=0;
  for(int i=1;i<=n;i++)
  {
    l[i]=p;
    if(v[i]==1)
    p=i;
  }
  p=n+1;
  for(int i=n;i>=1;i--)
  {
    r[i]=p;
    if(v[i]==1)
    p=i;
  }
int a=-1;
  vector< int > f;
  for(int i=1;i<=n;i++)
  {
  if(v[i]==0)
  {
    int ls=i-l[i];
    int rs=r[i]-i;
    if(min(ls,rs)>a)
    {
      f.clear();
      f.pb(i);
      a=min(ls,rs);
    }
    else
    if(min(ls,rs)==a)
    {
      f.pb(i);
    }
  }
  }

if(f.size()==1)
{
  int indx=f[0];
  v[indx]=1;
  //cout<<indx<<endl;

  if(j==k)
{
  int count=0;
  for(int m=indx-1;m>=0;m--)
  {
    if(v[m]==1)
    break;
    else
    count++;
  }
  int ls=count;

  count=0;
  for(int m=indx+1;m<=n+1;m++)
  {
    if(v[m]==1)
    break;
    else
    count++;
  }
int rs=count;
  cout<<"Case #"<<lauda<<": "<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
}
  continue;
}

int indx;
a=-1;
  for(int i=0;i<f.size();i++)
  {
    int ls=f[i]-l[f[i]];
    int rs=r[f[i]]-f[i];

    if(max(ls,rs)>a)
    indx=f[i],a=max(ls,rs);
  }


  v[indx]=1;
  //cout<<indx<<" here"<<endl;

  if(j==k)
  {
    int count=0;
    for(int m=indx-1;m>=0;m--)
    {
      if(v[m]==1)
      break;
      else
      count++;
    }
    int ls=count;

    count=0;
    for(int m=indx+1;m<=n+1;m++)
    {
      if(v[m]==1)
      break;
      else
      count++;
    }
int rs=count;
cout<<"Case #"<<lauda<<": "<<max(ls,rs)<<" "<<min(ls,rs)<<endl;

  }

}

}

  return 0;
}
