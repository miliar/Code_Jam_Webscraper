#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int t,k;
string s;
int main() {
  ios::sync_with_stdio(false);
  cin>>t;
  for(int cislo=1;cislo<=t;cislo++){
    cin>>s>>k;vector<bool> V(s.size(),false);
    bool doteraz=false;
    for(int i=0;i<s.size()-k+1;i++){
      if(i>=k && V[i-k])doteraz=!doteraz;
      if(s[i]=='+')V[i]=doteraz;
      else V[i]=!doteraz;
      if(V[i])doteraz=!doteraz;
    }
    int pocet=0;
    for(int i=s.size()-k+1;i<s.size();i++){
      if(i>=k && V[i-k])doteraz=!doteraz;
      if(s[i]=='+' && doteraz){pocet=-1;break;}
      if(s[i]=='-' && !doteraz){pocet=-1;break;}
    }
    if(pocet==-1){
      cout <<"Case #"<<cislo<<": IMPOSSIBLE\n";
      continue;
    }
    for(int i=0;i<V.size();i++)if(V[i])pocet++;
    cout <<"Case #"<<cislo<<": "<<pocet<<"\n";
  }
  return 0;
}