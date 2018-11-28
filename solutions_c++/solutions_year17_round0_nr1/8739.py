#include <bits/stdc++.h>
using namespace std;
const int MAXIMUM = 10000000;
#define FOR(i,n) for(int i=0,_n=n; i<_n; ++i)

int flips(int a[], int M, int N, int want) {
  int s[M]; FOR(i,M) s[i] = 0;
  int sum=0, ans=0;
  FOR(i,M) {
    s[i] = (a[i]+sum)%2 != want;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    ans += s[i];
    if(i>M-N and s[i]!=0) return MAXIMUM;
  }
  return ans;
}

int main() {
  int t;
  cin>>t;
  for(int i=0; i<t; ++i)
  {
    char ch; cin.get(ch);
    char stringname[1000];
    cin>>stringname;
    int len = strlen(stringname);
    int a[len];
    for(int j=0; j<len; ++j)
    {
        if(stringname[j] == '+')
            a[j] = 1;
        else
            a[j] = 0;
    }
    int k;
    cin>>k;
    int ans = flips(a, len, k, 1);
    if(ans == MAXIMUM)
        cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
    else
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
  }
}
