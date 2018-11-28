#include <iostream>
#include <cstdio>
using namespace std;
const int INF = 20000000;
#define FOR(i,n) for(int i=0,_n=n; i<_n; ++i)

int flips(int a[], int M, int N) {
  int want=1;
  int s[M]; FOR(i,M) s[i] = 0;
  int sum=0, ans=0;

  for(int i=0,_n=M; i<_n; ++i){
    s[i] = (a[i]+sum)%2 != want;
//    cout<<s[i]<<" "<<(a[i] + sum)%2<<" "<<sum<<" "<<a[i]<<endl;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
//    cout<<sum<<endl;
    ans += s[i];
//    cout<<ans<<endl;
    if(i>M-N and s[i]!=0) return -1;
  }
  return ans;
}

int main() {
  freopen("ingcg.txt", "r", stdin);
  freopen("outgcg.txt", "w", stdout);
  ios_base::sync_with_stdio(false);cin.tie(0);
  int t; cin>>t;
  for(int tc=1;tc<=t;tc++)
  {
      string s; int k;
      cin>>s>>k;
      int a[s.length()];
      int M = s.length();
      for(int i=0; i < M;i++)
      {
          if(s[i]=='+')a[i]=1;
          else a[i]=0;
      }
      int val=flips(a,M,k);
      if(val==-1)
      {
          cout<<"Case #"<<tc<<": IMPOSSIBLE\n";
      }
      else{
          cout<<"Case #"<<tc<<": "<<val<<"\n";
      }
  }
}
