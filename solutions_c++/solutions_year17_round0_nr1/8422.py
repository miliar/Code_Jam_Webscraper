//In the Name of God
//Ya Ali

#include<bits/stdc++.h>

#define err(A) cout<<#A<<" = "<<(A)<<endl

using namespace std;

int main()
{
  ios::sync_with_stdio(0);cin.tie(0);

  int T;
  cin>>T;
  for(int t=0;t<T;t++)
    {
      string s;
      int k;
      cin>>s>>k;

      int ans=0;
      
      bool P=true;
      for(int i=0;i<s.size();i++)
	if(s[i]=='-')
	  {
	    if(i+k>s.size())
	      P=false;
	    else
	      {
		ans++;
		for(int j=0;j<k;j++)
		  s[i+j]=(s[i+j]=='+'?'-':'+');
	      }
	  }

      
      cout<<"Case #"<<t+1<<": ";
      if(P) cout<<ans<<endl;
      else  cout<<"IMPOSSIBLE"<<endl;
    }
  
  return 0;
}
