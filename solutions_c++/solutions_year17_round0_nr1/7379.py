#include <bits/stdc++.h>
using namespace std;


int a[1007];
int x=1;
int m,k;
int inf = 1000000007;

int func() 
{
  int s[m]; 
  for(int i=0;i<m;i++) 
  {
    s[i] = 0;
  }
  int sum=0, ans=0;
  for(int i=0;i<m;i++) 
  {
    s[i] = (a[i]+sum)%2 != x;
    sum += s[i] - (i>=k-1?s[i-k+1]:0);
    ans += s[i];
    if(i>m-k and s[i]!=0) 
      return inf;
  }
  return ans;
}

int main() 
{
  int t;
  scanf("%d",&t);
  string str;
  int ans;

  for(int it=1;it<=t;it++)
  {
    cin>>str>>k;
   // cout<<s;
    m=str.size();
    for(int i=0;i<str.size();i++)
    {
      if(str[i]=='+')
        a[i]=1;
      else
        a[i]=0;
    }
    ans=func();
    if(ans==inf)
      printf("Case #%d: IMPOSSIBLE\n",it);
    else
      printf("Case #%d: %d\n",it,ans);
  }
  return 0;
}