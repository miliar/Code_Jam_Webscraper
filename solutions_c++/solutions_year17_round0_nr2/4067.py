#include <cstdio>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

bool chk = false;
string N;

bool promising(int len){
  for(int i=0;i<len;i++)
    if(N[i]>N[i+1]) return false;
  return true;
}

void su(int idx){
  if(idx == N.size()){
    chk=true; return;
  }
  for(;N[idx]>='0';N[idx]--){
    if(promising(idx))
      su(idx+1);
    else{
      for(int i=idx;i<N.size();i++)
        N[i]='9';
      return;
    }
    if(chk) return;
  }
}

int main(){
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    long long ans=0;
    chk = false;
    cin >> N;
    su(0);
    for(int i=0;i<N.size();i++)
      ans = ans * 10 +( N[i] - '0');
    printf("Case #%d: %lld\n",t,ans);
  }
}
