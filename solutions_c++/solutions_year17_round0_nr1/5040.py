#include<bits/stdc++.h>

using namespace std;
int k;
string s;

void input()
{
  cin>>s>>k;
  
}
int main()
{
  int num=0;
  int T;
  cin>>T;
  while(T--)
    {num++;
      input();
      int cnt=0;
      for(int i=0;i<s.size();i++)
	if(s[i]=='+' || i+k>s.size())
	  continue;
	else{
	  for(int j=i;j<i+k;j++)
	    if(s[j]=='+')
	      s[j]='-';
	    else
	      s[j]='+';
	  cnt++;
	}
      bool ok=true;
      for(int i=0;i<s.size();i++)
	if(s[i]=='-')
	  ok=false;
      // cout<<s<<endl;
      cout<<"Case #"<<num<<": ";
      if(ok)
	cout<<cnt<<endl;
      else
	cout<<"IMPOSSIBLE"<<endl;
    }
		       
	return 0;
}

