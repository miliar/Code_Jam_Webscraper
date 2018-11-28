//In the Name of God
//Ya Ali

#include<bits/stdc++.h>

#define int long long

#define pb push_back

#define err(A) cout<<#A<<" = "<<(A)<<endl

using namespace std;

bool good(int x)
{
  int lst=10;
  while(x)
    {
      int d=x%10;

      if(d>lst)
	return false;
      lst=d;
      
      x/=10;
    }
  return true;
}

main()
{
  ios::sync_with_stdio(0);cin.tie(0);

  int T;
  cin>>T;
  for(int t=0;t<T;t++)
    {
      int x;
      cin>>x;

      int ans;
      
      for(int _=x;_>0;_--)
	if(good(_))
	  {
	    ans=_;
	    break;
	  }

      cout<<"Case #"<<t+1<<": "<<ans<<endl;
    }
  
  return 0;
}
