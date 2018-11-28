#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
#define ll long long
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
string s[30];
int g[26][4];
int x[26],y[26];
bool chk(int a,int b,int x)
{
  int i,j;
  int l,r,m,n;
  m=g[x][1];
  n=g[x][0];
  l=g[x][3];
  r=g[x][2];
  if(a<m)
   m=a;
  if(a>n)
   n=a;
  if(b<l)
   l=b;
  if(b>r)
   r=b;
  for(i=m;i<=n;i++)
  {
    for(j=l;j<=r;j++)
     if(s[i][j]!='?' && (s[i][j]-'A')!=x)
       break;
    if(j<=r)
     break;
  }
  if(i<=n)
   return false;
  g[x][1]=m;
  g[x][0]=n;
  g[x][3]=l;
  g[x][2]=r;
  for(i=m;i<=n;i++)
  {
    for(j=l;j<=r;j++)
     s[i][j]=x+'A';
  }
  return true;
};
void fll(int a,int b,int c,int d,int m)
{
  int i,j;
  if(a>c)
  {
    swap(a,c);
    swap(b,d);
  }
  if(b<=d)
  {
   for(i=a;i<=c;i++)
   {
     for(j=b;j<=d;j++)
      s[i][j]=m+'A';
   }
  }
  else
  {
    for(i=a;i<=c;i++)
    {
     for(j=b;j>=d;j--)
      s[i][j]=m+'A';
    }
  }
};
bool r[26];
int main()
{
  //freopen("A-large(1).in", "r", stdin);
  //freopen("a.out", "w", stdout);
  int t,i,j,n,k,m,c;
  scanf("%d",&t);
  for(c=1;c<=t;c++)
  {
    scanf("%d%d",&n,&m);
    for(i=0;i<n;i++)
     cin>>s[i];
    int cnt;
    for(i=0;i<26;i++)
    {
      g[i][0]=-1;
      g[i][1]=n;
      g[i][2]=-1;
      g[i][3]=m;
    }
    memset(x,0,sizeof(x));
    memset(y,0,sizeof(y));
    memset(r,false,sizeof(r));
    for(i=0;i<n;i++)
    {
      for(j=0;j<m;j++)
      {
        if(s[i][j]!='?')
        {
          r[s[i][j]-'A']=true;
          if(g[s[i][j]-'A'][0]<i)
           g[s[i][j]-'A'][0]=i;
          if(g[s[i][j]-'A'][1]>i)
           g[s[i][j]-'A'][1]=i;
          if(g[s[i][j]-'A'][2]<j)
           g[s[i][j]-'A'][2]=j;
          if(g[s[i][j]-'A'][3]>j)
           g[s[i][j]-'A'][3]=j;
        }
      }
    }
    for(i=0;i<26;i++)
    {
      if(r[i])
      {
        for(j=g[i][1];j<=g[i][0];j++)
        {
          for(k=g[i][3];k<=g[i][2];k++)
           s[j][k]=i+'A';
        }
      }
    }
    for(i=0;i<n;i++)
    {
      for(j=0;j<m;j++)
      {
        if(s[i][j]=='?')
        {
          for(k=0;k<26;k++)
          {
            if(r[k] && chk(i,j,k))
            {
              break;
            }
          }

        }
      }
    }
    cout<<"Case #"<<c<<": \n";
    for(i=0;i<n;i++)
     cout<<s[i]<<endl;
  }
  return 0;
}
