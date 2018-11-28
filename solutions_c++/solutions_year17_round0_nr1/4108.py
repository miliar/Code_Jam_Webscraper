#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main(){
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    string S; int K,ans=0;
    cin >> S >> K;
    for(int i=0;i<=S.size()-K;i++){
      if(S[i]=='-'){
        ans++;
        for(int j=0;j<K;j++){
          if(S[i+j]=='-') S[i+j]='+';
          else S[i+j]='-';
        }
      }
    }
    bool chk = false;
    for(int i=S.size()-K+1;i<S.size();i++){
      if(S[i]=='-'){
        chk = true;
        break;
      }
    }
    printf("Case #%d: ",t);
    if(!chk) printf("%d\n",ans);
    else printf("IMPOSSIBLE\n");
  }
}
