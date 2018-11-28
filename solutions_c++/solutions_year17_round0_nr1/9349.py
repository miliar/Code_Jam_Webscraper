#include<bits/stdc++.h>
#define ll long long
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define mod 1000000007
using namespace std;



int Find_flips(vi A, int N)
{
  queue<int> f;
  int ans = 0;

  for (int i = 0; i < A.size(); ++i)
  {
    if (!f.empty() && f.front() <= i - N)
      f.pop();

    if ((A[i] ^ (f.size() % 2 == 0)) == 1)
    {
      if (i > A.size() - N)
        return -1;

        ans++;
        f.push(i);
    }
  }

  return ans;
}


main()
{

freopen("A-large.in","r",stdin);
freopen( "kflips.txt", "w", stdout );
  int T;
  cin>>T;

  for(int t=1;t<=T;t++)
  {
      string A;
      cin>>A;
      int k;
      cin>>k;

      vi v;
      for(int i=0;i<A.size();i++)
      {
          if(A[i]=='+')
            v.pb(1);
          else
            v.pb(0);
      }

      int ans = Find_flips(v,k);

      if(ans==-1)
        cout<<"Case #"<<t<<": "<<"IMPOSSIBLE\n";
      else
       cout<<"Case #"<<t<<": "<<ans<<"\n";
  }

}
