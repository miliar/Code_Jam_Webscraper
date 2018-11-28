//In the Name of God
//Ya Ali

#include<bits/stdc++.h>

#define ld long double

#define err(A) cout<<#A<<" = "<<(A)<<endl

using namespace std;

int main()
{
  ios::sync_with_stdio(0);cin.tie(0);

  int T;
  cin>>T;
  for(int t=0;t<T;t++)
    {
      int d,n;
      cin>>d>>n;

      ld mxt=0;
      
      for(int i=0;i<n;i++)
	{
	  ld x,v;
	  cin>>x>>v;
	  mxt=max(mxt,(d-x)/v);
	}
      
      ld ans=d/mxt;
      
      /**/cout<<setprecision(6)<<fixed;
      cout<<"Case #"<<t+1<<": "<<ans<<endl;
    }
  
  return 0;
}
