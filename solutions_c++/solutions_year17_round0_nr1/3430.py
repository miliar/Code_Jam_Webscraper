#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

#define INF 1000000000
#define REP(i,a,b) for(int i = int(a); i<=int(b);i++)

int main() {
  int TC;
  scanf("%d",&TC);
  REP(a,1,TC){
    string s;
    int k;
    int flag = 0;
    cin>>s>>k;
    // cout<<s<<endl;
    int counter = 0;
    for(int i = 0; i <= s.length()-k; i++){
      if(s[i]=='-'){
        s[i] = '+';
        for(int j = 1; j < k; j++){
          s[i+j] == '+'? s[i+j] = '-':s[i+j] = '+';
        }
        // cout<<s<<endl;
        counter++;
      }
    }
    for(int i = 0 ;i < s.length();i++){
      if(s[i]=='-')
        flag = 1;
    }
    if(flag)
      printf("Case #%d: IMPOSSIBLE\n",a);
    else
      printf("Case #%d: %d\n",a,counter);
    // cout<<s.length()<<" "<<k<<endl;
  }

}
