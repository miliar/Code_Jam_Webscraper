#include <iostream>
#include <cstdio>
using namespace std;

int main() {
  int T; scanf("%d",&T);
  for(int Case=1; Case<=T; ++Case) {
    int K;
    string s; cin >> s >> K;
    int len = s.length();
    int ans=0;
    bool isPossible=true;
    for(int i=0; i<len-K+1; ++i) {
      if(s[i]=='-') {
        for(int j=i; j<i+K; ++j) s[j]=s[j]=='-'?'+':'-';
        ++ans;
      }
    }
    for(int i=len-K+1; i<len; ++i) { if(s[i]=='-') isPossible=false; }
    if(isPossible)
      printf("Case #%d: %d\n",Case,ans);
    else
      printf("Case #%d: IMPOSSIBLE\n",Case);
  }
  return 0;
}
