#include <bits/stdc++.h>
using namespace std;

string str;

char revert(char ch)
{
  if(ch == '+') return '-';
  else return '+';
}

bool check()
{
  for(int i=0;i<(int)str.length();i++) if(str[i]=='-') return false;
  return true;
}

int main()
{
  int t;
  cin >> t;
  for(int cas=1;cas<=t;cas++)
  {
    cin >> str;
    int k,l,count=0;
    l=str.length();
    cin >> k;
    for(int i=0;i<(l-k+1);i++)
    {
      if(str[i]=='+') continue;
      for(int j=0;j<k;j++) str[i+j]=revert(str[i+j]);
      count++;
    }
    if(check()) printf("Case #%d: %d\n",cas,count);
    else printf("Case #%d: IMPOSSIBLE\n",cas);
  }
  return 0;
}
