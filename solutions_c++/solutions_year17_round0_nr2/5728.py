#include <iostream>

using namespace std;

int main()
{
  int n;
  cin>>n;
  for (int i=1;i<=n;i++)
  {
    string s;
    cin>>s;
    cout<<"Case #"<<i<<": ";
    int z=-1;
    for (int j=0;j<s.size()-1;j++)
    {
      if (s[j]>s[j+1])
	{
	z=j;
	break;}
    }
    if (z==-1)
      {
      cout<<s<<endl;
      continue;
    }
    for (int j=z+1;j<s.size();j++)
      s[j]='9';
    int a=z;
    while (s[z]==s[z-1])
      {
	z--;
	if (z==0)
	  break;
      }
    s[z]--;
    for (int j=z+1;j<=a;j++)
      s[j]='9';
    if (s[0]=='0')
      s.erase(0,1);
    cout<<s<<endl;
  }
  return 0;
}