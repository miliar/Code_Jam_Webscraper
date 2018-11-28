#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
int t,r,c;
vector<string> V;
vector<char> def;
vector<vector<int> > hrany;
vector<bool> bol;
int prehladajhore(int x,int y){
  while(true){
    x--;
    if(x<0 || V[x][y]=='#')break;
    if(V[x][y]=='-' || V[x][y]=='|')return x*c+y;
  }
  return -1;
}
int prehladajdole(int x,int y){
  while(true){
    x++;
    if(x>=r || V[x][y]=='#')break;
    if(V[x][y]=='-' || V[x][y]=='|')return x*c+y;
  }
  return -1;
}
int prehladajvlavo(int x,int y){
  while(true){
    y--;
    if(y<0 || V[x][y]=='#')break;
    if(V[x][y]=='-' || V[x][y]=='|')return x*c+y;
  }
  return -1;
}
int prehladajvpravo(int x,int y){
  while(true){
    y++;
    if(y>=c || V[x][y]=='#')break;
    if(V[x][y]=='-' || V[x][y]=='|')return x*c+y;
  }
  return -1;
}
bool dfs(int vrchol,char co){
  if(def[vrchol]!=co && def[vrchol]!='?')return false;
  def[vrchol]=co;
  for(int i=0;i<hrany[vrchol].size();i++){
    int sused=hrany[vrchol][i];
    if(bol[sused])continue;
    bol[sused]=true;
    if(!dfs(sused,co))return false;
  }
  return true;
}
int main(){
  ios::sync_with_stdio(false);
  cin>>t;
  for(int sada=1;sada<=t;sada++){
    cin>>r>>c;
    V.resize(r);
    for(int i=0;i<r;i++)cin>>V[i];
    cout <<"Case #"<<sada<<": ";
    hrany.assign(r*c,vector<int>(0));
    def.assign(r*c,'?');
    bool celezle=false;
    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++){
        if(V[i][j]=='.'){
            int hore=prehladajhore(i,j),dole=prehladajdole(i,j),vpravo=prehladajvpravo(i,j),vlavo=prehladajvlavo(i,j);
            if(hore==-1 && dole==-1 && vpravo==-1 && vlavo==-1){celezle=true;break;}
            if(hore==-1 && dole==-1 && vpravo==-1 && vlavo!=-1){
              if(def[vlavo]!='|')def[vlavo]='-';
              else {celezle=true;break;}
            }
            if(hore==-1 && dole==-1 && vpravo!=-1 && vlavo==-1){
              if(def[vpravo]!='|')def[vpravo]='-';
              else {celezle=true;break;}
            }
            if(hore!=-1 && dole==-1 && vpravo==-1 && vlavo==-1){
              if(def[hore]!='-')def[hore]='|';
              else {celezle=true;break;}
            }
            if(hore==-1 && dole!=-1 && vpravo==-1 && vlavo==-1){
              if(def[dole]!='-')def[dole]='|';
              else {celezle=true;break;}
            }
            if(hore!=-1 && dole!=-1){
              if(vpravo==-1 && vlavo==-1)celezle=true;
              if(vpravo!=-1 && vlavo!=-1)celezle=true;
              if(def[dole]!='|' && def[hore]!='|'){def[dole]='-';def[hore]='-';}
              else {celezle=true;break;}
            }
            if(vpravo!=-1 && vlavo!=-1){
              if(dole==-1 && hore==-1)celezle=true;
              if(dole!=-1 && hore!=-1)celezle=true;
              if(def[vpravo]!='-' && def[vlavo]!='-'){def[vpravo]='|';def[vlavo]='|';}
              else {celezle=true;break;}
            }
            if(vpravo!=-1 && dole!=-1){hrany[vpravo].push_back(dole);hrany[dole].push_back(vpravo);}
            if(vpravo!=-1 && hore!=-1){hrany[vpravo].push_back(hore);hrany[hore].push_back(vpravo);}
            if(vlavo!=-1 && hore!=-1){hrany[vlavo].push_back(hore);hrany[hore].push_back(vlavo);}
            if(vlavo!=-1 && dole!=-1){hrany[vlavo].push_back(dole);hrany[dole].push_back(vlavo);}
        }
        else if(V[i][j]=='|' || V[i][j]=='-'){
          if(i>0 && (V[i-1][j]=='|' || V[i-1][j]=='-'))
          {
            if(def[i*c+j]!='|')def[i*c+j]='-';
            else {celezle=true;}
            if(def[(i-1)*c+j]!='|')def[(i-1)*c+j]='-';
            else celezle=true;
          }
          if(i<r-1 && (V[i+1][j]=='|' || V[i+1][j]=='-'))
          {
            if(def[i*c+j]!='|')def[i*c+j]='-';
            else {celezle=true;}
            if(def[(i+1)*c+j]!='|')def[(i+1)*c+j]='-';
            else celezle=true;
          }
          if(j<c-1 && (V[i][j+1]=='|' || V[i][j+1]=='-'))
          {
            if(def[i*c+j]!='-')def[i*c+j]='|';
            else {celezle=true;}
            if(def[i*c+j+1]!='-')def[i*c+j+1]='|';
            else celezle=true;
          }
          if(j>0 && (V[i][j-1]=='|' || V[i][j-1]=='-'))
          {
            if(def[i*c+j]!='-')def[i*c+j]='|';
            else {celezle=true;}
            if(def[i*c+j-1]!='-')def[i*c+j-1]='|';
            else celezle=true;
          }
        }
      }
      if(celezle)break;
    }
    bol.assign(r*c,false);
    for(int i=0;i<r*c;i++){
      if(bol[i] || def[i]=='?')continue;
      if(!dfs(i,def[i]))celezle=true;
    }


    if(celezle){cout <<"IMPOSSIBLE\n";continue;}
    cout<<"POSSIBLE\n";
    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++){
        if(V[i][j]=='-' || V[i][j]=='|'){
            if(def[i*c+j]!='?')cout <<def[i*c+j];
            else cout<<"|";
        }
        else cout <<V[i][j];
      }cout <<endl;
    }
  }
  return 0;
}
