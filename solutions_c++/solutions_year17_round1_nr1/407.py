#include<bits/stdc++.h>
using namespace std;

char t[30][30];
int H,W;

void func(){
  for(int i=0;i<H;i++){
    for(int j=0;j<W;j++){
      if(t[i][j]!='?')continue;
      if(j>0)t[i][j]=t[i][j-1];
    }
  }
  
  for(int i=0;i<H;i++){
    for(int j=W-2;j>=0;j--){
      if(t[i][j]!='?')continue;
      t[i][j]=t[i][j+1];
    }
  }

  for(int i=0;i<H;i++){
    for(int j=0;j<W;j++){
      if(t[i][j]!='?')continue;
      if(i>0)t[i][j]=t[i-1][j];
    }
  }
  
  for(int i=H-2;i>=0;i--){
    for(int j=0;j<W;j++){
      if(t[i][j]!='?')continue;
      t[i][j]=t[i+1][j];
    }
  }  
}

int main(){
  int Tc;
  cin>>Tc;
  for(int tc=1;tc<=Tc;tc++){
    cout<<"Case #"<<tc<<":"<<endl;
    cin>>H>>W;
    for(int i=0;i<H;i++){
      for(int j=0;j<W;j++){
        cin>>t[i][j];
      }
    }
    func();
    for(int i=0;i<H;i++){
      for(int j=0;j<W;j++)cout<<t[i][j];
      cout<<endl;
    }
  }
  return 0;
}
