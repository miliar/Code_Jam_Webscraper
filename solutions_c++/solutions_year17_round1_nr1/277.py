#include<bits/stdc++.h>
using namespace std;
#define int long long
signed main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<":"<<endl;
    int r,c;
    cin>>r>>c;
    string s[r];
    for(int i=0;i<r;i++) cin>>s[i];
    for(int i=0;i<r;i++){
      int f=0;
      for(int j=0;j<c;j++) f|=s[i][j]!='?';
      if(!f) continue;
      for(int j=0;j<c;j++){
	if(s[i][j]=='?') continue;
	int k=j-1;
	while(k>=0&&s[i][k]=='?') s[i][k--]=s[i][j];
	k=j+1;
	while(k<c&&s[i][k]=='?') s[i][k++]=s[i][j];
      }
    }
    for(int i=0;i<r;i++){
      int f=0;
      for(int j=0;j<c;j++) f|=s[i][j]!='?';
      if(!f) continue;
      int k=i-1;
      while(k>=0&&s[k][0]=='?'){
	for(int j=0;j<c;j++) s[k][j]=s[i][j];
	k--;
      }
      k=i+1;
      while(k<r&&s[k][0]=='?'){
	for(int j=0;j<c;j++) s[k][j]=s[i][j];
	k--;
      }
    }
    for(int i=0;i<r;i++) cout<<s[i]<<endl;
  }
  return 0;
}
