#include <iostream>
#include <cstdio>
using namespace std;

int main(){
  int T; scanf("%d",&T);
  for(int Case=1; Case<=T; ++Case) {
    string s; cin >> s;
    int len=s.length();
    printf("Case #%d: ",Case);
    if(len==1) {
      cout << s << endl;
      continue;
    }
    bool hasAns = false;
    for(int i=0; i<len-1; ++i) {
      if(s[i]>s[i+1]) {
        --s[i];
        while(i>0 && s[i-1]>s[i]) {
          --i; --s[i];
        }
        for(int j=0; j<i; ++j) printf("%c",s[j]);
        if(i!=0 || s[i]!='0') printf("%c",s[i]);
        for(int j=i+1; j<len; ++j) printf("9");
        puts("");
        hasAns = true;
        break;
      }
    }
    if(!hasAns) cout << s << endl;
  }
  return 0;
}
