#include<iostream>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for(int t=0;t<T;t++)
  {
    string s;
    cin>>s;
    int k;
    cin>>k;
    int ans=0;
    bool imp=false;
    for(int i=0;i<s.size();i++)
    {
      if(s[i]=='-')
      {
        if(i+k>s.size())
        {
          imp=true;
          break;
        }
        ans++;
        for(int j=i;j<i+k;j++)
        {
          if(s[j]=='-') s[j]='+';
          else if(s[j]=='+') s[j]='-';
        }
      }
    }
    if(imp)
      cout<<"Case #"<<(t+1)<<": IMPOSSIBLE"<<endl;
    else
      cout<<"Case #"<<(t+1)<<": "<<ans<<endl;
  }
  return 0;
}
