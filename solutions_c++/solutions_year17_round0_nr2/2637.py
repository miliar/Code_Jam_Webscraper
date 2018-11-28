#include<iostream>
#include<string>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
  {
    string s;
    cin>>s;
    for(int i=s.size()-1;i>0;i--)
    {
      for(int j=i-1;j>=0;j--)
        if(s[j]>s[i])
        {
          for(int k=j+1;k<s.size();k++)
            s[k]='9';
          s[j]--;
          break;
        }
    }
    int ind=-1;
    for(int i=0;i<s.size();i++)
    {
      if(s[i]=='0')
        ind=i;
      else
        break;
    }
    cout<<"Case #"<<t<<": "<<s.substr(ind+1,s.size()-ind+1)<<endl;
  }
  return 0;
}
