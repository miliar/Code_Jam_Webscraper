#include <iostream>
using namespace std;

string solve(string s,int len)
{
  for(i = len - 1; i >= 1; i--)
  {
    if(s[i] < s[i-1])
    {
      s[i-1] = s[i-1]-1;
      for(j = i;j < len; j++)
        s[j] ='9';
    break;
    }
  }
  if(!i)
    return s;
  else
    return solve(s,len);
}

int main()
{
  int t,k=1;
  cin>>t;
  while(t--)
  {
    string s;
    cin>>s;
    cout<<"Case #"<<k++<<": "<<solve(s,s.size())<<endl;
  }
  return 0;
}
