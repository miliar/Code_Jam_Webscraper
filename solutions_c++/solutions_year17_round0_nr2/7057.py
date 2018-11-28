#include "bits/stdc++.h"
using namespace std;
string ans;
string limit;

string toString(long long int n)
{
  if(n==0)return "0";
  string ans;
  while(n)
  {
    char di='0'+(n%10);
    n/=10;
    ans=string(1,di)+ans;
  }
  return ans;
}

void clean(string & s)
{
  while(s.size()>0 && s[0]=='0')
    s.erase(0,1);
  if(s.size()==0)
    s="0";
}
bool isLessOrEqual(string & curAns)
{
  if(curAns.size()<limit.size())
    return 1;
  if(curAns.size()>limit.size())
    return 0;
  for(int i=0;i<curAns.size();i++)
  {
    if(curAns[i]>limit[i])
      return 0;
    if(curAns[i]<limit[i])
      return 1;
  }
  return 1;
}

bool solve(int in,char maxVal)
{
  if(in==limit.size())
    return 1;
  for(char choice=ans[in]-1;choice>=maxVal;choice--)
  {
    ans[in]=ans[in]-1;
    // Check if less
    string curAns;
    for(int i=0;i<in;i++)
      curAns=curAns+ans[i];//Error?
    for(int i=in;i<limit.size();i++)
      curAns=curAns+ans[in];
    if(!isLessOrEqual(curAns))
    {
      continue;
    }
    if(solve(in+1,max(maxVal,choice)))
    {
      return 1;
    }
  }
  ans[in]='9'+1;
  return 0;
}
int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
  {
    long long int n;
    cin>>n;
    limit=toString(n);
    ans=string(limit.size(),'9'+1);
    solve(0,'0');
    clean(ans);
    cout<<"Case #"<<t<<": "<<ans<<endl;
  }
}
