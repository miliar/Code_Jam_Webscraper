//In the Name of God
//Ya Ali

#include<bits/stdc++.h>

#define int long long

#define pb push_back

#define err(A) cout<<#A<<" = "<<(A)<<endl

using namespace std;

main()
{
  ios::sync_with_stdio(0);cin.tie(0);

  int T;
  cin>>T;
  for(int t=0;t<T;t++)
    {
      int n,k;

      cin>>n>>k;
      
      multiset<int> s;

      s.insert(n);

      for(k--;k--;)
	{
	  int d=*s.rbegin();
	  s.erase(s.find(d));
	  s.insert((d-1)/2);
	  s.insert(d/2);
	}

      int d=*s.rbegin();
      int ls=(d-1)/2;
      int rs=d/2;

      cout<<"Case #"<<t+1<<": "<<rs<<" "<<ls<<endl;
    }
  
  return 0;
}
