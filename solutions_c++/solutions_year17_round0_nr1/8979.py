#include <iostream>
#include<bits/stdc++.h>
using namespace std;
const int INF = 20000000;
#define FOR(i,n) for(int i=0,_n=n; i<_n; ++i)

int flips(int a[], int M, int N, int want) {
  int s[M]; FOR(i,M) s[i] = 0;
  int sum=0, ans=0;
  FOR(i,M) {
    s[i] = (a[i]+sum)%2 != want;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    ans += s[i];
    if(i>M-N and s[i]!=0) return INF;
  }
  return ans;
}

int main() {
  int  n,k,t,j=1;
  string s1;
  ifstream cin("A-large (1).in");
  ofstream cout("codejam2.txt");
  cin>>t;
  while(t--)
  {
      cin>>s1>>k;
      int a[s1.length()];
      for(int i=0;i<s1.length();i++)
      {
          if(s1[i]=='+')
          {
              a[i]=1;
          }
          else
          {
              a[i]=0;
          }
      }
      int ans=flips(a,s1.length(),k,1);
      if(ans==INF)
      {
        cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
        j++;
      }
      else
      {
        cout<<"Case #"<<j<<": "<<ans<<endl;
        j++;
      }
  }
}
