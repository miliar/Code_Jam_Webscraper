#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main()
{
  ll t;
  cin>>t;


  while(t--)
  {
      // ll ans = 0;
      ll n;
      cin>>n;
      vector<int> v;

      ll temp = n;
      while(temp!=0)
      {
        v.push_back(temp%10);
        temp /= 10;
      }

      reverse(v.begin(), v.end());
      ll len = v.size();
      if(len==1)
      {
        cout<<n<<endl;
        continue;
      }
      ll prev = v[len-1];
      for(ll i=len-2;i>=0;i--)
      {
        prev = v[i+1];
        if(prev>=v[i])
        {
          continue;
        }
        else if( prev < v[i]){
          v[i]--;
          for(ll j=i+1;j<=len;j++)
            v[j] = 9;
        }
      }
      // for(int i=0;i<v.size();i++)
      //   cout<<v[i]<<" ";
      ll ans = 0;
      ll i=0;
      while(v[i]==0)
        i++;
      for(int j=i;j<v.size();j++)
        ans = ans*10 + v[j];

      cout<<ans<<endl;
  }
}
