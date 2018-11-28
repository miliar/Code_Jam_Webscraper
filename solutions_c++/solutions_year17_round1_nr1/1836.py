#include<bits/stdc++.h>
using namespace std;
int main(){
  int t;
  cin>>t;
  for(int o=1;o<=t;o++){
    int h,w;
    string mp[25];
    cin>>h>>w;
    for(int i=0;i<h;i++)
      cin>>mp[i];
    for(int i=0;i<h;i++)
      for(int j=0;j<w;j++){
	if(mp[i][j]!='?'){
	  int l=j,r=j;
	  for(int k=j+1;k<w&&mp[i][k]=='?';k++)r=k;
	  for(int k=j-1;k>=0&&mp[i][k]=='?';k--)l=k;
	  for(int k=l;k<=r;k++)mp[i][k]=mp[i][j];
	}
      }
    for(int i=1;i<h;i++)
      for(int j=0;j<w;j++)
	if(mp[i][j]=='?')mp[i][j]=mp[i-1][j];
    for(int i=h-2;i>=0;i--)
      for(int j=0;j<w;j++)
	if(mp[i][j]=='?')mp[i][j]=mp[i+1][j];
    cout<<"Case #"<<o<<":"<<endl;
    for(int i=0;i<h;i++)
      cout<<mp[i]<<endl;
  }
  return 0;
}
