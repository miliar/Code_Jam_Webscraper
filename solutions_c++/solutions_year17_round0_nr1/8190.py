#include <bits/stdc++.h>

using namespace std;
bool check(string s){
  for(int i=0;i<s.size();i++){
    if(s[i]=='-') return true;
  }
  return false;
}
int OwO(string s,int n){
  
  int v[s.size()],ans=0;
  memset(v,0,sizeof(v));
  for(int i=0;i<s.size();i++){
    if(s[i]=='-' && (i+n-1)<s.size() ){
      ans++;
      for(int k=0;k<n;k++){
        s[i+k]=(s[i+k]=='-')?'+':'-';
      }
    }
  }
  if(!check(s)){
    return ans;
  }
  return -1;
}

int main(){
  freopen("A-large.in", "r", stdin);
  freopen("output.out", "w", stdout);
  string s;
  int t,n;
  cin>>t;
  for(int i=1;i<=t;i++){
    cin>>s>>n;
    int ans=OwO(s,n);
    cout<<"Case #"<<i<<": ";
    if(ans<0){
      puts("IMPOSSIBLE");
    }else cout<<ans<<endl;
  }
  return 0;
}