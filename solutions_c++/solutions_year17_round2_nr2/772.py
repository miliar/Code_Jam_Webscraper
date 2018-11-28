#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
string fcia(ll b, ll r, ll y){
  string vrat="";
  if(b>=r && b>=y){
    if(r+y<b)return "IMPOSSIBLE";
    for(int i=0;i<b;i++){
      vrat+="B";
      if(r>0){vrat+="R";r--;}
      if(b-i<=y)vrat+="Y";
    }
  }
  else if(r>=b && r>=y){
    if(b+y<r)return "IMPOSSIBLE";
    for(int i=0;i<r;i++){
      vrat+="R";
      if(b>0){vrat+="B";b--;}
      if(r-i<=y)vrat+="Y";
    }
  }
  else if(y>=b && y>=r){
    if(b+r<y)return "IMPOSSIBLE";
    for(int i=0;i<y;i++){
      vrat+="Y";
      if(b>0){vrat+="B";b--;}
      if(y-i<=r)vrat+="R";
    }
  }
  return vrat;
}
int main() {
  ios::sync_with_stdio(false);
  ll t,n,r,o,y,g,b,v;
  cin>>t;
  for(int cislo=1;cislo<=t;cislo++){
    cout <<"Case #"<<cislo<<": ";
    cin>>n>>r>>o>>y>>g>>b>>v;
    if(b==o){
      if(b+o==n){
        for(int i=0;i<n/2;i++)cout <<"BO";
        cout <<endl;
        continue;
      }
      if(b!=0){cout <<"IMPOSSIBLE\n";continue;}
    }
    if(r==g){
      if(r+g==n){
        for(int i=0;i<n/2;i++)cout <<"RG";
        cout <<endl;
        continue;
      }
      if(r!=0){cout <<"IMPOSSIBLE\n";continue;}
    }
    if(y==v){
      if(y+v==n){
        for(int i=0;i<n/2;i++)cout <<"YV";
        cout <<endl;
        continue;
      }
      if(y!=0){cout <<"IMPOSSIBLE\n";continue;}
    }
    if(b<o || r<g || y<v){cout <<"IMPOSSIBLE\n";continue;}
    string mozno=fcia(b-o, r-g, y-v);
    if(mozno=="IMPOSSIBLE"){cout <<"IMPOSSIBLE\n";continue;}
    for(int i=0;i<mozno.size();i++){
      if(mozno[i]=='B'){
        cout <<"B";
        if(o>0)while(o--)cout <<"OB";
        continue;
      }
      if(mozno[i]=='Y'){
        cout <<"Y";
        if(v>0)while(v--)cout <<"VY";
        continue;
      }
      if(mozno[i]=='R'){
        cout <<"R";
        if(g>0)while(g--)cout <<"GR";
        continue;
      }
    }
    cout <<endl;
  }
  return 0;
}