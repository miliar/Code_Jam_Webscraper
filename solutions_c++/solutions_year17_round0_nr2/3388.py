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
    cin>>s;
    // cout<<s<<endl;
    int flag = 0;
    for(int k = 0; k<s.length();k++){
      for(int i = 0; i<s.length()-1;i++){
        if(s[i]>s[i+1]){
          s[i] = s[i]-1;
          for(int j = i+1 ; j< s.length();j++){
            s[j] = '9';
          }
        }
      }
      
    }
    s.erase(0, min(s.find_first_not_of('0'), s.size()-1));
    cout<<"Case #"<<a<<": "<<s<<endl;
  }

}
