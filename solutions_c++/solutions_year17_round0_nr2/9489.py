#include <bits/stdc++.h>

using namespace std;

string disminuir(string s){
  char aux;
    if(int(s[s.length()-1])>48){
      if(s.length()==1 && s[0]=='1'){
      return "";
      }else{
      aux=s.back();
      s.pop_back();
      return s+char(int(aux)-1);
      }
    }else{
        aux=s.back();
        s.pop_back();
        return disminuir(s)+char(57);
    }
  return s;
}

int main(){
ios_base::sync_with_stdio(false);cin.tie(NULL);
int t;
cin>>t;
for(int i=1;i<=t;i++){
  string s;
  bool teach=true;
  cin>>s;
  while(teach){
  string t(s);
  sort(t.begin(),t.end());
    if(t!=s)
      s=disminuir(s);
    else
      teach=false;
  }
  cout<<"Case #"<<i<<": "<<s<<"\n";
}
return 0;
}
