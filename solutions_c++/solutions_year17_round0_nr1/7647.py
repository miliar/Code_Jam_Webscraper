#include<bits/stdc++.h>
using namespace std;

int ans,k;
string s;

char flip(char c)
{
  if(c=='-') return '+';
  return '-';
}

int main()
{
  int qw;
  cin>>qw;
  for(int q=1;q<=qw;q++)
    {
      cin>>s>>k;
      ans=0;
      for(int i=0;i<s.size();i++)
	if(s[i]=='-')
	  {
	    if(i+k>s.size())
	      ans=-1;
	    else
	      {
		ans++;
		for(int j=i;j<i+k;j++)
		  s[j]=flip(s[j]);
	      }
	  }
      cout<<"Case #"<<q<<": ";
      if(ans==-1) cout<<"IMPOSSIBlE\n";
      else cout<<ans<<endl;
    }
}
