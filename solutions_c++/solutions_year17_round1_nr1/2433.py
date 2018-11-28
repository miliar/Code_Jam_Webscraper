#include <bits/stdc++.h>
#define N 26
using namespace std;
int w,h;
string mp[N];

bool check(int u,int d,int l,int r){
  if(u<0||d>=h) return 0;
  for(int i=u;i<=d;i++)
    for(int j=l;j<=r;j++)if(mp[i][j]!='?') return 0;
  return 1;
}

void ume(){
  for(int i=0;i<h;i++){
    char ch = '?';
    for(int j=0;j<w;j++){
      if(mp[i][j]!='?')ch = mp[i][j];
      mp[i][j] = ch;
    }
    
    for(int j=w-1;j>=0;j--){
      if(mp[i][j]!='?')ch = mp[i][j];
      mp[i][j] = ch;
    }
  }
}

void ume2(){
  int update = 1;
  while(update){
    update = 0;
    for(int i=0;i<h;i++){
      string str = mp[i];
      if(check(i+1,i+1,0,w-1))mp[i+1] = str,update=1;
      if(check(i-1,i-1,0,w-1))mp[i-1] = str,update=1;
    }

    for(int i=h-1;i>=0;i--){
      string str = mp[i];
      if(check(i+1,i+1,0,w-1))mp[i+1] = str,update=1;
      if(check(i-1,i-1,0,w-1))mp[i-1] = str,update=1;
    }
  }

}

int main(){

  int q,cnt=0;
  cin>>q;
  while(q--){
  cin>>h>>w;
  for(int i=0;i<h;i++)cin>>mp[i];

  ume();
  ume2();
  cout<<"Case #"<<++cnt<<":"<<endl;
  for(int i=0;i<h;i++)cout<<mp[i]<<endl;
  }

  return 0;
}
