#include<bits/stdc++.h>
using namespace std;

int main()
{
  int n;
  string s;
  cin>>n;
  for(int q=1;q<=n;q++)
    {
      cin>>s;
      for(int i=s.size()-1;i>0;i--)
	if(s[i]<s[i-1])
	  {
	    s[i-1]--;
	    for(int j=i;j<s.size();j++)
	      s[j]='9';
	  }
      int i=0;
      while(s[i]=='0') i++;
      cout<<"Case #"<<q<<": ";
      for(;i<s.size();i++)
	cout<<s[i];
      cout<<endl;
    }
}
			
