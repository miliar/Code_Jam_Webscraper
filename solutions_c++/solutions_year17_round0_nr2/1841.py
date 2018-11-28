#include<bits/stdc++.h>
using namespace std;

bool ok(string s, int pos, int new_val){
  s[pos]='0'+new_val;
  for(int i=pos+1; i<s.length(); ++i)
      s[i]='9';
  for(int i=1; i<s.length(); ++i){
      if(s[i]<s[i-1])
          return false;
  }
  return true;
}

long long cal(string s, int pos, int new_val){
  s[pos]='0'+new_val;
  for(int i=pos+1; i<s.length(); ++i)
      s[i]='9';
  return stoll(s);
}

int main(){
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  int T, cas=0;
  cin>>T;
  long long ans, N;
  while(T--){
      cin>>N;
      string s=to_string(N);
      ans=1;
      if(s.length()==1){
          ans=N;
      }else{
          bool flag=true;
          for(int i=1; i<s.length(); ++i){
              if(s[i]<s[i-1])
                  flag=false;
          }
          if(flag){
              ans=N;
          }else{
              for(int i=0; i<s.length(); ++i){
                  int num=s[i]-'0';
                  for(int j=num-1; j>=0; --j){
                      if(ok(s, i, j)){
                          ans=max(ans, cal(s, i, j));
                      }
                  }
              }
          }
      }
      cout<<"Case #"<<++cas<<": "<<ans<<endl;
  }
  return 0;
}

